# Relatório de Defeito: BUG-002

**Título:** Ausência de atributo de identificação único (`id`) no botão de finalizar venda  
**Projeto:** StockFlow QA Portfolio  
**Módulo:** Ponto de Venda / PDV (`/`)  
**Relatado por:** Igor (QA Engineer)  
**Data de Identificação:** 10/11/2026  
**Severidade:** Alta  
**Prioridade:** Alta  
**Status:** Fechado (Resolvido via locator XPath resiliente)  

---

## 1. Descrição do Problema
No teste E2E `CT-E2E-004` (realização de venda no PDV), o script Selenium falhou com `TimeoutException` ao tentar acionar o botão de submissão da venda. O Page Object procurava um elemento com `#btn-finalizar-venda`, mas o HTML do formulário não possuía o atributo `id`, dependendo apenas de estilos CSS compartilhados.

---

## 2. Passos para Reproduzir
1. Autenticar-se no sistema com perfil Vendedor.
2. Navegar para a tela principal do PDV (`http://localhost:5000/`).
3. Selecionar um produto e definir a quantidade.
4. Tentar localizar o elemento via console de inspeção do navegador utilizando o comando `document.getElementById('btn-finalizar-venda')`.

---

## 3. Resultado Esperado
Elementos críticos da interface gráfica de alta relevância de negócio (como finalização de checkout) devem possuir atributos `id` ou `data-testid` estáticos para suportar acessibilidade e automação de testes (Testabilidade / *Testability* - ISTQB CTFL v4.0 Capítulo 2).

---

## 4. Resultado Atual no HTML
```html
<button type="submit" class="btn btn-success" style="...">
    Finalizar Venda (Emitir Nota/PDF)
</button>