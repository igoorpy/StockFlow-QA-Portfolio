# Tabela de Decisão - Regras do Ponto de Venda e Estado do Caixa

* Projeto: StockFlow
* Módulo: Processamento de Vendas e Estado do Caixa
* Autor: Igor 
* Conformidade: ISTQB CTFL v4.0 (Tabela de Decisão)

---

## Contexto Lógico

Para que uma venda seja registrada, o sistema avalia três condições:
1. Condição 1 (C1): O turno de Caixa está ABERTO?
2. Condição 2 (C2): A quantidade solicitada está DISPONÍVEL no estoque?
3. Condição 3 (C3): O operador possui SESSÃO ATIVA?

---

## Matriz da Tabela de Decisão

| Condições / Ações | Regra 1 | Regra 2 | Regra 3 | Regra 4 |
| :--- | :---: | :---: | :---: | :---: |
| C1: Caixa Aberto? | V | F | V | V |
| C2: Estoque Suficiente? | V | V | F | V |
| C3: Usuário Autenticado? | V | V | V | F |
| A1: Processar Venda e Baixar Estoque | X | | | |
| A2: Exibir erro "Caixa Fechado" | | X | | |
| A3: Exibir erro "Estoque Insuficiente" | | | X | |
| A4: Redirecionar para /login | | | | X |

*Legenda: V = Verdadeiro, F = Falso, X = Ação Executada.*

---

## Cenários de Teste Derivados

### CT-TAB-001: Regra 1 - Venda Autorizada
* Entrada: Caixa Aberto = V | Estoque = V | Usuário Autenticado = V
* Ação: Processar venda e atualizar saldo no PostgreSQL.

### CT-TAB-002: Regra 2 - Bloqueio por Caixa Fechado
* Entrada: Caixa Aberto = F | Estoque = V | Usuário Autenticado = V
* Ação: Exibir mensagem "Não é possível realizar vendas com o caixa fechado".

### CT-TAB-003: Regra 3 - Bloqueio por Estoque Insuficiente
* Entrada: Caixa Aberto = V | Estoque = F | Usuário Autenticado = V
* Ação: Exibir mensagem "Quantidade solicitada indisponível no estoque".

### CT-TAB-004: Regra 4 - Bloqueio por Falta de Autenticação
* Entrada: Caixa Aberto = V | Estoque = V | Usuário Autenticado = F
* Ação: Redirecionar para a tela de login (/login).