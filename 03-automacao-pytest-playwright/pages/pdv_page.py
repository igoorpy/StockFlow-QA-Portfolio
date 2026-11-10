from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class PDVPage(BasePage):
    # Locators vinculados diretamente às ações dos formulários HTML
    CAMPO_VALOR_INICIAL = (By.NAME, "valor_inicial")
    BOTAO_ABRIR_CAIXA = (By.XPATH, "//form[@action='/caixa/abrir']//button")

    SELECT_PRODUTO = (By.NAME, "produto_id")
    CAMPO_QUANTIDADE = (By.NAME, "quantidade")
    BOTAO_ADICIONAR_CARRINHO = (By.XPATH, "//form[@action='/carrinho/adicionar']//button")

    BOTAO_FINALIZAR_VENDA = (By.XPATH, "//form[@action='/vendas/finalizar']//button")
    MENSAGEM_SUCESSO = (By.CLASS_NAME, "alert-success")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "http://localhost:5000/vendas"

    def carregar(self):
        self.navegar(self.url)

    def garantir_caixa_aberto(self, valor_inicial="100.00"):
        """Verifica se o caixa está fechado, preenche o valor de fundo e abre o caixa."""
        inputs_caixa = self.driver.find_elements(*self.CAMPO_VALOR_INICIAL)
        if inputs_caixa:
            self.digitar(self.CAMPO_VALOR_INICIAL, valor_inicial)
            self.clicar(self.BOTAO_ABRIR_CAIXA)
            # Aguarda a atualização da página até que o campo de seleção de produto esteja visível
            self.wait.until(EC.visibility_of_element_located(self.SELECT_PRODUTO))

    def adicionar_item_carrinho(self, quantidade="2"):
        """Seleciona um produto disponível, define a quantidade e adiciona ao carrinho."""
        select_element = self.encontrar_elemento(self.SELECT_PRODUTO)
        select = Select(select_element)
        if len(select.options) > 1:
            select.select_by_index(1)
        elif len(select.options) == 1:
            select.select_by_index(0)

        self.digitar(self.CAMPO_QUANTIDADE, quantidade)
        self.clicar(self.BOTAO_ADICIONAR_CARRINHO)
        # Aguarda a renderização do botão de finalizar venda
        self.wait.until(EC.visibility_of_element_located(self.BOTAO_FINALIZAR_VENDA))

    def finalizar_venda(self):
        """Dispara a finalização da venda."""
        self.clicar(self.BOTAO_FINALIZAR_VENDA)