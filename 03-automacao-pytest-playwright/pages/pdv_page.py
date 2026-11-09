from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage

class PDVPage(BasePage):
    # Locators do formulário do PDV
    SELECT_PRODUTO = (By.NAME, "produto_id")
    CAMPO_QUANTIDADE = (By.NAME, "quantidade")
    BOTAO_FINALIZAR_VENDA = (By.XPATH, "//button[contains(., 'Finalizar') or contains(@class, 'btn-success')]")
    MENSAGEM_SUCESSO = (By.CLASS_NAME, "alert-success")

    def __init__(self, driver):
        super().__init__(driver)
        # Ajustado para a rota padrão do PDV no Flask
        self.url = "http://localhost:5000/"

    def carregar(self):
        self.navegar(self.url)

    def selecionar_primeiro_produto(self):
        """Seleciona a primeira opção válida do dropdown de produtos."""
        elementos_select = self.driver.find_elements(*self.SELECT_PRODUTO)
        if elementos_select:
            select = Select(elementos_select[0])
            if len(select.options) > 1:
                select.select_by_index(1)
            elif len(select.options) == 1:
                select.select_by_index(0)

    def preencher_quantidade(self, quantidade="1"):
        if self.driver.find_elements(*self.CAMPO_QUANTIDADE):
            self.digitar(self.CAMPO_QUANTIDADE, quantidade)

    def finalizar_venda(self):
        self.clicar(self.BOTAO_FINALIZAR_VENDA)