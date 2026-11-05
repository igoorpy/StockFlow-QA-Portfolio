from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    CAMPO_USUARIO = (By.NAME, "usuario")
    CAMPO_SENHA = (By.NAME, "senha")
    BOTAO_ENTRAR = (By.CSS_SELECTOR, "button[type='submit']")
    MENSAGEM_ERRO = (By.CLASS_NAME, "alert-error")  # Seletor corrigido conforme login.html

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "http://localhost:5000/login"

    def carregar(self):
        self.navegar(self.url)

    def realizar_login(self, usuario, senha):
        self.digitar(self.CAMPO_USUARIO, usuario)
        self.digitar(self.CAMPO_SENHA, senha)
        self.clicar(self.BOTAO_ENTRAR)

    def obter_mensagem_erro(self):
        return self.obter_texto(self.MENSAGEM_ERRO)

    def aguardar_login_sucesso(self):
        self.aguardar_mudanca_de_url(self.url)