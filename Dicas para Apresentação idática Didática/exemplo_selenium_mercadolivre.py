#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Exemplo Prático: Extração de dados de produtos do Mercado Livre

Este script demonstra como usar o Selenium para extrair informações de produtos
em promoção do Mercado Livre, incluindo nome, preço, desconto e link.

Conceitos demonstrados:
- Configuração do WebDriver
- Navegação em páginas web
- Localização de elementos com diferentes seletores
- Extração de dados estruturados
- Esperas explícitas para carregamento de elementos
- Tratamento de exceções
- Exportação de dados para JSON

Autor: Equipe do Minicurso de Automação com Python
Data: Abril de 2025
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import json
import time
import os
import re

# Diretório para salvar os dados
DADOS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dados')
os.makedirs(DADOS_DIR, exist_ok=True)

def configurar_driver():
    """
    Configura e inicializa o WebDriver do Chrome com opções personalizadas.
    
    Returns:
        webdriver.Chrome: Instância configurada do WebDriver
    """
    print("Configurando o WebDriver...")
    
    # Configurar opções do Chrome
    options = Options()
    options.add_argument("--start-maximized")  # Iniciar maximizado
    options.add_argument("--disable-notifications")  # Desabilitar notificações
    
    # Configurações para ambiente headless (sem interface gráfica)
    # Descomente as linhas abaixo para executar em modo headless
    # options.add_argument("--headless")
    # options.add_argument("--disable-gpu")
    # options.add_argument("--window-size=1920,1080")
    
    # Inicializar o driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    return driver

def extrair_produtos_mercadolivre(categoria="informatica", num_produtos=10):
    """
    Extrai informações de produtos em promoção do Mercado Livre.
    
    Args:
        categoria (str): Categoria de produtos a ser pesquisada
        num_produtos (int): Número máximo de produtos a serem extraídos
        
    Returns:
        list: Lista de dicionários com informações dos produtos
    """
    driver = configurar_driver()
    produtos = []
    
    try:
        # URL da página de ofertas do Mercado Livre
        url = f"https://www.mercadolivre.com.br/ofertas#filter=category:{categoria}"
        print(f"Acessando: {url}")
        driver.get(url)
        
        # Aguardar o carregamento dos produtos
        print("Aguardando carregamento da página...")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ol.items_container li")))
        
        # Dar tempo para carregamento completo (pode ser necessário em conexões lentas)
        time.sleep(2)
        
        # Localizar os cards de produtos
        print("Localizando produtos...")
        cards = driver.find_elements(By.CSS_SELECTOR, "ol.items_container li")
        
        # Limitar ao número desejado de produtos
        cards = cards[:min(len(cards), num_produtos)]
        
        print(f"Encontrados {len(cards)} produtos. Extraindo informações...")
        
        # Extrair informações de cada produto
        for i, card in enumerate(cards):
            try:
                # Extrair nome do produto
                nome_elemento = card.find_element(By.CSS_SELECTOR, "p.promotion-item__title")
                nome = nome_elemento.text.strip()
                
                # Extrair preço atual
                preco_elemento = card.find_element(By.CSS_SELECTOR, "span.andes-money-amount__fraction")
                preco_centavos_elemento = card.find_elements(By.CSS_SELECTOR, "span.andes-money-amount__cents")
                
                preco_inteiro = preco_elemento.text.replace(".", "")
                preco_centavos = preco_centavos_elemento[0].text if preco_centavos_elemento else "00"
                preco_atual = float(f"{preco_inteiro}.{preco_centavos}")
                
                # Extrair preço original (se disponível)
                try:
                    preco_original_elemento = card.find_element(By.CSS_SELECTOR, "s.andes-money-amount__previous")
                    preco_original_texto = preco_original_elemento.text.strip()
                    # Remover símbolos e converter para float
                    preco_original = float(re.sub(r'[^\d,]', '', preco_original_texto).replace(',', '.'))
                except NoSuchElementException:
                    preco_original = preco_atual  # Se não houver preço original, usar o atual
                
                # Calcular desconto
                if preco_original > preco_atual:
                    desconto = (preco_original - preco_atual) / preco_original
                else:
                    desconto = 0.0
                
                # Extrair link do produto
                link_elemento = card.find_element(By.CSS_SELECTOR, "a.promotion-item__link-container")
                link = link_elemento.get_attribute("href")
                
                # Extrair URL da imagem
                try:
                    img_elemento = card.find_element(By.CSS_SELECTOR, "img.promotion-item__img")
                    img_url = img_elemento.get_attribute("src")
                except NoSuchElementException:
                    img_url = ""
                
                # Criar dicionário com informações do produto
                produto = {
                    "nome": nome,
                    "preco_atual": preco_atual,
                    "preco_original": preco_original,
                    "desconto": round(desconto * 100, 2),  # Converter para porcentagem
                    "link": link,
                    "imagem": img_url,
                    "categoria": categoria
                }
                
                produtos.append(produto)
                print(f"  Produto {i+1}: {nome} - R$ {preco_atual:.2f}")
                
            except Exception as e:
                print(f"  Erro ao extrair produto {i+1}: {str(e)}")
        
        print(f"Extração concluída. Total de produtos extraídos: {len(produtos)}")
        
    except TimeoutException:
        print("Erro: Tempo limite excedido ao carregar a página.")
    except Exception as e:
        print(f"Erro durante a extração: {str(e)}")
    finally:
        # Fechar o navegador
        driver.quit()
        print("Navegador fechado.")
    
    return produtos

