#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Exemplo Prático: Geração de catálogo de produtos em PDF

Este script demonstra como usar a biblioteca ReportLab para criar
catálogos de produtos em PDF com formatação profissional, incluindo
imagens, tabelas, gráficos e elementos visuais.

Conceitos demonstrados:
- Criação de documentos PDF com ReportLab
- Formatação de texto e parágrafos
- Adição de imagens e elementos gráficos
- Criação de tabelas formatadas
- Geração de gráficos e visualizações
- Criação de cabeçalhos e rodapés
- Numeração de páginas e índice
- Uso de estilos consistentes

Autor: Equipe do Minicurso de Automação com Python
Data: Abril de 2025
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm, mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Image, 
                               Table, TableStyle, PageBreak, ListFlowable, 
                               ListItem, Frame, PageTemplate, NextPageTemplate)
from reportlab.platypus.flowables import Flowable, HRFlowable
from reportlab.platypus.frames import Frame
from reportlab.platypus.doctemplate import PageTemplate
from reportlab.graphics.shapes import Drawing, Rect
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.piecharts import Pie
from reportlab.pdfgen import canvas
import json
import os
import random
from datetime import datetime
import io
import matplotlib.pyplot as plt
import numpy as np

# Diretórios
DADOS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dados')
IMAGENS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'imagens')
os.makedirs(DADOS_DIR, exist_ok=True)
os.makedirs(IMAGENS_DIR, exist_ok=True)

# Cores para uso no catálogo
CORES = {
    'azul_claro': colors.Color(0.7, 0.85, 1),
    'azul_escuro': colors.Color(0, 0.47, 0.84),
    'verde_claro': colors.Color(0.78, 0.94, 0.8),
    'verde_escuro': colors.Color(0, 0.38, 0),
    'vermelho_claro': colors.Color(1, 0.78, 0.8),
    'vermelho_escuro': colors.Color(0.61, 0, 0.02),
    'amarelo_claro': colors.Color(1, 0.92, 0.61),
    'amarelo_escuro': colors.Color(0.61, 0.4, 0),
    'cinza_claro': colors.Color(0.95, 0.95, 0.95),
    'cinza_escuro': colors.Color(0.35, 0.35, 0.35),
    'branco': colors.white,
    'preto': colors.black
}

class Cabecalho(Flowable):
    """Classe para criar cabeçalho personalizado em cada página."""
    
    def __init__(self, width=None, height=None):
        Flowable.__init__(self)
        self.width = width or A4[0]
        self.height = height or 2.5*cm
        self.styles = getSampleStyleSheet()
    
    def coord(self, x, y, unit=1):
        """Converte coordenadas para o sistema do ReportLab."""
        x, y = x * unit, self.height - y * unit
        return x, y
    
    def draw(self):
        """Desenha o cabeçalho."""
        # Configurar canvas
        self.canv.saveState()
        
        # Desenhar retângulo de fundo
        self.canv.setFillColor(CORES['azul_escuro'])
        self.canv.rect(0, 0, self.width, self.height, stroke=0, fill=1)
        
        # Adicionar título
        self.canv.setFont('Helvetica-Bold', 16)
        self.canv.setFillColor(CORES['branco'])
        self.canv.drawString(1*cm, self.height-1.3*cm, "CATÁLOGO DE PRODUTOS")
        
        # Adicionar data
        self.canv.setFont('Helvetica', 10)
        data_atual = datetime.now().strftime("%d/%m/%Y")
        self.canv.drawRightString(self.width-1*cm, self.height-1.3*cm, f"Atualizado em: {data_atual}")
        
        # Adicionar linha decorativa
        self.canv.setStrokeColor(CORES['branco'])
        self.canv.setLineWidth(1)
        self.canv.line(1*cm, 0.5*cm, self.width-1*cm, 0.5*cm)
        
        self.canv.restoreState()

