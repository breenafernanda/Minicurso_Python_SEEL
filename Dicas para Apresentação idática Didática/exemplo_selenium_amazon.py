#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Exemplo Prático: Extração de dados de produtos da Amazon

Este script demonstra como usar o Selenium para extrair informações de produtos
em promoção da Amazon, incluindo nome, preço, avaliação e detalhes.

Conceitos demonstrados:
- Configuração do WebDriver com opções avançadas
- Navegação em páginas web com cookies e headers personalizados
- Localização de elementos com XPath e seletores CSS
- Esperas explícitas e implícitas
- Rolagem de página para carregar conteúdo dinâmico
- Tratamento de exceções e cenários de erro
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
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from webdriver_manager.chrome import ChromeDriverManager
import json
import time
import os
import re
import random

# Diretório para salvar os dados
DADOS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dados')
os.makedirs(DADOS_DIR, exist_ok=True)

def configurar_driver():
    """
    Configura e inicializa o WebDriver do Chrome com opções avançadas.
    
    Returns:
        webdriver.Chrome: Instância configurada do WebDriver
    """
    print("Configurando o WebDriver...")
    
    # Configurar opções do Chrome
    options = Options()
    options.add_argument("--start-maximized")  # Iniciar maximizado
    options.add_argument("--disable-notifications")  # Desabilitar notificações
    options.add_argument("--disable-infobars")  # Desabilitar infobars
    options.add_argument("--disable-extensions")  # Desabilitar extensões
    
    # Adicionar User-Agent personalizado para evitar bloqueios
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    options.add_argument(f"user-agent={user_agent}")
    
    # Configurações para ambiente headless (sem interface gráfica)
    # Descomente as linhas abaixo para executar em modo headless
    # options.add_argument("--headless")
    # options.add_argument("--disable-gpu")
    # options.add_argument("--window-size=1920,1080")
    
    # Inicializar o driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    # Configurar espera implícita
    driver.implicitly_wait(10)
    
    return driver

