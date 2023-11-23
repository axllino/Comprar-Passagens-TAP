from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.support.select import Select
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as condicao_esperada


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1200,700', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)
    chrome_options.add_experimental_option('prefs', {
        # Auterar o local padrão do download de arquivos
        'download.default_directory': 'C:\\Users\\lino\\Desktop\\Comprar Passagens TAP\\Comprar-Passagens-TAP\\download',
        # Notificar o google chrome sobre essa auteração
        'download.directory_upgrade': True,
        # Desabilitar a confirmação de download
        'download.prompt_for_download': False,
        # Desabilitar notificações
        'profile.default_content_setting_values.notifications': 2,
        # Permitir multiplos download
        'profile.default_content_setting_values.automatic_downloads': 1,
    })
    # Inicializando o webdriver
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    wait = WebDriverWait(
        driver,
        10,
        poll_frequency=1,
        ignored_exceptions=[
            NoSuchCookieException,
            ElementNotVisibleException,
            ElementNotSelectableException
        ]
    )

    return driver, wait


driver, wait = iniciar_driver()


def digitar_naturalmente(texto, elemento):
    for letra in texto:
        elemento.send_keys(letra)
        sleep(random.randint(1, 5)/30)


# navegar até o site
driver.get('https://www.flytap.com/pt-pt/')
sleep(5)

# botao_windows = driver.find_element(By.ID, 'WindowsRadioButton')
permitir_cookies = driver.find_element(
    By.ID, "onetrust-accept-btn-handler")
sleep(3)
permitir_cookies.click()
sleep(2)

# popup_promocional = wait.until(condicao_esperada.visibility_of_element_located(
#   (By.XPATH, '//img[@alt="Registrieren"]')))
# sleep(2)
# popup_promocional.click()

primeira_opcao_promocao = wait.until(condicao_esperada.visibility_of_element_located(
    (By.XPATH, '//a[@data-ga-module-id="Cheap Flights Showcase Homepage"]')))

driver.execute_script(
    "arguments[0].scrollIntoView();", primeira_opcao_promocao)
sleep(3)
primeira_opcao_promocao.click()
sleep(5)
# botao_windows = driver.find_element(By.ID, 'WindowsRadioButton')

data_ida = wait.until(condicao_esperada.element_to_be_clickable(
    (By.XPATH, '//button[@class="month chart-item cheapest"]')))
driver.execute_script("arguments[0].scrollIntoView();", data_ida)
sleep(2)
data_ida.click()
sleep(2)


botao_reservar_agora = wait.until(condicao_esperada.element_to_be_clickable(
    (By.XPATH, '//span[@class="mask"]')))
driver.execute_script("arguments[0].scrollIntoView();", botao_reservar_agora)
sleep(2)
botao_reservar_agora.click()
sleep(2)

# Após clicar no botão abrir_janela
janelas = driver.window_handles

# Trocar para a última aba aberta
driver.switch_to.window(janelas[-1])


tarifa_economica = wait.until(condicao_esperada.element_to_be_clickable(
    (By.XPATH, '//div[@class="flight__cabin-left"]/p[0]')))
driver.execute_script("arguments[0].scrollIntoView();", tarifa_economica)
sleep(2)
tarifa_economica.click()
sleep(2)

botao_continuar_basic = wait.until(condicao_esperada.element_to_be_clickable((
    By.XPATH, '//button[@class="button button-accent button--icon button--xtrasmall"]/p[0]')))
driver.execute_script("arguments[0].scrollIntoView();", botao_continuar_basic)
sleep(2)
botao_continuar_basic.click()
sleep(2)

concluir_reserva_agora = wait.until(condicao_esperada.element_to_be_clickable((
    By.XPATH, '//button[@aria-label="Concluir esta reserva agora"]')))
driver.execute_script("arguments[0].scrollIntoView();", concluir_reserva_agora)
sleep(2)
concluir_reserva_agora.click()
sleep(2)

prosseguir_sem_seguro = wait.until(condicao_esperada.element_to_be_clickable(
    (By.XPATH, '///button[@aria-label="Prosseguir para a página do pagamento sem qualquer seguro"]')))
driver.execute_script("arguments[0].scrollIntoView();", prosseguir_sem_seguro)
sleep(2)
prosseguir_sem_seguro.click()
sleep(2)

prosseguir_pagamento = wait.until(condicao_esperada.element_to_be_clickable(
    (By.XPATH, '//button[@aria-label="Prosseguir para a página do pagamento sem qualquer seguro"]')))
driver.execute_script("arguments[0].scrollIntoView();", prosseguir_pagamento)
sleep(2)
prosseguir_pagamento.click()
sleep(2)

login_no = wait.until(condicao_esperada.element_to_be_clickable(
    (By.XPATH, '//input[@id="login-no"]')))
driver.execute_script("arguments[0].scrollIntoView();", login_no)
sleep(2)
login_no.click()
sleep(2)

# //button[text()= Prosseguir como convidado ]

# driver.execute_script('arguments[0].click()', botao_radio)
# botao_radio.send_keys(Keys.DOWN)

input('Aperte uma tecla para fechar')
