# Exercícios Práticos: Selenium para Automação Web

## Exercício 1: Extração de Dados de um E-commerce

### Objetivo
Praticar a extração de dados de produtos de um site de e-commerce usando Selenium.

### Enunciado
Você precisa criar um script que acesse um site de e-commerce e extraia informações sobre produtos em promoção. Sua tarefa é:
1. Acessar a página principal do site
2. Navegar até a seção de ofertas/promoções
3. Extrair informações de pelo menos 5 produtos (nome, preço original, preço com desconto, porcentagem de desconto)
4. Salvar os dados em um arquivo CSV

### Modelo de Solução
```python
# Solução do Exercício 1

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import csv
import time
import re

# Configurar o driver
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
# options.add_argument("--headless")  # Descomente para executar em modo headless

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# URL do site (usando o Magazine Luiza como exemplo)
url = "https://www.magazineluiza.com.br/"

try:
    # Acessar o site
    print("Acessando o site...")
    driver.get(url)
    
    # Aguardar carregamento da página
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    
    # Navegar para a seção de ofertas
    print("Navegando para a seção de ofertas...")
    ofertas_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Ofertas') or contains(@href, 'ofertas')]"))
    )
    ofertas_link.click()
    
    # Aguardar carregamento da página de ofertas
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-testid='product-card']"))
    )
    
    # Extrair informações dos produtos
    print("Extraindo informações dos produtos...")
    produtos = []
    
    # Encontrar cards de produtos
    cards = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[data-testid='product-card']"))
    )
    
    # Limitar a 5 produtos ou menos
    cards = cards[:5]
    
    for card in cards:
        try:
            # Extrair nome do produto
            nome = card.find_element(By.CSS_SELECTOR, "h2[data-testid='product-title']").text
            
            # Extrair preço original (pode estar em diferentes formatos)
            try:
                preco_original_elem = card.find_element(By.CSS_SELECTOR, "p[data-testid='price-original']")
                preco_original_texto = preco_original_elem.text
            except:
                preco_original_texto = "N/A"
            
            # Extrair preço com desconto
            try:
                preco_atual_elem = card.find_element(By.CSS_SELECTOR, "p[data-testid='price-value']")
                preco_atual_texto = preco_atual_elem.text
            except:
                preco_atual_texto = "N/A"
            
            # Extrair porcentagem de desconto
            try:
                desconto_elem = card.find_element(By.CSS_SELECTOR, "p[data-testid='discount-percentage']")
                desconto_texto = desconto_elem.text
            except:
                desconto_texto = "N/A"
            
            # Processar textos para extrair valores numéricos
            preco_original = re.sub(r'[^\d,]', '', preco_original_texto).replace(',', '.')
            preco_atual = re.sub(r'[^\d,]', '', preco_atual_texto).replace(',', '.')
            desconto = re.sub(r'[^\d]', '', desconto_texto)
            
            # Adicionar à lista de produtos
            produtos.append({
                'nome': nome,
                'preco_original': preco_original_texto,
                'preco_atual': preco_atual_texto,
                'desconto': desconto_texto
            })
            
            print(f"Produto extraído: {nome}")
        
        except Exception as e:
            print(f"Erro ao extrair produto: {str(e)}")
    
    # Salvar dados em CSV
    print("Salvando dados em CSV...")
    with open('produtos_promocao.csv', 'w', newline='', encoding='utf-8') as arquivo:
        campos = ['nome', 'preco_original', 'preco_atual', 'desconto']
        writer = csv.DictWriter(arquivo, fieldnames=campos)
        
        writer.writeheader()
        for produto in produtos:
            writer.writerow(produto)
    
    print(f"Extração concluída! {len(produtos)} produtos extraídos e salvos em 'produtos_promocao.csv'")

except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")

finally:
    # Fechar o navegador
    driver.quit()
```

## Exercício 2: Automação de Formulário

### Objetivo
Praticar a interação com formulários web usando Selenium.

