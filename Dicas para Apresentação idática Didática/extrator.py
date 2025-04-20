import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configurações
SITES = {
    'amazon': {
        'url': 'https://www.amazon.com.br/deals',
        'seletores': {
            'produtos': '.a-section.octopus-dlp-asin-section',
            'titulo': '.a-size-base-plus',
            'preco_atual': '.a-price-whole',
            'preco_antigo': '.a-text-price .a-offscreen',
            'imagem': '.octopus-dlp-asin-image img',
            'link': 'a.a-link-normal'
        }
    },
    'mercadolivre': {
        'url': 'https://www.mercadolivre.com.br/ofertas',
        'seletores': {
            'produtos': '.promotion-item',
            'titulo': '.promotion-item__title',
            'preco_atual': '.andes-money-amount__fraction',
            'preco_antigo': '.andes-money-amount--previous .andes-money-amount__fraction',
            'imagem': '.promotion-item__img-container img',
            'link': '.promotion-item__link-container'
        }
    }
}

def inicializar_driver():
    """Inicializa e retorna o driver do Selenium."""
    print("Inicializando o driver do Selenium...")
    options = Options()
    options.add_argument("--headless")  # Modo invisível
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def extrair_dados_site(driver, site_nome, config):
    """Extrai dados de produtos em promoção de um site específico."""
    print(f"Extraindo dados do site {site_nome}...")
    
    # Navegar para a URL
    driver.get(config['url'])
    print(f"Navegando para {config['url']}...")
    
    # Aguardar carregamento da página
    time.sleep(5)
    
    # Localizar elementos de produtos
    produtos_elementos = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, config['seletores']['produtos']))
    )
    
    print(f"Encontrados {len(produtos_elementos)} produtos em {site_nome}")
    
    dados_produtos = []
    
    # Extrair dados de cada produto
    for produto in produtos_elementos[:10]:  # Limitar a 10 produtos para exemplo
        try:
            # Extrair título
            titulo_elemento = produto.find_element(By.CSS_SELECTOR, config['seletores']['titulo'])
            titulo = titulo_elemento.text.strip()
            
            # Extrair preço atual
            preco_atual_elemento = produto.find_element(By.CSS_SELECTOR, config['seletores']['preco_atual'])
            preco_atual = preco_atual_elemento.text.strip().replace('.', '').replace(',', '.')
            
            # Extrair preço antigo (pode não existir)
            try:
                preco_antigo_elemento = produto.find_element(By.CSS_SELECTOR, config['seletores']['preco_antigo'])
                preco_antigo = preco_antigo_elemento.text.strip().replace('R$', '').replace('.', '').replace(',', '.').strip()
            except:
                preco_antigo = None
            
            # Extrair URL da imagem
            imagem_elemento = produto.find_element(By.CSS_SELECTOR, config['seletores']['imagem'])
            imagem_url = imagem_elemento.get_attribute('src')
            
            # Extrair link do produto
            link_elemento = produto.find_element(By.CSS_SELECTOR, config['seletores']['link'])
            link = link_elemento.get_attribute('href')
            
            # Calcular desconto
            if preco_antigo and preco_antigo != '':
                try:
                    desconto = round((1 - float(preco_atual) / float(preco_antigo)) * 100, 2)
                except:
                    desconto = None
            else:
                desconto = None
            
            # Adicionar dados ao array
            dados_produtos.append({
                'site': site_nome,
                'titulo': titulo,
                'preco_atual': float(preco_atual) if preco_atual else None,
                'preco_antigo': float(preco_antigo) if preco_antigo else None,
                'desconto': desconto,
                'imagem_url': imagem_url,
                'link': link
            })
            
        except Exception as e:
            print(f"Erro ao extrair dados de um produto: {e}")
            continue
    
    return dados_produtos

def extrair_todos_dados():
    """Extrai dados de todos os sites configurados."""
    driver = inicializar_driver()
    todos_dados = []
    
    try:
        for site_nome, config in SITES.items():
            dados_site = extrair_dados_site(driver, site_nome, config)
            todos_dados.extend(dados_site)
    finally:
        driver.quit()
    
    # Converter para DataFrame
    df = pd.DataFrame(todos_dados)
    
    # Salvar dados brutos
    os.makedirs('dados', exist_ok=True)
    df.to_csv('dados/produtos_extraidos.csv', index=False)
    
    print(f"Extração concluída. Total de {len(df)} produtos extraídos.")
    return df

if __name__ == "__main__":
    extrair_todos_dados()
