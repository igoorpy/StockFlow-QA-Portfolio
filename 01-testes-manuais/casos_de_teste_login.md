# Suíte de Casos de Teste - Módulo Autenticação e Segurança (RBAC)

* Projeto: StockFlow
* Aplicação: Gestão de Estoque e PDV (Flask/PostgreSQL)
* Autor: Igor 
* Conformidade: ISTQB CTFL v4.0 (Técnica de Transição de Estado e RBAC)

---

## Contexto e Regras de Negócio (Base de Teste)

* RN04 - Autenticação Obrigatória: Nenhuma rota interna da aplicação deve ser acessível sem sessão ativa.
* RN05 - Hash de Senha Seguro: Senhas devem ser validadas via hash (Werkzeug PBKDF2).
* RN06 - Controle de Acesso Baseado em Função (RBAC):
  * Perfil Vendedor: Acesso restrito ao PDV, Consulta de Produtos, Caixa e Clientes.
  * Perfil Admin: Acesso total ao sistema, incluindo a rota de Auditoria (/auditoria).

---

## Casos de Teste Manuais

### CT-LOG-001: Autenticação válida com perfil Vendedor

* Técnica Aplicada: Transição de Estado (Não Autenticado -> Autenticado)
* Severidade: Crítica
* Pré-condições:
  1. Usuário "carlos.vendedor" cadastrado no banco PostgreSQL.
* Passos de Execução:
  1. Navegar até a URL de login (/login).
  2. Informar o usuário "carlos.vendedor".
  3. Informar a senha "123456".
  4. Clicar em "Entrar".
* Resultado Esperado:
  * Autenticação realizada com sucesso.
  * Redirecionamento para o Dashboard/PDV.
  * Sessão aberta com o usuário_id e cargo "vendedor".

---

### CT-LOG-002: Rejeição de login com senha incorreta

* Técnica Aplicada: Transição de Estado (Permanência em Não Autenticado)
* Severidade: Alta
* Pré-condições:
  1. Usuário "mariana.vendedora" cadastrado na base de dados.
* Passos de Execução:
  1. Acessar a página de login (/login).
  2. Digitar o usuário "mariana.vendedora".
  3. Digitar a senha incorreta "senha_invalida_999".
  4. Clicar em "Entrar".
* Resultado Esperado:
  * Autenticação recusada.
  * Exibição da mensagem de erro "Usuário ou senha inválidos".
  * Nenhuma sessão gerada.

---

### CT-LOG-003: Bloqueio de acesso a rota restrita de Admin por Vendedor (RBAC)

* Técnica Aplicada: Controle de Acesso / RBAC
* Severidade: Alta
* Pré-condições:
  1. Usuário "carlos.vendedor" autenticado na aplicação.
* Passos de Execução:
  1. Tentar acessar diretamente no navegador a URL de auditoria (/auditoria).
* Resultado Esperado:
  * O decorator @admin_required deve interceptar a requisição.
  * Acesso negado e redirecionamento para página inicial/alerta de permissão insuficiente.

---

### CT-LOG-004: Encerramento de sessão (Logout) e invalidação de histórico

* Técnica Aplicada: Transição de Estado (Autenticado -> Não Autenticado)
* Severidade: Média
* Pré-condições:
  1. Usuário autenticado na aplicação.
* Passos de Execução:
  1. Clicar no botão "Sair" (/logout).
  2. Tentar acessar o menu de vendas (/vendas) utilizando o botão de voltar do navegador.
* Resultado Esperado:
  * Sessão encerrada no backend.
  * Acesso bloqueado, redirecionando automaticamente para a tela de login (/login).