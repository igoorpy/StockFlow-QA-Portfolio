# Testes Automatizados de API REST (Postman + Newman)

Esta pasta contém a suíte de testes automatizados para a camada de serviços (API REST) do sistema StockFlow, validando protocolo HTTP, contratos JSON, códigos de status, SLAs de tempo de resposta e regras de autorização/RBAC.


## Matriz de Casos de Teste de API (Conformidade ISTQB CTFL v4.0)

| ID do Teste | Endpoint | Método | Tipo | Objetivo / Regra de Negócio | Status Esperado | Status |
| :--- | :--- | :---: | :---: | :--- | :---: | :---: |
| CT-API-001 | `/login` | `POST` | Positivo | Validar autenticação do vendedor com credenciais válidas e retorno do contrato JSON. | `200 OK` | PASSED |
| CT-API-002 | `/login` | `POST` | Negativo | Validar rejeição de acesso com senha incorreta e retorno de código de não autorizado. | `401 Unauthorized` | PASSED |


## Refatoração de Contrato e Negociação de Conteúdo (HTTP / JSON)

Durante a fase inicial de automação da rota `/login`, identificou-se que o backend retornava documento HTML (`text/html`) em vez do contrato JSON negociado via cabeçalho `Accept: application/json`.

### Ação de Engenharia de Qualidade Aplicada:
- **Diagnóstico:** A rota aceitava apenas entradas do tipo `request.form` (formulário Web), resultando em resposta HTML e falha na desserialização de testes de API no Postman.
- **Solução Implementada:** Inclusão da verificação `request.is_json` no controlador `pagina_login()` do Flask.
- **Resultado:** A rota passou a atender requisições de API REST retornando `jsonify()` com Status `200 OK` (ou `401 Unauthorized`), mantendo a compatibilidade com a interface gráfica do navegador.