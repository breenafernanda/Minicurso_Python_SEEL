"""INSTALAR BIBLIOTECAS NECESSARIAS
pip install selenium
pip install ChromeDriverManager
"""
# importar bibliotecas necessárias
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from colorama import Fore, Style
import openpyxl
from openpyxl import Workbook
import pandas as pd

# Função para imprimir colorido no terminal 
def imprimir(texto, valor):
    print(f"{Fore.LIGHTMAGENTA_EX}{texto}: {Fore.CYAN}{valor}{Style.RESET_ALL}")


""" Script do Projeto - Selenium """
# Inicializa WebDriver Chrome
def abrir_navegador():
    driver = webdriver.Chrome(Options())
    return driver

# Extrair dados de 1 produto - retorna {produto}
def extrair_dados_selenium(driver, url):
    try:
        # acessar url 
        driver.get(url)
        time.sleep(5)

        """IDENTIFICAR SELETORES DE ELEMENTO WEB"""
        id_nome_produto = 'productTitle'
        selector_porcentagem_desconto = '#corePriceDisplay_desktop_feature_div > div.a-section.a-spacing-none.aok-align-center.aok-relative > span.a-size-large.a-color-price.savingPriceOverride.aok-align-center.reinventPriceSavingsPercentageMargin.savingsPercentage'
        selector_preço_desconto = '#corePriceDisplay_desktop_feature_div > div.a-section.a-spacing-none.aok-align-center.aok-relative > span.a-price.aok-align-center.reinventPricePriceToPayMargin.priceToPay > span:nth-child(2)'
        selector_preço_original = '#corePriceDisplay_desktop_feature_div > div.a-section.a-spacing-small.aok-align-center > span > span.aok-relative > span.a-size-small.a-color-secondary.aok-align-center.basisPrice > span > span:nth-child(2)'
        xpath_imagem_produto = '//*[@id="landingImage"]'
        
        # extrair nome do produto
        nome_do_produto = driver.find_element(By.ID, id_nome_produto).text
        imprimir("Nome do Produto", nome_do_produto)

        # Porcentagem de desconto 
        porcentagem_desconto = driver.find_element(By.CSS_SELECTOR, selector_porcentagem_desconto).text
        imprimir("Desconto (%)", porcentagem_desconto)

        # extrair preço original
        preço_original = driver.find_element(By.CSS_SELECTOR, selector_preço_original).text
        imprimir("Preço Original", preço_original)

        # extrair preço com desconto
        preço_desconto = driver.find_element(By.CSS_SELECTOR, selector_preço_desconto).text.replace("\n", ',')
        imprimir("Preço com Desconto", preço_desconto)
        
        # extrair imagem 
        elemento_imagem = driver.find_element(By.XPATH, xpath_imagem_produto).get_attribute('src')
        imprimir("Imagem (scr)", elemento_imagem)

        # Criar dicionário com todos os dados do Produto
        produto = {
            "Nome": nome_do_produto,
            "Desconto %": porcentagem_desconto,
            "Preço Original": preço_original,
            "Preço com Desconto": preço_desconto,
            "URL da Imagem": elemento_imagem
        }
        print(f'{Fore.LIGHTMAGENTA_EX}------------------------------------{Style.RESET_ALL}')
        return produto
    
    except: 
        img_recaptcha = 'body > div > div.a-row.a-spacing-double-large > div.a-section > div > div > form > div.a-row.a-spacing-large > div > div > div.a-row.a-text-center > img'
        try: 
            while True:
                try:
                    recaptcha = driver.find_element(By.CSS_SELECTOR, img_recaptcha).get_attribute('src')
                    print(f'{Fore.RED}Resolva o Recaptcha{Style.RESET_ALL}')
                    time.sleep(5)
                except: break 
            return extrair_dados_selenium(driver, url)


        except: print('Recaptcha não localizado.')
        time.sleep(1000)

# Extrair dados de todos produtos - retorna [produtos]
def extrair_produtos():
    # Inicializar webdriver
    driver = abrir_navegador()
    
    # Definir URL's
    url1 = 'https://www.amazon.com.br/Recado-3M-Autoadesivo-Cole%C3%A7%C3%A3o-Supernova/dp/B09YYGCPGV?ref=dlx_deals_dg_dcl_B09YYGCPGV_dt_sl14_ac&pf_rd_r=ZRWD59DBNHXQHY5Q6966&pf_rd_p=2d04dc0d-d8ca-40f6-b7ec-b3fce0874cac'
    url2 = 'https://www.amazon.com.br/Xixaomiro-Teclado-Polegada-1920x1200-8000mAh/dp/B0D1FN49HJ?ref=dlx_deals_dg_dcl_B0D1FN49HJ_dt_sl14_ac&pf_rd_r=DVX7TFBWJ55KHMK0NE8A&pf_rd_p=2d04dc0d-d8ca-40f6-b7ec-b3fce0874cac'
    url3 = 'https://www.amazon.com.br/GameSir-G7-SE-Controle-Joysticks/dp/B0C7GW9F88?ref=dlx_deals_dg_dcl_B0C7GW9F88_dt_sl14_ac&pf_rd_r=M50A1FM4X6NTCE7ASXW4&pf_rd_p=2d04dc0d-d8ca-40f6-b7ec-b3fce0874cac'
    vetor_de_urls = [url1, url2, url3]

    # Iniciar lista de
    produtos = []

    for url in vetor_de_urls:
        produto = extrair_dados_selenium(driver, url)
        produtos.append(produto)

    # print(f'{Fore.YELLOW}{produtos}{Style.RESET_ALL}')

    # Fechar webdriver
    driver.quit()
    
    # Retorna o vetor de produtos
    return produtos

""" Script do Projeto - Openpyxl """
# Salvar [produtos] em "planilha.xlsx"

def salvar_planilha(produtos, nome_arquivo='planilha.xlsx'):
    # Cria um novo Workbook
    wb = Workbook()
    # Seleciona a planilha ativa
    ws = wb.active
    # Define o título da planilha
    ws.title = 'Produtos'

    # Adiciona o cabeçalho
    cabecalho = ['Nome', 'Desconto %', 'Preço Original', 'Preço com Desconto', 'URL da Imagem']  
    ws.append(cabecalho)

    # Adiciona os dados dos produtos
    for produto in produtos:
        ws.append([produto['Nome'], produto['Desconto %'], produto['Preço Original'], produto['Preço com Desconto'], produto['URL da Imagem']])
        # Ajuste as chaves conforme a estrutura do dicionário 'produto'

    # Salva o arquivo Excel
    wb.save(nome_arquivo)
    imprimir(f'Planilha salva como', f'{nome_arquivo}')
    return nome_arquivo



# Script Execução
if __name__ == "__main__": 
    # 1ª etapa (Extrair dados da Web)
    produtos = extrair_produtos()

    # 2ª etapa (Salvar dados no excel)
    planilha = salvar_planilha(produtos)
