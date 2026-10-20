# Automação de Testes de Componente, Integridade e Cobertura de Backend

Este repositório contém a suíte de testes automatizados de nível de componente, integração de banco de dados e medição de cobertura de código para o sistema StockFlow, desenvolvida em Python com Pytest e Pytest-Cov.

---

## Escopo dos Testes de Backend (Conformidade ISTQB CTFL v4.0)

A suíte abrange a validação direta de regras de negócio, controle de acesso (RBAC), integridade de transações no PostgreSQL e chamadas de funções do backend (técnicas de caixa-branca e cobertura de instrução - CTFL v4.0 Capítulo 4.3).

| ID do Teste | Módulo / Função Alvo | Técnica Aplicada | Objetivo do Teste | Status |
| :--- | :--- | :--- | :--- | :---: |
| CT-BACK-001 | database/connection.py | Teste de Infraestrutura | Validar se a conexão com o banco de dados PostgreSQL está operacional. | PASSED |
| CT-BACK-002 | database/vendas.py | Teste Caixa-Branca / Regra de Negócio | Garantir que a função finalizar_venda_multi_item rejeita itens com quantidade <= 0. | PASSED |
| CT-BACK-003 | database/vendas.py | Integridade Transacional (ACID) | Validar o procedimento de ROLLBACK completo ao tentar processar venda com item inexistente. | PASSED |
| CT-BACK-004 | database/usuarios.py | Segurança / Criptografia | Validar a equivalência de hash PBKDF2/Werkzeug para autenticação de usuários. | PASSED |
| CT-BACK-005 | database/usuarios.py | Controle de Acesso (RBAC) | Confirmar que o perfil vendedor não possui privilégios de administrador na base de dados. | PASSED |
| CT-BACK-006 | database/produtos.py | Regra de Negócio / Filtro | Validar a identificação de produtos com estoque em nível crítico (quantidade <= 3). | PASSED |
| CT-BACK-007 | database/produtos.py | Integridade de Dados | Garantir a ausência de registros com preço ou quantidade com valores negativos. | PASSED |
| CT-BACK-008 | database/caixa.py | Teste de Infraestrutura | Verificar a acessibilidade e a consulta operacional na tabela de caixa. | PASSED |
| CT-BACK-009 | database/caixa.py | Validação de Domínio | Garantir que os registros da tabela caixa contenham apenas os status Aberto ou Fechado. | PASSED |
| CT-BACK-010 | database/auditoria.py | Rastreabilidade / Auditoria | Verificar se a tabela logs_auditoria está disponível para gravação de eventos de sistema. | PASSED |
| CT-BACK-011 | database/caixa.py | Cobertura de Instrução | Execução direta da função Python obter_caixa_atual() sem lançar exceções. | PASSED |
| CT-BACK-012 | database/produtos.py | Cobertura de Instrução | Execução direta da função Python listar_produtos() retornando os dados da base. | PASSED |
| CT-BACK-013 | database/produtos.py | Cobertura de Instrução | Execução direta da função Python obter_metricas_estoque() validando dicionário de métricas. | PASSED |

============================ test session starts =============================
platform linux -- Python 3.12.3, pytest-9.1.1, pluggy-1.7.0 -- .venv/bin/python
plugins: cov-7.1.0
collected 13 items                                                                                  

../StockFlow-QA-Portfolio/03-automacao-pytest-playwright/testes_vendas_backend.py::test_conexao_banco_dados PASSED [  7%]
../StockFlow-QA-Portfolio/03-automacao-pytest-playwright/testes_vendas_backend.py::test_impedir_venda_quantidade_zero_ou_negativa PASSED [ 15%]
../StockFlow-QA-Portfolio/03-automacao-pytest-playwright/testes_vendas_backend.py::test_verificar_rollback_em_item_inexistente PASSED [ 23%]
../StockFlow-QA-Portfolio/03-automacao-pytest-playwright/testes_vendas_backend.py::test_validar_autenticacao_e_hash_senha PASSED [ 30%]
../StockFlow-QA-Portfolio/03-automacao-pytest-playwright/testes_vendas_backend.py::test_validar_distincao_cargos_rbac PASSED [ 38%]
../StockFlow-QA-Portfolio/03-automacao-pytest-playwright/testes_vendas_backend.py::test_verificar_alerta_estoque_critico PASSED [ 46%]
../StockFlow-QA-Portfolio/03-automacao-pytest-playwright/testes_vendas_backend.py::test_validar_integridade_valores_produtos PASSED [ 53%]
../StockFlow-QA-Portfolio/03-automacao-pytest-playwright/testes_vendas_backend.py::test_verificar_existencia_registro_caixa PASSED [ 61%]
../StockFlow-QA-Portfolio/03-automacao-pytest-playwright/testes_vendas_backend.py::test_validar_status_caixa_invalido PASSED [ 69%]
../StockFlow-QA-Portfolio/03-automacao-pytest-playwright/testes_vendas_backend.py::test_validar_presenca_logs_auditoria PASSED [ 76%]
../StockFlow-QA-Portfolio/03-automacao-pytest-playwright/testes_vendas_backend.py::test_execucao_funcao_obter_caixa_atual PASSED [ 84%]
../StockFlow-QA-Portfolio/03-automacao-pytest-playwright/testes_vendas_backend.py::test_execucao_funcao_listar_produtos PASSED [ 92%]
../StockFlow-QA-Portfolio/03-automacao-pytest-playwright/testes_vendas_backend.py::test_execucao_funcao_obter_metricas_estoque PASSED [100%]

========================================== tests coverage ===========================================
Name                     Stmts   Miss  Cover   Missing
------------------------------------------------------
database/__init__.py         0      0   100%
database/auditoria.py       30     30     0%   1-42
database/caixa.py           83     68    18%   9, 16-18, 22-37, 41-98, 102-132
database/clientes.py        44     44     0%   1-53
database/connection.py      36     29    19%   15-17, 21-160
database/produtos.py        92     63    32%   5-20, 26, 30-37, 45-47, 51-63, 67-83, 86-98, 104, 119-121
database/seed.py            27     27     0%   1-69
database/usuarios.py        79     79     0%   1-109
database/vendas.py          71     45    37%   13, 17, 33-34, 38-68, 79-108, 112-140
------------------------------------------------------
TOTAL                      462    385    17%
======================================== 13 passed in 0.85s =========================================