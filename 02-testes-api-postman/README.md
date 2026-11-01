## 🛠️ Refatoração de Contrato e Negociação de Conteúdo (HTTP / JSON)

Durante a fase inicial de automação da rota `/login`, identificou-se que o backend retornava documento HTML (`text/html`) em vez do contrato JSON negociado via cabeçalho `Accept: application/json`.

### Ação de Engenharia de Qualidade Aplicada:
- **Diagnóstico:** A rota aceitava apenas entradas do tipo `request.form` (formulário Web), resultando em resposta HTML e falha na desserialização de testes de API no Postman.
- **Solução Implementada:** Inclusão da verificação `request.is_json` no controlador `pagina_login()` do Flask.
- **Resultado:** A rota passou a atender requisições de API REST retornando `jsonify()` com Status `200 OK` (ou `401 Unauthorized`), mantendo a compatibilidade com a interface gráfica do navegador.