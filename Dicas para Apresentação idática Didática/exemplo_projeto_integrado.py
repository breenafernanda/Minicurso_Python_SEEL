#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Projeto Integrado: Sistema Completo de Monitoramento de Preços

Este script integra todas as tecnologias apresentadas no minicurso para criar
um sistema completo de monitoramento de preços, desde a extração de dados
até a geração de relatórios e catálogos.

Tecnologias integradas:
- Selenium para extração de dados de e-commerce
- Pandas para análise e processamento de dados
- OpenPyXL para geração de relatórios em Excel
- ReportLab para criação de catálogos em PDF
- Matplotlib para visualizações

Autor: Equipe do Minicurso de Automação com Python
Data: Abril de 2025
"""

import os
import json
import time
import random
import argparse
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from webdriver_manager.chrome import ChromeDriverManager
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.chart import BarChart, PieChart, Reference
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak

# Configurações globais
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'dados')
IMAGES_DIR = os.path.join(BASE_DIR, 'imagens')
REPORTS_DIR = os.path.join(BASE_DIR, 'relatorios')
HISTORY_FILE = os.path.join(DATA_DIR, 'historico_precos.json')

# Criar diretórios se não existirem
for directory in [DATA_DIR, IMAGES_DIR, REPORTS_DIR]:
    os.makedirs(directory, exist_ok=True)

# Cores para uso nos relatórios
COLORS = {
    'blue_light': '#B3E0FF',
    'blue_dark': '#0078D7',
    'green_light': '#C6EFCE',
    'green_dark': '#006100',
    'red_light': '#FFC7CE',
    'red_dark': '#9C0006',
    'yellow_light': '#FFEB9C',
    'yellow_dark': '#9C6500',
    'gray_light': '#F2F2F2',
    'gray_dark': '#595959',
    'white': '#FFFFFF',
    'black': '#000000'
}

# Configurações para ReportLab
RL_COLORS = {
    'blue_light': colors.Color(0.7, 0.85, 1),
    'blue_dark': colors.Color(0, 0.47, 0.84),
    'green_light': colors.Color(0.78, 0.94, 0.8),
    'green_dark': colors.Color(0, 0.38, 0),
    'red_light': colors.Color(1, 0.78, 0.8),
    'red_dark': colors.Color(0.61, 0, 0.02),
    'yellow_light': colors.Color(1, 0.92, 0.61),
    'yellow_dark': colors.Color(0.61, 0.4, 0),
    'gray_light': colors.Color(0.95, 0.95, 0.95),
    'gray_dark': colors.Color(0.35, 0.35, 0.35),
    'white': colors.white,
    'black': colors.black
}

class PriceMonitor:
    """Classe principal para o sistema de monitoramento de preços."""
    
    def __init__(self, config=None):
        """
        Inicializa o sistema de monitoramento.
        
        Args:
            config (dict, optional): Configurações personalizadas.
        """
        self.config = {
            'max_products': 50,
            'min_discount': 10,  # Desconto mínimo para destacar produtos (%)
            'search_terms': ['ofertas do dia', 'promoção', 'liquidação'],
            'target_sites': ['mercadolivre', 'amazon'],
            'history_days': 30,  # Dias para manter no histórico
            'report_types': ['excel', 'pdf']
        }
        
        if config:
            self.config.update(config)
        
        self.today = datetime.now().strftime('%Y-%m-%d')
        self.products = []
        self.history = self._load_history()
        
        print(f"Sistema de Monitoramento de Preços inicializado.")
        print(f"Data atual: {self.today}")
        print(f"Configurações: {self.config}")
    
    def _load_history(self):
        """
        Carrega o histórico de preços.
        
        Returns:
            dict: Histórico de preços por produto e data.
        """
        if os.path.exists(HISTORY_FILE):
            try:
                with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
                    history = json.load(f)
                print(f"Histórico carregado: {len(history)} produtos.")
                return history
            except Exception as e:
                print(f"Erro ao carregar histórico: {str(e)}")
                return {}
        else:
            print("Arquivo de histórico não encontrado. Criando novo histórico.")
            return {}
    
    def _save_history(self):
        """Salva o histórico de preços atualizado."""
        try:
            with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
                json.dump(self.history, f, ensure_ascii=False, indent=4)
            print(f"Histórico salvo em: {HISTORY_FILE}")
        except Exception as e:
            print(f"Erro ao salvar histórico: {str(e)}")
    
    def _update_history(self):
        """Atualiza o histórico com os produtos extraídos hoje."""
        # Adicionar produtos de hoje ao histórico
        for product in self.products:
            product_id = product.get('id') or product.get('nome')
            if product_id not in self.history:
                self.history[product_id] = {}
            
            self.history[product_id][self.today] = {
                'nome': product.get('nome', ''),
                'preco': product.get('preco_atual', 0),
                'preco_original': product.get('preco_original', 0),
                'desconto': product.get('desconto', 0),
                'site': product.get('site', ''),
                'categoria': product.get('categoria', ''),
                'link': product.get('link', '')
            }
        
        # Remover entradas antigas (mais antigas que history_days)
        cutoff_date = (datetime.now() - timedelta(days=self.config['history_days'])).strftime('%Y-%m-%d')
        for product_id in list(self.history.keys()):
            for date in list(self.history[product_id].keys()):
                if date < cutoff_date:
                    del self.history[product_id][date]
            
            # Remover produto se não tiver mais datas
            if not self.history[product_id]:
                del self.history[product_id]
        
        # Salvar histórico atualizado
        self._save_history()
    
    def extract_data(self):
        """Extrai dados de produtos dos sites alvo."""
        self.products = []
        
        for site in self.config['target_sites']:
            for term in self.config['search_terms']:
                print(f"Extraindo dados de {site} para o termo: {term}")
                
                if site == 'mercadolivre':
                    products = self._extract_from_mercadolivre(term)
                elif site == 'amazon':
                    products = self._extract_from_amazon(term)
                else:
                    print(f"Site não suportado: {site}")
                    continue
                
                # Adicionar site de origem aos produtos
                for product in products:
                    product['site'] = site
                
                self.products.extend(products)
                
                # Adicionar delay entre extrações
                time.sleep(random.uniform(1, 3))
        
        # Limitar ao número máximo de produtos
        if len(self.products) > self.config['max_products']:
            self.products = self.products[:self.config['max_products']]
        
        print(f"Extração concluída. Total de produtos: {len(self.products)}")
        
        # Salvar dados extraídos
        self._save_extracted_data()
        
        # Atualizar histórico
        self._update_history()
    
    def _configure_driver(self):
        """
        Configura e inicializa o WebDriver do Chrome.
        
        Returns:
            webdriver.Chrome: Instância configurada do WebDriver
        """
        # Configurar opções do Chrome
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-infobars")
        
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
    
    def _extract_from_mercadolivre(self, search_term):
        """
        Extrai dados de produtos do Mercado Livre.
        
        Args:
            search_term (str): Termo de busca
            
        Returns:
            list: Lista de produtos extraídos
        """
        driver = self._configure_driver()
        products = []
        
        try:
            # URL da página de ofertas do Mercado Livre
            url = f"https://www.mercadolivre.com.br/ofertas#deal_print_id=undefined&c_id=special-normal&c_element_order=1&c_campaign=OFERTAS_FLASH&c_uid=undefined"
            if search_term != "ofertas do dia":
                url = f"https://lista.mercadolivre.com.br/{search_term.replace(' ', '-')}_Ofertas"
            
            print(f"Acessando: {url}")
            driver.get(url)
            
            # Aguardar o carregamento dos produtos
            wait = WebDriverWait(driver, 10)
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ol.items_container li, .ui-search-layout__item")))
            
            # Dar tempo para carregamento completo
            time.sleep(2)
            
            # Localizar os cards de produtos
            cards = driver.find_elements(By.CSS_SELECTOR, "ol.items_container li, .ui-search-layout__item")
            
            print(f"Encontrados {len(cards)} produtos. Extraindo informações...")
            
            # Extrair informações de cada produto
            for i, card in enumerate(cards):
                try:
                    # Extrair nome do produto
                    try:
                        nome_elemento = card.find_element(By.CSS_SELECTOR, "p.promotion-item__title, .ui-search-item__title")
                        nome = nome_elemento.text.strip()
                    except NoSuchElementException:
                        continue  # Pular se não encontrar o nome
                    
                    # Extrair preço atual
                    try:
                        preco_elemento = card.find_element(By.CSS_SELECTOR, "span.andes-money-amount__fraction")
                        preco_centavos_elemento = card.find_elements(By.CSS_SELECTOR, "span.andes-money-amount__cents")
                        
                        preco_inteiro = preco_elemento.text.replace(".", "")
                        preco_centavos = preco_centavos_elemento[0].text if preco_centavos_elemento else "00"
                        preco_atual = float(f"{preco_inteiro}.{preco_centavos}")
                    except (NoSuchElementException, ValueError, IndexError):
                        continue  # Pular se não encontrar o preço
                    
                    # Extrair preço original (se disponível)
                    try:
                        preco_original_elemento = card.find_element(By.CSS_SELECTOR, "s.andes-money-amount__previous, .ui-search-price__original-value .andes-money-amount__fraction")
                        preco_original_texto = preco_original_elemento.text.strip()
                        # Remover símbolos e converter para float
                        preco_original = float(preco_original_texto.replace(".", "").replace("R$", "").replace(" ", "").replace(",", "."))
                    except (NoSuchElementException, ValueError):
                        preco_original = preco_atual  # Se não houver preço original, usar o atual
                    
                    # Calcular desconto
                    if preco_original > preco_atual:
                        desconto = (preco_original - preco_atual) / preco_original * 100
                    else:
                        desconto = 0.0
                    
                    # Extrair link do produto
                    try:
                        link_elemento = card.find_element(By.CSS_SELECTOR, "a.promotion-item__link-container, .ui-search-link")
                        link = link_elemento.get_attribute("href")
                    except NoSuchElementException:
                        link = ""
                    
                    # Extrair URL da imagem
                    try:
                        img_elemento = card.find_element(By.CSS_SELECTOR, "img.promotion-item__img, .ui-search-result-image__element")
                        img_url = img_elemento.get_attribute("src") or img_elemento.get_attribute("data-src")
                    except NoSuchElementException:
                        img_url = ""
                    
                    # Extrair categoria (se disponível)
                    try:
                        categoria_elemento = card.find_element(By.CSS_SELECTOR, ".ui-search-item__group__element .ui-search-item__title, .promotion-item__category")
                        categoria = categoria_elemento.text.strip()
                    except NoSuchElementException:
                        categoria = "Não categorizado"
                    
                    # Criar dicionário com informações do produto
                    produto = {
                        'id': f"ml_{i+1}_{self.today}",
                        'nome': nome,
                        'preco_atual': preco_atual,
                        'preco_original': preco_original,
                        'desconto': round(desconto, 2),
                        'link': link,
                        'imagem': img_url,
                        'categoria': categoria,
                        'destaque': desconto >= self.config['min_discount'],
                        'data_extracao': self.today
                    }
                    
                    products.append(produto)
                    print(f"  Produto {i+1}: {nome} - R$ {preco_atual:.2f}")
                    
                    # Limitar ao número máximo de produtos
                    if len(products) >= self.config['max_products']:
                        break
                    
                except Exception as e:
                    print(f"  Erro ao extrair produto {i+1}: {str(e)}")
            
        except Exception as e:
            print(f"Erro durante a extração do Mercado Livre: {str(e)}")
        finally:
            driver.quit()
        
        return products
    
    def _extract_from_amazon(self, search_term):
        """
        Extrai dados de produtos da Amazon.
        
        Args:
            search_term (str): Termo de busca
            
        Returns:
            list: Lista de produtos extraídos
        """
        driver = self._configure_driver()
        products = []
        
        try:
            # URL da Amazon Brasil
            url = "https://www.amazon.com.br/"
            print(f"A
(Content truncated due to size limit. Use line ranges to read in chunks)