def extrair_produtos_amazon(termo_busca="ofertas do dia", num_produtos=10):
    """
    Extrai informações de produtos da Amazon com base em um termo de busca.
    
    Args:
        termo_busca (str): Termo para pesquisar na Amazon
        num_produtos (int): Número máximo de produtos a serem extraídos
        
    Returns:
        list: Lista de dicionários com informações dos produtos
    """
    driver = configurar_driver()
    produtos = []
    
    try:
        # URL da Amazon Brasil
        url = "https://www.amazon.com.br/"
        print(f"Acessando: {url}")
        driver.get(url)
        
        # Aguardar carregamento da página inicial
        print("Aguardando carregamento da página inicial...")
        wait = WebDriverWait(driver, 10)
        campo_busca = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
        
        # Pesquisar o termo
        print(f"Pesquisando por: {termo_busca}")
        campo_busca.clear()
        campo_busca.send_keys(termo_busca)
        
        # Clicar no botão de busca
        botao_busca = driver.find_element(By.ID, "nav-search-submit-button")
        botao_busca.click()
        
        # Aguardar resultados da busca
        print("Aguardando resultados da busca...")
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.s-result-item")))
        
        # Dar tempo para carregamento completo
        time.sleep(2)
        
        # Função para extrair produtos da página atual
        def extrair_produtos_pagina():
            # Localizar os cards de produtos
            cards = driver.find_elements(By.CSS_SELECTOR, "div.s-result-item[data-component-type='s-search-result']")
            
            produtos_pagina = []
            for card in cards:
                try:
                    # Verificar se é um produto válido (não é patrocinado, etc.)
                    if "AdHolder" in card.get_attribute("class"):
                        continue
                    
                    # Extrair nome do produto
                    try:
                        nome_elemento = card.find_element(By.CSS_SELECTOR, "h2 a span")
                        nome = nome_elemento.text.strip()
                    except NoSuchElementException:
                        continue  # Pular se não encontrar o nome
                    
                    # Extrair preço atual
                    try:
                        preco_elemento = card.find_element(By.CSS_SELECTOR, "span.a-price-whole")
                        preco_centavos_elemento = card.find_element(By.CSS_SELECTOR, "span.a-price-fraction")
                        
                        preco_inteiro = preco_elemento.text.replace(".", "").replace(",", "")
                        preco_centavos = preco_centavos_elemento.text
                        preco_atual = float(f"{preco_inteiro}.{preco_centavos}")
                    except (NoSuchElementException, ValueError):
                        continue  # Pular se não encontrar o preço ou não conseguir converter
                    
                    # Extrair preço original (se disponível)
                    preco_original = None
                    try:
                        preco_original_elemento = card.find_element(By.CSS_SELECTOR, "span.a-price.a-text-price span.a-offscreen")
                        preco_original_texto = preco_original_elemento.get_attribute("innerHTML")
                        # Remover símbolos e converter para float
                        preco_original = float(re.sub(r'[^\d,.]', '', preco_original_texto.replace(",", ".")))
                    except (NoSuchElementException, ValueError):
                        preco_original = preco_atual  # Se não houver preço original, usar o atual
                    
                    # Calcular desconto
                    if preco_original and preco_original > preco_atual:
                        desconto = (preco_original - preco_atual) / preco_original
                    else:
                        desconto = 0.0
                    
                    # Extrair avaliação (se disponível)
                    avaliacao = None
                    num_avaliacoes = 0
                    try:
                        avaliacao_elemento = card.find_element(By.CSS_SELECTOR, "i.a-icon-star-small")
                        avaliacao_texto = avaliacao_elemento.get_attribute("class")
                        avaliacao_match = re.search(r'a-star-small-(\d+)', avaliacao_texto)
                        if avaliacao_match:
                            avaliacao = float(avaliacao_match.group(1)) / 10
                        
                        # Número de avaliações
                        num_avaliacoes_elemento = card.find_element(By.CSS_SELECTOR, "span.a-size-base.s-underline-text")
                        num_avaliacoes_texto = num_avaliacoes_elemento.text.replace(".", "").replace(",", "")
                        num_avaliacoes_match = re.search(r'(\d+)', num_avaliacoes_texto)
                        if num_avaliacoes_match:
                            num_avaliacoes = int(num_avaliacoes_match.group(1))
                    except (NoSuchElementException, ValueError, AttributeError):
                        pass  # Ignorar se não encontrar avaliação
                    
                    # Extrair link do produto
                    link = ""
                    try:
                        link_elemento = card.find_element(By.CSS_SELECTOR, "h2 a")
                        link = link_elemento.get_attribute("href")
                        # Limpar o link (remover parâmetros de rastreamento)
                        link = re.sub(r'/ref=.*$', '', link)
                    except NoSuchElementException:
                        pass
                    
                    # Extrair URL da imagem
                    img_url = ""
                    try:
                        img_elemento = card.find_element(By.CSS_SELECTOR, "img.s-image")
                        img_url = img_elemento.get_attribute("src")
                    except NoSuchElementException:
                        pass
                    
                    # Criar dicionário com informações do produto
                    produto = {
                        "nome": nome,
                        "preco_atual": preco_atual,
                        "preco_original": preco_original if preco_original != preco_atual else None,
                        "desconto": round(desconto * 100, 2) if desconto > 0 else 0,  # Converter para porcentagem
                        "avaliacao": avaliacao,
                        "num_avaliacoes": num_avaliacoes,
                        "link": link,
                        "imagem": img_url,
                        "termo_busca": termo_busca
                    }
                    
                    produtos_pagina.append(produto)
                    
                except StaleElementReferenceException:
                    # Elemento ficou obsoleto (página atualizou)
                    continue
                except Exception as e:
                    print(f"  Erro ao extrair produto: {str(e)}")
            
            return produtos_pagina
        
        # Extrair produtos da primeira página
        print("Extraindo produtos da página 1...")
        produtos_pagina = extrair_produtos_pagina()
        produtos.extend(produtos_pagina)
        print(f"  Encontrados {len(produtos_pagina)} produtos na página 1")
        
        # Se precisar de mais produtos e houver mais páginas, continuar
        pagina = 1
        while len(produtos) < num_produtos:
            # Verificar se há botão de próxima página
            try:
                proxima_pagina = driver.find_element(By.CSS_SELECTOR, "a.s-pagination-next")
                
                # Se encontrou o botão, clicar nele
                pagina += 1
                print(f"Navegando para a página {pagina}...")
                proxima_pagina.click()
                
                # Aguardar carregamento da nova página
                time.sleep(2 + random.uniform(0.5, 1.5))  # Adicionar delay aleatório para parecer mais humano
                
                # Extrair produtos da nova página
                print(f"Extraindo produtos da página {pagina}...")
                produtos_pagina = extrair_produtos_pagina()
                produtos.extend(produtos_pagina)
                print(f"  Encontrados {len(produtos_pagina)} produtos na página {pagina}")
                
                # Se não encontrou produtos nesta página, parar
                if not produtos_pagina:
                    break
                
            except NoSuchElementException:
                # Não há mais páginas
                print("Não há mais páginas de resultados.")
                break
            
            # Limitar ao número máximo de páginas (para evitar loops infinitos)
            if pagina >= 5:
                print("Limite máximo de páginas atingido.")
                break
        
        # Limitar ao número desejado de produtos
        produtos = produtos[:num_produtos]
        
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

