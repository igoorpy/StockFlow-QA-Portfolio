from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def navegar(self, url):
        self.driver.get(url)

    def encontrar_elemento(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def clicar(self, locator):
        elemento = self.wait.until(EC.element_to_be_clickable(locator))
        elemento.click()

    def digitar(self, locator, texto):
        elemento = self.encontrar_elemento(locator)
        elemento.clear()
        elemento.send_keys(texto)

    def obter_texto(self, locator):
        return self.encontrar_elemento(locator).text

    def aguardar_mudanca_de_url(self, url_antiga):
        """Aguarda a conclusão do redirecionamento da página."""
        self.wait.until(EC.url_changes(url_antiga))