from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

urls = ['http://4usee.com/conta/E9E138/', 'http://conta2.4yousee.com.br' ]
USUARIO = '' 
SENHA = ''

data = []
for i, url in enumerate(urls, 1):
    if not 'http' in url or 'https' in url and url.startswith('4usee'):
        url = f'https://{url}'
    else:
        nome_cliente, email_cliente, telefone_cliente = '', '', ''

        driver = webdriver.Chrome(executable_path=r"C:\driver_chrome_selenium\chromedriver.exe")
        driver.get(url)
        time.sleep(2)
        try:
            # Fazendo Login
            usuario = driver.find_element_by_name('usr_log')
            usuario.send_keys(USUARIO)
            usuario.send_keys(Keys.ENTER)

            senha = driver.find_element_by_name('usr_sen')
            senha.send_keys(SENHA)
            senha.send_keys(Keys.ENTER)
            time.sleep(3)

            # Acessando menú do usuário
            icone_usuario = driver.find_elements_by_xpath("//*[@class='user-avatar']")
            icone_usuario[0].click()

            # Acessando a informações da conta
            icone_informacoes_conta = driver.find_element_by_xpath('//a[contains(@href,"conta.php")]')
            icone_informacoes_conta.click()

            nome_cliente = driver.find_element_by_css_selector("#litnome_cliente")
            email_cliente = driver.find_element_by_css_selector("#litemail")
            telefone_cliente = driver.find_element_by_css_selector("#littelefone1")

            nome_cliente, email_cliente, telefone_cliente = nome_cliente.get_attribute("value"), email_cliente.get_attribute(
                "value"), telefone_cliente.get_attribute("value")

            print('\n\n==============> ', i, url, nome_cliente, email_cliente, telefone_cliente, end="\n")
            driver.close()

            data.append([i, url, nome_cliente,  email_cliente, telefone_cliente])
        except:
            data.append([i, url, nome_cliente,  email_cliente, telefone_cliente])
            print('\n\n==============> ', i, url, nome_cliente,  email_cliente, telefone_cliente, end="\n")

            driver.close()

header = ['#', 'url', 'nome do cliente', 'email', 'telefone']

with open('contas.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(data)
