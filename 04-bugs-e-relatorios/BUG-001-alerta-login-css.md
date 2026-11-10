# Relatório de Defeito: BUG-001

**Título:** Divergência de classe CSS nos alertas visuais de erro na tela de Login  
**Projeto:** StockFlow QA Portfolio  
**Módulo:** Autenticação (`/login`)  
**Relatado por:** Igor (QA Engineer)  
**Severidade:** Média  
**Prioridade:** Média  
**Status:** Corrigido / Resolvido  

---

## Descrição do Problema
Durante a execução do caso de teste E2E `CT-E2E-002`, o Selenium apresentou estouro de tempo limite (*TimeoutException*). A investigação indicou que o elemento visual de alerta na página `login.html` utilizava a classe `.alert-error`, enquanto a automação buscava pelo padrão `.alert-danger`.

---

## Passos para Reproduzir
1. Navegar para `http://localhost:5000/login`.
2. Digitar o usuário `carlos.vendedor`.
3. Inserir a senha incorreta `senha_errada`.
4. Clicar no botão **Entrar no Sistema**.
5. Inspecionar o elemento de erro renderizado na página.

---

## Resultado Esperado
O alerta de mensagem incorreta deve possuir classe CSS semântica padronizada (`alert-danger`).

---

## ❌ Resultado Atual
O elemento HTML utiliza a classe personalizada `alert-error`:
```html
<div class="alert-error">
     Usuário ou senha inválidos
</div>