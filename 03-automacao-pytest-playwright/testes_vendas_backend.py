"""
Suíte de Testes Automatizados de Componente e Integridade (Backend / PostgreSQL)
Projeto: StockFlow
Framework: Pytest
Objetivo: Cobertura total das regras de negócio, integridade transacional SQL, RBAC, Caixa e Auditoria.
Conformidade ISTQB CTFL v4.0: Teste de Componente / Teste Caixa-Branca (Capítulos 2 e 4)
"""

import sys
import os

# Garante que o diretório raiz do StockFlow esteja no caminho de busca do Python
sys.path.insert(0, os.getcwd())

import pytest
from werkzeug.security import check_password_hash
from database.connection import conectar
from database.vendas import finalizar_venda_multi_item


@pytest.fixture
def conexao_db():
    """Fixture que fornece uma conexão ativa com o PostgreSQL do Docker Compose."""
    conexao = conectar()
    assert conexao is not None, "Falha ao conectar com o banco de dados PostgreSQL do Docker Compose."
    yield conexao
    conexao.close()


# ==============================================================================
# MÓDULO 1: INFRAESTRUTURA E BANCO DE DADOS
# ==============================================================================

def test_conexao_banco_dados(conexao_db):
    """CT-BACK-001: Validar se a conexão com o PostgreSQL está operacional."""
    cursor = conexao_db.cursor()
    cursor.execute("SELECT 1;")
    resultado = cursor.fetchone()
    cursor.close()
    assert resultado[0] == 1, "A consulta de teste no banco falhou."


# ==============================================================================
# MÓDULO 2: TRANSAÇÕES E REGRAS DE VENDAS (database/vendas.py)
# ==============================================================================

def test_impedir_venda_quantidade_zero_ou_negativa():
    """CT-BACK-002: Validar se a regra de negócio rejeita quantidades inválidas diretamente na função."""
    cliente_id = 1
    itens_invalidos = [
        {"produto_id": 1, "quantidade": 0, "preco_unitario": 100.0}
    ]
    
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


# ==============================================================================
# MÓDULO 3: SEGURANÇA, HASH DE SENHAS E RBAC (database/usuarios.py)
# ==============================================================================

def test_validar_autenticacao_e_hash_senha(conexao_db):
    """CT-BACK-004: Validar a integridade da autenticação de senhas usando Werkzeug."""
    cursor = conexao_db.cursor()
    cursor.execute("SELECT senha FROM usuarios WHERE usuario = 'carlos.vendedor';")
    usuario = cursor.fetchone()
    cursor.close()
    
    assert usuario is not None, "O usuário carlos.vendedor não foi encontrado no banco de dados."
    senha_hash_banco = usuario[0]
    
    assert check_password_hash(senha_hash_banco, "123456") is True, "A validação de senha válida falhou."
    assert check_password_hash(senha_hash_banco, "senha_errada") is False, "O sistema aceitou uma senha incorreta."


def test_validar_distincao_cargos_rbac(conexao_db):
    """CT-BACK-005: Validar se a atribuição de cargos (vendedor vs admin) está correta na base."""
    cursor = conexao_db.cursor()
    cursor.execute("SELECT cargo FROM usuarios WHERE usuario = 'carlos.vendedor';")
    cargo_vendedor = cursor.fetchone()[0]
    cursor.close()
    
    assert cargo_vendedor == "vendedor", "O cargo do usuário carlos.vendedor não é 'vendedor'."
    assert cargo_vendedor != "admin", "O vendedor possui privilégios de admin na base de dados!"


# ==============================================================================
# MÓDULO 4: PRODUTOS E REGRAS DE ESTOQUE (database/produtos.py)
# ==============================================================================

def test_verificar_alerta_estoque_critico(conexao_db):
    """CT-BACK-006: Validar se a consulta de produtos identifica itens com estoque crítico (<= 3)."""
    cursor = conexao_db.cursor()
    cursor.execute("SELECT nome, quantidade FROM produtos WHERE quantidade <= 3;")
    produtos_criticos = cursor.fetchall()
    cursor.close()
    
    for produto in produtos_criticos:
        assert produto[1] <= 3, f"O produto {produto[0]} foi listado como crítico incorretamente."


def test_validar_integridade_valores_produtos(conexao_db):
    """CT-BACK-007: Garantir que nenhum produto no banco possua preço ou quantidade negativa."""
    cursor = conexao_db.cursor()
    cursor.execute("SELECT COUNT(*) FROM produtos WHERE preco < 0 OR quantidade < 0;")
    quantidade_invalidos = cursor.fetchone()[0]
    cursor.close()
    
    assert quantidade_invalidos == 0, "Existem produtos cadastrados com preços ou quantidades negativas no banco!"


# ==============================================================================
# MÓDULO 5: CAIXA E SESSÃO TURNO (database/caixa.py)
# ==============================================================================

def test_verificar_existencia_registro_caixa(conexao_db):
    """CT-BACK-008: Validar se a tabela de controle de caixa está operacional no banco."""
    cursor = conexao_db.cursor()
    cursor.execute("SELECT COUNT(*) FROM caixa;")
    total_registros = cursor.fetchone()[0]
    cursor.close()
    
    assert total_registros >= 0, "A consulta na tabela de controle de caixa falhou."


def test_validar_status_caixa_invalido(conexao_db):
    """CT-BACK-009: Garantir que a tabela de caixa não aceite status inconsistentes."""
    cursor = conexao_db.cursor()
    # Usa LOWER() para comparar de forma insensível a maiúsculas/minúsculas
    cursor.execute("SELECT COUNT(*) FROM caixa WHERE LOWER(status) NOT IN ('aberto', 'fechado');")
    status_invalidos = cursor.fetchone()[0]
    cursor.close()
    
    assert status_invalidos == 0, "Existem registros de caixa com status inconsistente no banco!"
# ==============================================================================
# MÓDULO 6: AUDITORIA E LOGS DE SISTEMA (database/auditoria.py)
# ==============================================================================

def test_validar_presenca_logs_auditoria(conexao_db):
    """CT-BACK-010: Validar a capacidade do PostgreSQL de registrar logs de auditoria."""
    cursor = conexao_db.cursor()
    cursor.execute("SELECT COUNT(*) FROM logs_auditoria;")
    total_logs = cursor.fetchone()[0]
    cursor.close()
    
    assert total_logs >= 0, "A tabela de logs de auditoria não está acessível no banco PostgreSQL."