import shutil
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--headless")  # Execução em segundo plano
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Localiza o executável do Brave no Linux (/usr/bin/brave-browser)
    caminho_brave = shutil.which("brave-browser") or shutil.which("brave") or "/usr/bin/brave-browser"
    options.binary_location = caminho_brave

    # O Selenium Manager detecta a versão do Brave (v153) e baixa o driver correto
    service = Service()
    browser = webdriver.Chrome(service=service, options=options)
    
    yield browser

    browser.quit()