def salvar_dados(produtos, nome_arquivo="produtos_mercadolivre.json"):
    """
    Salva os dados dos produtos em um arquivo JSON.
    
    Args:
        produtos (list): Lista de dicionários com informações dos produtos
        nome_arquivo (str): Nome do arquivo para salvar os dados
    """
    caminho_arquivo = os.path.join(DADOS_DIR, nome_arquivo)
    
    try:
        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
            json.dump(produtos, f, ensure_ascii=False, indent=4)
        print(f"Dados salvos com sucesso em: {caminho_arquivo}")
    except Exception as e:
        print(f"Erro ao salvar dados: {str(e)}")

def main():
    """Função principal do script."""
    print("=" * 60)
    print("EXTRAÇÃO DE PRODUTOS EM PROMOÇÃO DO MERCADO LIVRE")
    print("=" * 60)
    
    # Categorias disponíveis
    categorias = {
        "1": "informatica",
        "2": "celulares",
        "3": "eletrodomesticos",
        "4": "casa-moveis-decoracao",
        "5": "esportes-fitness"
    }
    
    # Exibir opções de categorias
    print("\nCategorias disponíveis:")
    for key, value in categorias.items():
        print(f"{key}. {value.replace('-', ' ').title()}")
    
    # Solicitar escolha do usuário
    escolha = input("\nEscolha uma categoria (1-5) ou pressione Enter para usar 'informatica': ")
    categoria = categorias.get(escolha, "informatica")
    
    # Solicitar número de produtos
    try:
        num_produtos = int(input("Quantos produtos deseja extrair? (padrão: 10): "))
    except ValueError:
        num_produtos = 10
    
    print("\nIniciando extração de dados...")
    produtos = extrair_produtos_mercadolivre(categoria, num_produtos)
    
    if produtos:
        nome_arquivo = f"produtos_mercadolivre_{categoria}.json"
        salvar_dados(produtos, nome_arquivo)
        
        # Exibir estatísticas básicas
        if produtos:
            precos = [p["preco_atual"] for p in produtos]
            descontos = [p["desconto"] for p in produtos]
            
            print("\nEstatísticas:")
            print(f"  Preço médio: R$ {sum(precos)/len(precos):.2f}")
            print(f"  Preço mínimo: R$ {min(precos):.2f}")
            print(f"  Preço máximo: R$ {max(precos):.2f}")
            print(f"  Desconto médio: {sum(descontos)/len(descontos):.2f}%")
            print(f"  Maior desconto: {max(descontos):.2f}%")
    else:
        print("Nenhum produto foi extraído.")
    
    print("\nProcesso concluído!")

if __name__ == "__main__":
    main()