def extrair_detalhes_produto(url):
    """
    Extrai detalhes adicionais de um produto específico.
    
    Args:
        url (str): URL da página do produto
        
    Returns:
        dict: Dicionário com detalhes adicionais do produto
    """
    driver = configurar_driver()
    detalhes = {}
    
    try:
        print(f"Acessando página do produto: {url}")
        driver.get(url)
        
        # Aguardar carregamento da página
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, "productTitle")))
        
        # Extrair descrição do produto
        try:
            descricao_elemento = driver.find_element(By.ID, "productDescription")
            detalhes["descricao"] = descricao_elemento.text.strip()
        except NoSuchElementException:
            detalhes["descricao"] = ""
        
        # Extrair características/especificações
        caracteristicas = {}
        try:
            # Tentar diferentes seletores para especificações
            for selector in ["#feature-bullets", "#technicalSpecifications_feature_div", "#detailBullets_feature_div"]:
                try:
                    specs_elemento = driver.find_element(By.CSS_SELECTOR, selector)
                    items = specs_elemento.find_elements(By.CSS_SELECTOR, "li")
                    
                    for item in items:
                        texto = item.text.strip()
                        if ":" in texto:
                            chave, valor = texto.split(":", 1)
                            caracteristicas[chave.strip()] = valor.strip()
                        else:
                            # Para bullets sem chave:valor
                            caracteristicas[f"item_{len(caracteristicas)+1}"] = texto
                    
                    if caracteristicas:
                        break  # Se encontrou especificações, parar de procurar
                except NoSuchElementException:
                    continue
        except Exception as e:
            print(f"Erro ao extrair características: {str(e)}")
        
        detalhes["caracteristicas"] = caracteristicas
        
        # Extrair disponibilidade
        try:
            disponibilidade_elemento = driver.find_element(By.ID, "availability")
            detalhes["disponibilidade"] = disponibilidade_elemento.text.strip()
        except NoSuchElementException:
            detalhes["disponibilidade"] = "Não informado"
        
        # Extrair vendedor
        try:
            vendedor_elemento = driver.find_element(By.CSS_SELECTOR, "#merchant-info")
            detalhes["vendedor"] = vendedor_elemento.text.strip()
        except NoSuchElementException:
            detalhes["vendedor"] = "Amazon"
        
        print("Detalhes do produto extraídos com sucesso.")
        
    except Exception as e:
        print(f"Erro ao extrair detalhes do produto: {str(e)}")
    finally:
        driver.quit()
    
    return detalhes

def salvar_dados(produtos, nome_arquivo="produtos_amazon.json"):
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
    print("EXTRAÇÃO
(Content truncated due to size limit. Use line ranges to read in chunks)