class Rodape(Flowable):
    """Classe para criar rodapé personalizado em cada página."""
    
    def __init__(self, width=None, height=None, numero_pagina=None):
        Flowable.__init__(self)
        self.width = width or A4[0]
        self.height = height or 1.5*cm
        self.numero_pagina = numero_pagina
        self.styles = getSampleStyleSheet()
    
    def draw(self):
        """Desenha o rodapé."""
        # Configurar canvas
        self.canv.saveState()
        
        # Desenhar linha superior
        self.canv.setStrokeColor(CORES['cinza_escuro'])
        self.canv.setLineWidth(0.5)
        self.canv.line(1*cm, self.height-0.5*cm, self.width-1*cm, self.height-0.5*cm)
        
        # Adicionar texto de copyright
        self.canv.setFont('Helvetica', 8)
        self.canv.setFillColor(CORES['cinza_escuro'])
        self.canv.drawString(1*cm, 0.5*cm, "© 2025 Minicurso de Automação com Python. Todos os direitos reservados.")
        
        # Adicionar número de página
        if self.numero_pagina is not None:
            self.canv.drawRightString(self.width-1*cm, 0.5*cm, f"Página {self.numero_pagina}")
        
        self.canv.restoreState()

class NumeroPagina(Flowable):
    """Classe para adicionar número de página."""
    
    def __init__(self, numero=None):
        Flowable.__init__(self)
        self.numero = numero
    
    def draw(self):
        if self.numero is not None:
            self.canv.saveState()
            self.canv.setFont('Helvetica', 9)
            self.canv.drawRightString(A4[0]-1*cm, 0.75*cm, f"Página {self.numero}")
            self.canv.restoreState()

def carregar_dados(arquivo=None):
    """
    Carrega dados de produtos de um arquivo JSON.
    
    Args:
        arquivo (str, optional): Nome do arquivo específico a ser carregado.
            Se None, tenta carregar qualquer arquivo de produtos disponível.
    
    Returns:
        list: Lista de dicionários com os dados dos produtos
    """
    # Se nenhum arquivo específico foi fornecido, procurar por arquivos de produtos
    if arquivo is None:
        arquivos_json = [f for f in os.listdir(DADOS_DIR) if f.startswith('produtos_') and f.endswith('.json')]
        if not arquivos_json:
            print("Nenhum arquivo de produtos encontrado. Gerando dados de exemplo...")
            return gerar_dados_exemplo()
        
        # Usar o arquivo mais recente
        arquivo = max(arquivos_json, key=lambda f: os.path.getmtime(os.path.join(DADOS_DIR, f)))
    
    caminho_arquivo = os.path.join(DADOS_DIR, arquivo)
    print(f"Carregando dados de: {caminho_arquivo}")
    
    try:
        # Carregar dados do JSON
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            dados = json.load(f)
        
        print(f"Dados carregados com sucesso: {len(dados)} produtos")
        return dados
    
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho_arquivo}")
        return gerar_dados_exemplo()
    
    except Exception as e:
        print(f"Erro ao carregar dados: {str(e)}")
        return gerar_dados_exemplo()

