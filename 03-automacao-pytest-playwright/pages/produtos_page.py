from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProdutosPage(BasePage):
    # Seletores da interface gráfica de produtos e estoque
    TABELA_PRODUTOS = (By.CSS_SELECTOR, "table")
    LINHAS_PRODUTOS = (By.CSS_SELECTOR, "table tbody tr")
    ALERTAS_ESTOQUE_CRITICO = (By.CSS_SELECTOR, ".badge-danger, .badge-warning, .alert-warning")
    TITULO_PAGINA = (By.TAG_NAME, "h1")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "http://localhost:5000/produtos"

    def carregar(self):
        self.navegar(self.url)

    def obter_total_produtos_listados(self):
        """Retorna a quantidade de itens presentes na tabela de estoque."""
        elementos = self.driver.find_elements(*self.LINHAS_PRODUTOS)
        return len(elementos)

    def verificar_presenca_tabela(self):
        """Confirma se a estrutura da tabela está visível na página."""
        return len(self.driver.find_elements(*self.TABELA_PRODUTOS)) > 0