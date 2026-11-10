# Relatório de Defeito: BUG-005

**Título:** Dependência de estado do caixa e renderização condicional dos botões do PDV  
**Projeto:** StockFlow QA Portfolio  
**Módulo:** Ponto de Venda / PDV (`/vendas`)  
**Relatado por:** Igor (QA Engineer)  
**Data de Identificação:** 10/11/2026  
**Severidade:** Alta  
**Prioridade:** Alta  
**Status:** Fechado (Resolvido com sincronismo de estado e Explicit Waits)  

---

## 1. Descrição do Problema
Durante a execução do teste `test_realizar_venda_pdv_sucesso`, a suíte falhava com a exceção `selenium.common.exceptions.TimeoutException`. O Selenium não encontrava o botão de submissão de itens nem o botão de finalização da venda, pois a interface Jinja2 omitia a renderização desses elementos HTML quando o caixa do sistema estava no estado Fechado ou quando o carrinho de compras estava vazio (`{% if carrinho %}`).

---

## 2. Passos para Reproduzir
1. Autenticar no sistema com usuário Vendedor.
2. Navegar para a rota `/vendas` garantindo que o caixa esteja Fechado na base de dados.
3. Tentar interagir diretamente com o dropdown de produtos ou clicar no botão de finalizar venda sem preencher o fundo inicial de caixa e sem inserir itens no carrinho.
4. Observar a ausência dos elementos no DOM da página.

---

## 3. Resultado Esperado
O script de automação E2E deve verificar dinamicamente o estado da sessão (Caixa Aberto/Fechado), preencher o valor inicial de caixa caso necessário e aguardar a renderização síncrona dos elementos do carrinho antes de disparar a submissão final.

---

## 4. Resultado Atual no HTML
Os botões de adicionar ao carrinho e finalizar venda não existiam na árvore DOM até a execução das etapas prévias:
```html
<!-- Renderizado apenas se caixa aberto -->
{% if caixa %}
  <!-- Renderizado apenas se carrinho não vazio -->
  {% if carrinho %}
    <button type="submit" class="btn btn-success">Finalizar Venda</button>
  {% endif %}
{% endif %}