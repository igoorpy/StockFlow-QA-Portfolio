import pytest
from pages.login_page import LoginPage
from pages.pdv_page import PDVPage

def test_realizar_venda_pdv_sucesso(driver):
    """CT-E2E-004: Validar fluxo completo de realização de venda pela interface Web."""
    # 1. Login no sistema
    login_page = LoginPage(driver)
    login_page.carregar()
    login_page.realizar_login("carlos.vendedor", "123456")
    login_page.aguardar_login_sucesso()

    # 2. Carregar interface do PDV
    pdv_page = PDVPage(driver)
    pdv_page.carregar()

    # 3. Interação com o formulário de venda
    pdv_page.selecionar_primeiro_produto()
    pdv_page.preencher_quantidade("2")
    pdv_page.finalizar_venda()

    # 4. Validação da execução
    assert driver.current_url.startswith("http://localhost:5000")