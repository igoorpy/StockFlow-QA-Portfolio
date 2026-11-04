# Testes Automatizados de API REST (Postman + Newman CLI)

Esta pasta contém a suíte completa de testes automatizados para a camada de serviços (API REST) do sistema **StockFlow**, cobrindo validações de protocolo HTTP, contratos JSON, códigos de status, SLAs de tempo de resposta e regras de autorização/RBAC.

---

## Matriz Final de Casos de Teste (Conformidade ISTQB CTFL v4.0)

| ID do Teste | Endpoint | Método | Tipo | Objetivo / Regra de Negócio | Status Esperado | Status |
| :--- | :--- | :---: | :---: | :--- | :---: | :---: |
| CT-API-001 | `/login` | `POST` | Positivo | Validar autenticação do vendedor com credenciais válidas e retorno do contrato JSON. | `200 OK` | PASSED |
| CT-API-002 | `/login` | `POST` | Negativo | Validar rejeição de acesso com senha incorreta e retorno de código de não autorizado. | `401 Unauthorized` | PASSED |
| CT-API-001B | `/login` | `POST` | Positivo | Validar autenticação do administrador e geração de sessão cookie admin. | `200 OK` | PASSED |
| CT-API-003 | `/produtos` | `GET` | Positivo | Validar consulta do catálogo de produtos por perfil admin com retorno de Array JSON. | `200 OK` | PASSED |
| CT-API-004 | `/vendas` | `POST` | Positivo | Validar fechamento de pedido com envio de carrinho em formato JSON. | `200 OK` | PASSED |
| CT-API-005 | `/auditoria` | `GET` | Positivo | Validar consulta de logs de auditoria restritos ao perfil administrador. | `200 OK` | PASSED |

---

## Refatoração de Contrato e Negociação de Conteúdo (HTTP / JSON)

As rotas do backend Flask foram refatoradas para arquitetura **Dual-Interface** (suporte simultâneo a navegação Web HTML e chamadas de API REST JSON via `request.is_json` e cabeçalho `Accept: application/json`).

---

## Execução Automatizada via Linha de Comando (Newman CLI)

### Pré-requisitos:
- Node.js e NPM instalados
- Newman e reporter HTML instalados globalmente (`npm install -g newman newman-reporter-htmlextra`)
- Backend StockFlow rodando em `http://localhost:5000`

### Comando de Execução:
```bash
newman run StockFlow_Postman_Collection.json \
  -e StockFlow_Environment.json \
  --env-var "base_url=http://localhost:5000" \
  -r cli,htmlextra \
  --reporter-htmlextra-export ./relatorio-newman.html