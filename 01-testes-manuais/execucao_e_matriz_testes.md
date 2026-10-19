# Registro de Execução e Matriz de Cobertura de Testes Manuais

* Projeto: StockFlow
* Ciclo de Testes: Ciclo 01 - Execução Inicial do Módulo PDV, Autenticação e Caixa
* Autor: Igor 
* Ambiente: Localhost (Linux Mint / Docker Compose - PostgreSQL 15)

---

## Resumo do Ciclo de Execução

| Módulo | Casos Planejados | Executados | Aprovados (PASS) | Reprovados (FAIL) | Bloqueados |
| :--- | :---: | :---: | :---: | :---: | :---: |
| PDV / Estoque | 3 | 3 | 3 | 0 | 0 |
| Login / RBAC | 4 | 4 | 3 | 1 | 0 |
| Regras do Caixa | 4 | 4 | 4 | 0 | 0 |
| **Total** | **11** | **11** | **10** | **1** | **0** |

---

## Detalhamento da Execução por Caso de Teste

### Módulo: PDV e Estoque
* **CT-PDV-001:** Venda com estoque suficiente -> **PASS**
* **CT-PDV-002:** Impedir venda acima do estoque -> **PASS**
* **CT-PDV-003:** Análise do Valor Limite (Estoque Zera) -> **PASS**

### Módulo: Autenticação e Segurança (RBAC)
* **CT-LOG-001:** Login válido perfil Vendedor -> **PASS**
* **CT-LOG-002:** Rejeição de senha incorreta -> **PASS**
* **CT-LOG-003:** Bloqueio de rota `/auditoria` para perfil Vendedor -> **FAIL**
* **CT-LOG-004:** Encerramento de sessão (Logout) -> **PASS**

### Módulo: Tabela de Decisão do Caixa
* **CT-TAB-001 (Regra 1):** Venda com Caixa Aberto, Estoque e Autenticação -> **PASS**
* **CT-TAB-002 (Regra 2):** Venda com Caixa Fechado -> **PASS**
* **CT-TAB-003 (Regra 3):** Venda sem Estoque -> **PASS**
* **CT-TAB-004 (Regra 4):** Venda sem Sessão (Usuário Anônimo) -> **PASS**