### Enunciado
Você precisa criar um script que preencha automaticamente um formulário de cadastro em um site. Sua tarefa é:
1. Acessar a página do formulário
2. Preencher todos os campos obrigatórios com dados fictícios
3. Enviar o formulário
4. Verificar se o cadastro foi realizado com sucesso

### Modelo de Solução
```python
# Solução do Exercício 2

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

# Configurar o driver
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# URL do formulário (usando um site de exemplo)
url = "https://www.fakeformfiller.com/"  # Substitua por um site real de formulário

# Dados fictícios para preenchimento
dados_cadastro = {
    "nome": "João Silva",
    "email": f"joao.silva{random.randint(1000, 9999)}@email.com",
    "telefone": f"(11) 9{random.randint(1000, 9999)}-{random.randint(1000, 9999)}",
    "cpf": f"{random.randint(100, 999)}.{random.randint(100, 999)}.{random.randint(100, 999)}-{random.randint(10, 99)}",
    "endereco": "Rua das Flores, 123",
    "cidade": "São Paulo",
    "estado": "SP",
    "cep": f"{random.randint(10000, 99999)}-{random.randint(100, 999)}",
    "senha": f"Senha{random.randint(100, 999)}!"
}

try:
    # Acessar o site
    print("Acessando o formulário...")
    driver.get(url)
    
    # Aguardar carregamento da página
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    
    # Preencher o formulário
    print("Preenchendo o formulário...")
    
    # Nome
    try:
        campo_nome = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "name"))
        )
        campo_nome.send_keys(dados_cadastro["nome"])
    except:
        try:
            campo_nome = driver.find_element(By.NAME, "name")
            campo_nome.send_keys(dados_cadastro["nome"])
        except:
            print("Campo nome não encontrado")
    
    # Email
    try:
        campo_email = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        campo_email.send_keys(dados_cadastro["email"])
    except:
        try:
            campo_email = driver.find_element(By.NAME, "email")
            campo_email.send_keys(dados_cadastro["email"])
        except:
            print("Campo email não encontrado")
    
    # Telefone
    try:
        campo_telefone = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "phone"))
        )
        campo_telefone.send_keys(dados_cadastro["telefone"])
    except:
        try:
            campo_telefone = driver.find_element(By.NAME, "phone")
            campo_telefone.send_keys(dados_cadastro["telefone"])
        except:
            print("Campo telefone não encontrado")
    
    # CPF
    try:
        campo_cpf = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "cpf"))
        )
        campo_cpf.send_keys(dados_cadastro["cpf"])
    except:
        try:
            campo_cpf = driver.find_element(By.NAME, "cpf")
            campo_cpf.send_keys(dados_cadastro["cpf"])
        except:
            print("Campo CPF não encontrado")
    
    # Endereço
    try:
        campo_endereco = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "address"))
        )
        campo_endereco.send_keys(dados_cadastro["endereco"])
    except:
        try:
            campo_endereco = driver.find_element(By.NAME, "address")
            campo_endereco.send_keys(dados_cadastro["endereco"])
        except:
            print("Campo endereço não encontrado")
    
    # Cidade
    try:
        campo_cidade = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "city"))
        )
        campo_cidade.send_keys(dados_cadastro["cidade"])
    except:
        try:
            campo_cidade = driver.find_element(By.NAME, "city")
            campo_cidade.send_keys(dados_cadastro["cidade"])
        except:
            print("Campo cidade não encontrado")
    
    # Estado (select)
    try:
        select_estado = Select(driver.find_element(By.ID, "state"))
        select_estado.select_by_value(dados_cadastro["estado"])
    except:
        try:
            select_estado = Select(driver.find_element(By.NAME, "state"))
            select_estado.select_by_value(dados_cadastro["estado"])
        except:
            print("Campo estado não encontrado")
    
    # CEP
    try:
        campo_cep = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "zip"))
        )
        campo_cep.send_keys(dados_cadastro["cep"])
    except:
        try:
            campo_cep = driver.find_element(By.NAME, "zip")
            campo_cep.send_keys(dados_cadastro["cep"])
        except:
            print("Campo CEP não encontrado")
    
    # Senha
    try:
        campo_senha = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        campo_senha.send_keys(dados_cadastro["senha"])
    except:
        try:
            campo_senha = driver.find_element(By.NAME, "password")
            campo_senha.send_keys(dados_cadastro["senha"])
        except:
            print("Campo senha não encontrado")
    
    # Confirmar senha
    try:
        campo_confirmar_senha = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "confirm_password"))
        )
        campo_confirmar_senha.send_keys(dados_cadastro["senha"])
    except:
        try:
            campo_confirmar_senha = driver.find_element(By.NAME, "confirm_password")
            campo_confirmar_senha.send_keys(dados_cadastro["senha"])
        except:
            print("Campo confirmar senha não encontrado")
    
    # Aceitar termos (checkbox)
    try:
        checkbox_termos = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "terms"))
        )
        if not checkbox_termos.is_selected():
            checkbox_termos.click()
    except:
        try:
            checkbox_termos = driver.find_element(By.NAME, "terms")
            if not checkbox_termos.is_selected():
                checkbox_termos.click()
        except:
            print("Checkbox de termos não encontrado")
    
    # Enviar formulário
    print("Enviando formulário...")
    try:
        botao_enviar = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        botao_enviar.click()
    except:
        try:
            botao_enviar = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
            botao_enviar.click()
        except:
            print("Botão de envio não encontrado")
    
    # Verificar sucesso
    print("Verificando resultado...")
    try:
        mensagem_sucesso = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'sucesso') or contains(text(), 'cadastrado')]"))
        )
        print("Cadastro realizado com sucesso!")
        print(f"Mensagem: {mensagem_sucesso.text}")
    except:
        print("Não foi possível confirmar o sucesso do cadastro.")
    
    # Tirar screenshot da página de resultado
    driver.save_screenshot("resultado_cadastro.png")
    print("Screenshot salvo como 'resultado_cadastro.png'")

except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")

finally:
    # Aguardar um pouco para visualizar o resultado
    time.sleep(5)
    
    # Fechar o navegador
    driver.quit()
```

