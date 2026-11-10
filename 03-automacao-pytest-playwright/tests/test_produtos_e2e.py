import pytest
from pages.login_page import LoginPage
from pages.produtos_page import ProdutosPage

def test_visualizar_listagem_produtos_admin(driver):
    """CT-E2E-005: Validar acesso e carregamento da consulta de produtos pelo perfil Administrador."""
    # 1. Autenticação com credenciais de Administrador
    login_page = LoginPage(driver)
    login_page.carregar()
    login_page.realizar_login("admin", "admin123")
    login_page.aguardar_login_sucesso()

    # 2. Navegação para o catálogo de produtos
    produtos_page = ProdutosPage(driver)
    produtos_page.carregar()

    # 3. Validações da interface
    assert produtos_page.verificar_presenca_tabela(), "A tabela de produtos não foi carregada no DOM."
    assert produtos_page.obter_total_produtos_listados() > 0, "A tabela de produtos está vazia."