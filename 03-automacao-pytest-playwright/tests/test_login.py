import pytest
from pages.login_page import LoginPage

def test_login_vendedor_sucesso(driver):
    """CT-E2E-001: Validar login bem-sucedido de perfil Vendedor."""
    login_page = LoginPage(driver)
    login_page.carregar()
    
    login_page.realizar_login("carlos.vendedor", "123456")
    login_page.aguardar_login_sucesso()
    
    assert "login" not in driver.current_url.lower()

def test_login_credenciais_invalidas(driver):
    """CT-E2E-002: Validar mensagem de erro ao informar senha incorreta."""
    login_page = LoginPage(driver)
    login_page.carregar()
    
    login_page.realizar_login("carlos.vendedor", "senha_incorreta")
    
    mensagem_erro = login_page.obter_mensagem_erro()
    assert len(mensagem_erro) > 0

def test_login_admin_sucesso(driver):
    """CT-E2E-003: Validar login bem-sucedido de perfil Administrador."""
    login_page = LoginPage(driver)
    login_page.carregar()
    
    login_page.realizar_login("admin", "admin123")
    login_page.aguardar_login_sucesso()
    
    assert "login" not in driver.current_url.lower()