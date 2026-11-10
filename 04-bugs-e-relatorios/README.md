# Gestão de Defeitos e Relatórios de Bugs (ISTQB CTFL v4.0)

Este diretório contém a documentação formal dos defeitos identificados, triados e corrigidos durante o ciclo de vida dos testes (unidade, API e automação Web E2E) no sistema **StockFlow**.

---

## Matriz Consolidada de Defeitos

| ID | Título do Defeito | Módulo | Severidade | Prioridade | Origem / Teste | Status |
| :--- | :--- | :--- | :---: | :---: | :--- | :---: |
| **BUG-001** | Divergência de classe CSS nos alertas de erro | Autenticação (`/login`) | Média | Média | Automação (`CT-E2E-002`) | **FECHADO** |
| **BUG-002** | Ausência de ID estático no botão do PDV | Vendas (`/`) | Alta | Alta | Automação (`CT-E2E-004`) | **FECHADO** |
| **BUG-003** | Asserção pré-matura por Condição de Corrida | Navegação / HTTP | Média | Alta | Sincronismo Selenium | **FECHADO** |
| **BUG-004** | Incompatibilidade de versão no ChromeDriver | Infra / Driver | Alta | Alta | Execução Linux / Brave | **FECHADO** |
| **BUG-005** | Dependência de estado do caixa e renderização condicional | Vendas (`/vendas`) | Alta | Alta | Automação (`CT-E2E-004`) | **FECHADO** |
---

## Ciclo de Vida de Defeitos Aplicado

Os relatórios seguem a estrutura padrão recomendada pelo ISTQB:
1. **Identificação:** Captura do erro via execução manual/automatizada.
2. **Triagem & Causa-Raiz:** Análise do código-fonte (Flask/HTML) e dos logs do terminal.
3. **Reporte Formal:** Elaboração do relatório de bug com passos reprodutíveis.
4. **Resolução & Reteste:** Validação da correção com asserções automatizadas no Pytest.