def gerar_dados_exemplo():
    """
    Gera dados fictícios de produtos para demonstração.
    
    Returns:
        list: Lista de dicionários com dados fictícios
    """
    print("Gerando dados de exemplo...")
    
    # Criar dados fictícios
    dados = []
    categorias = ['Informática', 'Eletrônicos', 'Celulares', 'Acessórios', 'Casa']
    
    # Nomes de produtos por categoria
    produtos_por_categoria = {
        'Informática': [
            'Notebook Dell Inspiron 15', 'MacBook Air M1', 'Monitor LG 24"', 
            'Teclado Mecânico Redragon', 'Mouse sem fio Logitech', 'SSD Kingston 480GB',
            'Memória RAM Corsair 16GB', 'Placa de Vídeo NVIDIA GTX 1660', 
            'Roteador TP-Link Archer C6', 'Impressora HP LaserJet'
        ],
        'Eletrônicos': [
            'Smart TV Samsung 50"', 'Soundbar JBL 2.1', 'Fone de Ouvido Sony WH-1000XM4',
            'Caixa de Som Bluetooth JBL', 'Chromecast Google TV', 'Echo Dot 4ª Geração',
            'Câmera Canon EOS Rebel', 'Projetor Epson PowerLite', 'Kindle Paperwhite',
            'Apple Watch Series 7'
        ],
        'Celulares': [
            'iPhone 13 Pro', 'Samsung Galaxy S21', 'Xiaomi Redmi Note 10', 
            'Motorola Edge 20', 'Realme GT Master', 'POCO X3 Pro',
            'OnePlus 9', 'Google Pixel 6', 'Asus Zenfone 8', 'LG Velvet'
        ],
        'Acessórios': [
            'Carregador Wireless Samsung', 'Capa para iPhone Silicone', 'Película de Vidro',
            'Suporte para Notebook', 'Hub USB-C 8 em 1', 'Mochila para Notebook',
            'Fone de Ouvido Bluetooth i12', 'Power Bank 10000mAh', 'Tripé para Celular',
            'Controle para Jogos Bluetooth'
        ],
        'Casa': [
            'Aspirador de Pó Robô', 'Cafeteira Elétrica', 'Fritadeira Air Fryer',
            'Liquidificador Philips Walita', 'Panela Elétrica de Arroz', 'Ventilador de Mesa',
            'Umidificador de Ar', 'Purificador de Água', 'Jogo de Panelas Tramontina',
            'Kit de Facas Inox'
        ]
    }
    
    # Descrições genéricas por categoria
    descricoes_por_categoria = {
        'Informática': [
            "Ideal para trabalho e estudo com excelente desempenho.",
            "Alta performance para tarefas do dia a dia e jogos leves.",
            "Qualidade de imagem excepcional e design moderno.",
            "Conforto e precisão para longas horas de uso.",
            "Conectividade estável e rápida para sua rede doméstica."
        ],
        'Eletrônicos': [
            "Qualidade de imagem 4K com cores vibrantes e realistas.",
            "Som imersivo que transforma sua experiência de áudio.",
            "Conectividade inteligente com todos os seus dispositivos.",
            "Design elegante e funcionalidades avançadas.",
            "Tecnologia de ponta para seu entretenimento."
        ],
        'Celulares': [
            "Câmera profissional para fotos incríveis em qualquer condição.",
            "Bateria de longa duração para o dia todo de uso intenso.",
            "Processador potente para multitarefas e jogos.",
            "Tela de alta resolução com cores vibrantes.",
            "Design premium com acabamento de alta qualidade."
        ],
        'Acessórios': [
            "Compatível com diversos dispositivos para maior versatilidade.",
            "Material durável e resistente para uso prolongado.",
            "Design compacto e portátil, ideal para viagens.",
            "Proteção completa contra quedas e arranhões.",
            "Facilita seu dia a dia com praticidade e eficiência."
        ],
        'Casa': [
            "Facilita tarefas domésticas com eficiência e praticidade.",
            "Design moderno que combina com qualquer decoração.",
            "Economia de energia com alta performance.",
            "Material de alta qualidade para maior durabilidade.",
            "Tecnologia avançada para mais conforto no seu lar."
        ]
    }
    
    # Características por categoria
    caracteristicas_por_categoria = {
        'Informática': [
            "Processador Intel/AMD", "Memória RAM", "Armazenamento SSD/HD", 
            "Placa de vídeo", "Sistema operacional", "Conectividade"
        ],
        'Eletrônicos': [
            "Resolução de tela", "Potência de som", "Conectividade", 
            "Tecnologia de imagem", "Recursos smart", "Eficiência energética"
        ],
        'Celulares': [
            "Processador", "Memória RAM", "Armazenamento", 
            "Câmera", "Bateria", "Tela", "Sistema operacional"
        ],
        'Acessórios': [
            "Material", "Compatibilidade", "Dimensões", 
            "Peso", "Recursos adicionais", "Garantia"
        ],
        'Casa': [
            "Potência", "Capacidade", "Material", 
            "Dimensões", "Funções", "Eficiência energética"
        ]
    }
    
    # Gerar produtos fictícios
    for i in range(50):
        categoria = random.choice(categorias)
        
        # Selecionar nome de produto aleatório para a categoria
        nome = random.choice(produtos_por_categoria[categoria])
        
        # Adicionar variante ao nome para evitar duplicatas
        variante = random.choice(["Premium", "Plus", "Pro", "Lite", "Max", "Ultra", "2023", "X", "S", ""])
        if variante:
            nome = f"{nome} {variante}"
        
        # Gerar preço e desconto
        preco_original = random.uniform(100, 5000)
        desconto = random.uniform(0, 0.4)
        preco_atual = preco_original * (1 - desconto)
        
        # Selecionar descrição aleatória
        descricao = random.choice(descricoes_por_categoria[categoria])
        
        # Gerar características aleatórias
        num_caracteristicas = random.randint(3, 6)
        caracteristicas_disponiveis = caracteristicas_por_categoria[categoria]
        caracteristicas_selecionadas = random.sample(caracteristicas_disponiveis, min(num_caracteristicas, len(caracteristicas_disponiveis)))
        
        caracteristicas = {}
        for carac in caracteristicas_selecionadas:
            if carac == "Processador":
                caracteristicas[carac] = random.choice(["Intel Core i5", "Intel Core i7", "AMD Ryzen 5", "AMD Ryzen 7", "Apple M1", "Snapdragon 888"])
            elif carac == "Memória RAM":
                caracteristicas[carac] = f"{random.choice([4, 8, 16, 32])}GB"
            elif carac == "Armazenamento" or carac == "Armazenamento SSD/HD":
                caracteristicas[carac] = f"{random.choice([128, 256, 512, 1024])}GB"
            elif carac == "Câmera":
                caracteristicas[carac] = f"{random.choice([12, 16, 32, 48, 64, 108])}MP"
            elif carac == "Bateria":
                caracteristicas[carac] = f"{random.choice([3000, 4000, 5000])}mAh"
            elif carac == "Tela" or carac == "Resolução de tela":
                caracteristicas[carac] = random.choice(["HD", "Full HD", "2K", "4K", "OLED", "AMOLED", "IPS LCD"])
            elif carac == "Sistema operacional":
                caracteristicas[carac] = random.choice(["Windows 11", "macOS", "Android 12", "iOS 15", "Linux"])
            elif carac == "Potência":
                caracteristicas[carac] = f"{random.choice([600, 800, 1000, 1200, 1500, 2000])}W"
            elif carac == "Capacidade":
                caracteristicas[carac] = f"{random.choice([1, 2, 3, 4, 5, 10])} litros"
            elif carac == "Material":
                caracteristicas[carac] = random.choice(["Plástico", "Alumínio", "Aço inox", "Vidro temperado", "Silicone", "Couro sintético"])
            elif carac == "Dimensões":
                caracteristicas[carac] = f"{random.randint(10, 100)}x{random.randint(10, 100)}x{random.randint(1, 30)}cm"
            elif carac == "Peso":
                caracteristicas[carac] = f"{random.uniform(0.1, 5):.1f}kg"
            else:
                caracteristicas[carac] = "Informação não disponível"
        
        # Criar produto
        produto = {
            'id': i + 1,
            'nome': nome,
            'categoria': categoria,
            'preco_atual': round(preco_atual, 2),
            'preco_original': round(preco_original, 2),
            'desconto': round(desconto * 100, 2),
            'avaliacao': round(random.uniform(1, 5), 1),
            'num_avaliacoes': random.randint(0, 1000),
            'descricao': descricao,
            'caracteristicas': caracteristicas,
            'disponivel': random.choice([True, False]),
            'destaque': random.random() < 0.2,  # 20% de chance de ser destaque
            'vendedor': f"Vendedor {random.randint(1, 10)}",
            'data_extracao': datetime.now().strftime('%Y-%m-%d'),
            'imagem': f"produto_{i+1}.jpg"  # Imagem fictícia
        }
        dados.append(produto)
    
    # Salvar dados de exemplo
    caminho_arquivo = os.path.join(DADOS_DIR, 'produtos_exemplo.json')
    with open(caminho_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)
    print(f"Dados de exemplo salvos 
(Content truncated due to size limit. Use line ranges to read in chunks)