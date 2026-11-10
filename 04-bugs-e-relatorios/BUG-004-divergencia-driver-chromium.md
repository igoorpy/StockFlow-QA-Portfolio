# Relatório de Defeito: BUG-004

**Título:** Falha de inicialização de sessão por incompatibilidade de versão do ChromeDriver  
**Projeto:** StockFlow QA Portfolio  
**Módulo:** Infraestrutura de Testes / Driver Selenium  
**Relatado por:** Igor (QA Engineer)  
**Data de Identificação:** 10/11/2026  
**Severidade:** Alta  
**Prioridade:** Alta  
**Status:** Fechado (Resolvido com Selenium Manager nativo)  

---

## 1. Descrição do Problema
Ao iniciar a suíte no terminal Linux utilizando a biblioteca externa `webdriver-manager`, o teste falhou na fixture `driver` com a exceção `selenium.common.exceptions.SessionNotCreatedException`. A biblioteca realizou o download da versão 157 do ChromeDriver, enquanto o navegador **Brave Browser** instalado na máquina rodava o engine Chromium na versão 153.

---

## 2. Passos para Reproduzir
1. Instalar o `webdriver-manager` via pip.
2. Definir o caminho de binário do Brave Browser (`/usr/bin/brave-browser`).
3. Chamar `ChromeDriverManager().install()` em um ambiente com versão do navegador anterior à versão mais recente do Google Chrome.

---

## 3. Resultado Esperado
A automação deve parear dinamicamente a versão exata do binário do navegador Chromium instalado no sistema operacional com seu driver correspondente.

---

## 4. Causa-Raiz e Solução Aplicada
* **Causa-Raiz:** Conflito de versão promovido por gerenciador externo terceirizado.
* **Solução:** O `conftest.py` foi refatorado para utilizar o **Selenium Manager nativo (Selenium 4+)**, que inspeciona o executável do Brave em `/usr/bin/brave-browser`, identifica automaticamente a versão 153 e obtém o driver exato sem intervenção manual.