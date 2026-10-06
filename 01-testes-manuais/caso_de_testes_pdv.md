# Suíte de Casos de Teste - Módulo Ponto de Venda (PDV) e Estoque

* Projeto: StockFlow
* Aplicação: Gestão de Estoque e PDV (Flask/PostgreSQL)
* Autor: Igor (Analista de QA)
* Conformidade: ISTQB CTFL v4.0 (Técnicas de Caixa-Preta)

## Contexto e Regras de Negócio (Base de Teste)

* RN01 - Baixa de Estoque: Ao registrar uma venda, a quantidade vendida deve ser subtraída do saldo do produto no PostgreSQL.
* RN02 - Impeditivo de Saldo Insuficiente: Não é permitido realizar venda com quantidade superior ao estoque atual.
* RN03 - Identificação do Operador: Toda venda registrada deve estar associada ao usuário/vendedor logado na sessão.


## Casos de Teste Manuais

### CT-PDV-001: Venda de produto com estoque suficiente (Cenário Positivo)

* Técnica CTFL: Partição de Equivalência (Classe de Entrada Válida)
* Severidade: Alta

* Pré-condições:
  1. Aplicação StockFlow rodando em ambiente local.
  2. Usuário autenticado com o login "carlos.vendedor".
  3. Caixa aberto no sistema.
  4. Produto "Notebook Dell Inspiron 15" cadastrado com saldo de 12 unidades.
  5. Cliente "Lucas Mendes" cadastrado na base de dados.

* Passos de Execução:
  1. Acessar o menu "Vendas / PDV".
  2. Selecionar o cliente "Lucas Mendes".
  3. Adicionar o produto "Notebook Dell Inspiron 15" ao carrinho.
  4. Informar a quantidade de 2 unidades.
  5. Selecionar a forma de pagamento "PIX".
  6. Confirmar o processamento da venda.

* Resultado Esperado:
  * A venda deve ser processada e finalizada com sucesso.
  * O sistema deve realizar a transação no banco de dados.
  * O saldo do produto "Notebook Dell Inspiron 15" na tela de produtos/estoque deve ser reduzido para 10 unidades (12 - 2).


### CT-PDV-002: Impedir venda com quantidade maior do que o estoque disponível (Cenário de Exceção)

* Técnica CTFL: Partição de Equivalência (Classe de Entrada Inválida)
* Severidade: Crítica

* Pré-condições:
  1. Usuário autenticado na aplicação.
  2. Caixa aberto.
  3. Produto "Cadeira Gamer ThunderX3" cadastrado com saldo de 5 unidades.

* Passos de Execução:
  1. Acessar o menu "Vendas / PDV".
  2. Selecionar o produto "Cadeira Gamer ThunderX3".
  3. Digitar no campo de quantidade o valor 6 unidades.
  4. Tentar finalizar a venda.

* Resultado Esperado:
  * O sistema deve bloquear a operação e impedir o registro no banco de dados.
  * Deve ser exibida uma mensagem de alerta informando a indisponibilidade de estoque.
  * O saldo do produto "Cadeira Gamer ThunderX3" deve permanecer em 5 unidades.


### CT-PDV-003: Validação de limite máximo de estoque disponível (Análise do Valor Limite)

* Técnica CTFL: Análise do Valor Limite (Fronteira Exata N = Saldo Atual)
* Severidade: Alta

* Pré-condições:
  1. Usuário autenticado com o login "mariana.vendedora".
  2. Produto "Smartphone Samsung Galaxy S23" com saldo exato de 8 unidades.

* Passos de Execução:
  1. Acessar o PDV.
  2. Selecionar o produto "Smartphone Samsung Galaxy S23".
  3. Informar a quantidade de exatamente 8 unidades (igual ao limite em estoque).
  4. Processar a venda.

* Resultado Esperado:
  * A venda deve ser concluída com sucesso.
  * O estoque do produto "Smartphone Samsung Galaxy S23" deve ser atualizado para 0 unidades.
  * O produto deve continuar cadastrado, porém com indicação de saldo zerado.