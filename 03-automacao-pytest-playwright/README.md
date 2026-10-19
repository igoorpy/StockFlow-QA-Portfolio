# Automação de Testes de Backend & Componentes (Pytest)

Este diretório contém os scripts de testes automatizados de nível de componente e integração de banco de dados para o sistema **StockFlow**, utilizando o framework **Pytest**.

## Escopo dos Testes (Backend / PostgreSQL)

| ID do Teste | Função / Módulo | Técnica CTFL | Objetivo do Teste |
| :--- | :--- | :--- | :--- |
| **CT-BACK-001** | `test_conexao_banco_dados` | Teste de Infraestrutura | Validar se a conexão com o container PostgreSQL está ativa. |
| **CT-BACK-002** | `test_impedir_venda_quantidade_zero_ou_negativa` | Caixa-Branca / Regra de Negócio | Garantir que a função `finalizar_venda_multi_item` rejeita quantidades inválidas. |
| **CT-BACK-003** | `test_verificar_rollback_em_item_inexistente` | Atomicidade (ACID / SQL) | Garantir o `ROLLBACK` de transações corrompidas sem afetar o banco. |

---

## Executar os Testes

Com os containers Docker do StockFlow rodando, execute o comando abaixo no terminal:

```bash
# A partir da pasta do sistema StockFlow com a .venv ativa:
PYTHONPATH=. .venv/bin/pytest "../StockFlow-QA-Portfolio/03-automacao-pytest-playwright/testes_vendas_backend.py" -v