# Automação de Testes de Componente e Integridade de Backend

Este repositório contém a suíte de testes automatizados de nível de componente e integração de banco de dados para o sistema StockFlow, desenvolvida na linguagem Python com o framework Pytest.

---

## Escopo dos Testes de Backend (Conformidade ISTQB CTFL v4.0)

A suíte abrange a validação direta de regras de negócio, controle de acesso e integridade de transações relacionais no PostgreSQL, em conformidade com as diretrizes de testes de componente e técnicas de caixa-branca da norma ISTQB CTFL v4.0.

| ID do Teste | Módulo / Função Alvo | Técnica Aplicada | Objetivo do Teste | Status |
| :--- | :--- | :--- | :--- | :---: |
| CT-BACK-001 | database/connection.py | Teste de Infraestrutura | Validar se a conexão com o banco de dados PostgreSQL está operacional. | PASSED |
| CT-BACK-002 | database/vendas.py | Teste Caixa-Branca / Regra de Negócio | Garantir que a função finalizar_venda_multi_item rejeita itens com quantidade menor ou igual a zero. | PASSED |
| CT-BACK-003 | database/vendas.py | Integridade Transacional (ACID) | Validar o procedimento de ROLLBACK completo ao tentar processar venda com item inexistente. | PASSED |
| CT-BACK-004 | database/usuarios.py | Segurança / Criptografia | Validar a equivalência de hash PBKDF2/Werkzeug para autenticação de usuários. | PASSED |
| CT-BACK-005 | database/usuarios.py | Controle de Acesso (RBAC) | Confirmar que o perfil vendedor não possui privilégios de administrador na base de dados. | PASSED |
| CT-BACK-006 | database/produtos.py | Regra de Negócio / Filtro | Validar a identificação de produtos com estoque em nível crítico (quantidade menor ou igual a 3). | PASSED |
| CT-BACK-007 | database/produtos.py | Integridade de Dados | Garantir a ausência de registros com preço ou quantidade com valores negativos. | PASSED |
| CT-BACK-008 | database/caixa.py | Teste de Infraestrutura | Verificar a acessibilidade e a consulta operacional na tabela de caixa. | PASSED |
| CT-BACK-009 | database/caixa.py | Validação de Domínio | Garantir que os registros da tabela caixa contenham apenas os status Aberto ou Fechado. | PASSED |
| CT-BACK-010 | database/auditoria.py | Rastreabilidade / Auditoria | Verificar se a tabela logs_auditoria está disponível para gravação de eventos de sistema. | PASSED |

---

======================================== test session starts ========================================
platform linux -- Python 3.12.3, pytest-9.1.1, pluggy-1.7.0 -- .venv/bin/python
rootdir: /home/igor/Documentos/Projetos-e-Faculdade/Python - Projetos
collected 10 items                                                                                  

../StockFlow-QA-Portfolio/03-automacao-pytest-playwright/testes_vendas_backend.py::test_conexao_banco_dados PASSED [ 10%]
../StockFlow-QA-Portfolio/03-automacao-pytest-playwright/testes_vendas_backend.py::test_impedir_venda_quantidade_zero_ou_negativa PASSED [ 20%]
../StockFlow-QA-Portfolio/03-automacao-pytest-playwright/testes_vendas_backend.py::test_verificar_rollback_em_item_inexistente PASSED [ 30%]
../StockFlow-QA-Portfolio/03-automacao-pytest-playwright/testes_vendas_backend.py::test_validar_autenticacao_e_hash_senha PASSED [ 40%]
../StockFlow-QA-Portfolio/03-automacao-pytest-playwright/testes_vendas_backend.py::test_validar_distincao_cargos_rbac PASSED [ 50%]
../StockFlow-QA-Portfolio/03-automacao-pytest-playwright/testes_vendas_backend.py::test_verificar_alerta_estoque_critico PASSED [ 60%]
../StockFlow-QA-Portfolio/03-automacao-pytest-playwright/testes_vendas_backend.py::test_validar_integridade_valores_produtos PASSED [ 70%]
../StockFlow-QA-Portfolio/03-automacao-pytest-playwright/testes_vendas_backend.py::test_verificar_existencia_registro_caixa PASSED [ 80%]
../StockFlow-QA-Portfolio/03-automacao-pytest-playwright/testes_vendas_backend.py::test_validar_status_caixa_invalido PASSED [ 90%]
../StockFlow-QA-Portfolio/03-automacao-pytest-playwright/testes_vendas_backend.py::test_validar_presenca_logs_auditoria PASSED [100%]

=======================10 passed in 0.53s ===========================