"""
Suíte de Testes Automatizados de Componente (Backend / PostgreSQL)
Projeto: StockFlow
Framework: Pytest
Objetivo: Validar regras de negócio e integridade transacional SQL sem interface gráfica.
Conformidade ISTQB CTFL v4.0: Teste de Componente / Teste Caixa-Branca
"""

import sys
import os

# Garante que o diretório raiz do StockFlow esteja no caminho de busca do Python
sys.path.insert(0, os.getcwd())

import pytest
from database.connection import conectar
from database.vendas import finalizar_venda_multi_item


@pytest.fixture
def conexao_db():
    """Fixture que fornece uma conexão ativa com o PostgreSQL do Docker."""
    conexao = conectar()
    assert conexao is not None, "Falha ao conectar com o banco de dados PostgreSQL do Docker Compose."
    yield conexao
    conexao.close()


def test_conexao_banco_dados(conexao_db):
    """CT-BACK-001: Validar se a conexão com o PostgreSQL está operacional."""
    cursor = conexao_db.cursor()
    cursor.execute("SELECT 1;")
    resultado = cursor.fetchone()
    cursor.close()
    assert resultado[0] == 1, "A consulta de teste no banco falhou."


def test_impedir_venda_quantidade_zero_ou_negativa():
    """CT-BACK-002: Validar se a regra de negócio rejeita quantidades inválidas diretamente na função."""
    cliente_id = 1
    itens_invalidos = [
        {"produto_id": 1, "quantidade": 0, "preco_unitario": 100.0}
    ]
    
    # Chama a função real do backend: finalizar_venda_multi_item
    sucesso, mensagem = finalizar_venda_multi_item(carrinho=itens_invalidos, forma_pagamento="Dinheiro", cliente_id=cliente_id)
    
    assert sucesso is False, "A função permitiu registrar venda com quantidade zero ou negativa."


def test_verificar_rollback_em_item_inexistente(conexao_db):
    """CT-BACK-003: Validar a atomicidade (ROLLBACK) quando um dos itens da venda não existe."""
    cursor = conexao_db.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM vendas;")
    total_vendas_antes = cursor.fetchone()[0]
    
    itens_com_erro = [
        {"produto_id": 99999, "quantidade": 1, "preco_unitario": 9999.00}
    ]
    
    sucesso, mensagem = finalizar_venda_multi_item(carrinho=itens_com_erro, forma_pagamento="PIX", cliente_id=1)
    
    assert sucesso is False
    
    cursor.execute("SELECT COUNT(*) FROM vendas;")
    total_vendas_depois = cursor.fetchone()[0]
    cursor.close()
    
    assert total_vendas_antes == total_vendas_depois, "O ROLLBACK falhou e a transação incompleta persistiu no banco!"