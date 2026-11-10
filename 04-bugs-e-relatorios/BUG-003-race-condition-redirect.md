# Relatório de Defeito: BUG-003

**Título:** Falha de validação de URL por Condição de Corrida (*Race Condition*) pós-autenticação  
**Projeto:** StockFlow QA Portfolio  
**Módulo:** Navegação / Sessão HTTP  
**Relatado por:** Igor (QA Engineer)  
**Data de Identificação:** 10/11/2026  
**Severidade:** Média  
**Prioridade:** Alta  
**Status:** Fechado (Resolvido com Explicit Wait `EC.url_changes`)  

---

## 1. Descrição do Problema
Nos testes de login (`test_login.py`), a instrução `assert "login" not in driver.current_url.lower()` falhou lançando `AssertionError`. O Selenium efetuou o clique no botão de submit e avaliou a propriedade `driver.current_url` milissegundos depois, antes que a resposta HTTP 302/200 com a alteração de rota fosse processada pelo navegador.

---

## 2. Passos para Reproduzir
1. Executar o Selenium em ambiente de rápida instrução de código.
2. Preencher as credenciais e disparar o clique no botão de login.
3. Consultar a propriedade `driver.current_url` imediatamente na linha seguinte, sem aplicação de sincronização.

---

## 3. Resultado Esperado
O script de teste deve aguardar explicitamente a transição de rotas do navegador antes de avaliar asserções sobre o estado final da aplicação.

---

## 4. Causa-Raiz e Solução Aplicada
* **Causa-Raiz:** Assincronismo inerente entre a velocidade de execução do código Python e o ciclo de requisição/resposta do servidor Flask.
* **Solução:** Adicionado o método `aguardar_mudanca_de_url` na `BasePage` (`pages/base_page.py`), utilizando `WebDriverWait(driver, 10).until(EC.url_changes(url_antiga))`. Isso garante que a asserção só é executada após a conclusão do redirecionamento.