## Exercício 3: Web Scraping de Notícias

### Objetivo
Praticar a extração de conteúdo de múltiplas páginas e navegação entre elas.

### Enunciado
Você precisa criar um script que extraia as últimas notícias de um portal de notícias. Sua tarefa é:
1. Acessar a página principal do portal
2. Extrair os títulos, resumos e links das notícias em destaque
3. Acessar cada link de notícia e extrair o conteúdo completo
4. Salvar todas as informações em um arquivo JSON

### Modelo de Solução
```python
# Solução do Exercício 3

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import json
import time
from datetime import datetime

# Configurar o driver
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
# options.add_argument("--headless")  # Descomente para executar em modo headless

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# URL do portal de notícias (usando G1 como exemplo)
url = "https://g1.globo.com/"

# Lista para armazenar as notícias
noticias = []

try:
    # Acessar o site
    print("Acessando o portal de notícias...")
    driver.get(url)
    
    # Aguardar carregamento da página
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    
    # Extrair notícias em destaque
    print("Extraindo notícias em destaque...")
    
    # Encontrar elementos de notícia
    elementos_noticia = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".feed-post-body"))
    )
    
    # Limitar a 5 notícias para o exemplo
    elementos_noticia = elementos_noticia[:5]
    
    # Extrair informações básicas e links
    for elemento in elementos_noticia:
        try:
            # Extrair título
            titulo_elemento = elemento.find_element(By.CSS_SELECTOR, ".feed-post-body-title")
            titulo = titulo_elemento.text
            
            # Extrair resumo (se disponível)
            try:
                resumo_elemento = elemento.find_element(By.CSS_SELECTOR, ".feed-post-body-resumo")
                resumo = resumo_elemento.text
            except:
                resumo = "Resumo não disponível"
            
            # Extrair link
            link_elemento = elemento.find_element(By.CSS_SELECTOR, "a")
            link = link_elemento.get_attribute("href")
            
            # Adicionar à lista de notícias
            noticia = 
(Content truncated due to size limit. Use line ranges to read in chunks)