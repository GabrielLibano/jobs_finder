import time
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By

sendkey = "Analista de dados Junior"


driver = webdriver.Chrome()  # Optional argument, if not specified will search path.

driver.get('https://www.glassdoor.com.br/Sal%C3%A1rios/index.htm');

time.sleep(0.5)

#Buscando o salario daquele trabalho
driver.find_element(By.ID, 'KeywordSearch').send_keys(sendkey)
driver.find_element(By.ID,"HeroSearchButton").click()
time.sleep(2)

#Pegando o salario e qtd
mediaSalarial = driver.find_element(By.CLASS_NAME, 'ebrouyy2').text
qtdSalarios = driver.find_element(By.CLASS_NAME, 'css-1vkj9it').text
table = {"Media salárial":[mediaSalarial], "Quantidade de Salario Reportado":[qtdSalarios], "Title": [sendkey]}
print (table)
testedf = pd.DataFrame(table)
testedf.to_excel("salarios.xlsx")

time.sleep(5)

driver.quit()



####
    # driver = webdriver.Chrome()  # Optional argument, if not specified will search path.

    # driver.get('https://www.glassdoor.com.br/Sal%C3%A1rios/index.htm');

    # time.sleep(0.5)

    # #Buscando o salario daquele trabalho
    # driver.find_element(By.ID, 'KeywordSearch').send_keys(search_term)
    # driver.find_element(By.ID,"HeroSearchButton").click()
    # time.sleep(2)

    # #Pegando o salario e qtd
    # mediaSalarial = driver.find_element(By.CLASS_NAME, 'ebrouyy2').text
    # qtdSalarios = driver.find_element(By.CLASS_NAME, 'css-1vkj9it').text
    # table = {"Media salárial":[mediaSalarial], "Quantidade de Salario Reportado":[qtdSalarios]}
    # testedf = pd.DataFrame(table)
    # testedf.to_excel("salarios.xlsx")

    # time.sleep(5)

    # driver.quit()

    # jobs_all['k'] = 1
    # testedf['k'] = 1
    # resultado = pd.merge(jobs_all, testedf, on=['k'])
    # resultado = resultado.drop(["k"],axis=1)

    # resultado.to_excel("\export\jobs.xlsx")

    