import pytest
from pages.login_page import LoginPage
from pages.pdv_page import PDVPage

def test_realizar_venda_pdv_sucesso(driver):
    """CT-E2E-004: Validar fluxo completo do PDV (abrir caixa, adicionar item ao carrinho e finalizar venda)."""
    # 1. Autenticação com perfil Vendedor
    login_page = LoginPage(driver)
    login_page.carregar()
    login_page.realizar_login("carlos.vendedor", "123456")
    login_page.aguardar_login_sucesso()

    # 2. Navegação para o PDV / Vendas
    pdv_page = PDVPage(driver)
    pdv_page.carregar()

    # 3. Execução sequencial das etapas do PDV
    pdv_page.garantir_caixa_aberto(valor_inicial="100.00")
    pdv_page.adicionar_item_carrinho(quantidade="2")
    pdv_page.finalizar_venda()

    # 4. Asserção do fluxo
    assert "vendas" in driver.current_url.lower() or driver.current_url.rstrip("/") == "http://localhost:5000"