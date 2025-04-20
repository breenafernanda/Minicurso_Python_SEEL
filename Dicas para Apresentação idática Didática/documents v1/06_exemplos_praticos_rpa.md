# Exemplos Práticos de Python para RPA

Neste capítulo, vamos explorar exemplos práticos de como usar Python para automação de processos robóticos (RPA). Vamos aplicar os conceitos que aprendemos nos capítulos anteriores para criar soluções de automação que podem ser usadas em ambientes de trabalho reais.

## O que é RPA?

RPA (Robotic Process Automation) é uma tecnologia que permite configurar software para emular e integrar as ações de um ser humano interagindo dentro de sistemas digitais para executar um processo de negócio. Utilizando ferramentas de RPA, uma empresa pode configurar "robôs" de software para capturar e interpretar aplicativos para processar uma transação, manipular dados, disparar respostas e se comunicar com outros sistemas digitais.

Python é uma linguagem excelente para RPA devido à sua simplicidade, legibilidade e ao vasto ecossistema de bibliotecas disponíveis para automação.

## Bibliotecas Python Comuns para RPA

Antes de mergulharmos nos exemplos, vamos conhecer algumas bibliotecas Python populares para RPA:

1. **Selenium**: Automação de navegadores web
2. **PyAutoGUI**: Automação de interface gráfica (controle de mouse e teclado)
3. **Pandas**: Manipulação e análise de dados
4. **openpyxl/xlwings**: Manipulação de planilhas Excel
5. **PyPDF2/pdfplumber**: Manipulação de arquivos PDF
6. **Requests/BeautifulSoup**: Requisições HTTP e web scraping
7. **pywin32**: Automação de aplicativos Windows
8. **schedule**: Agendamento de tarefas
9. **smtplib**: Envio de e-mails
10. **pytesseract**: OCR (Reconhecimento Óptico de Caracteres)

## Exemplo 1: Automação de Navegador Web com Selenium

O Selenium é uma das ferramentas mais populares para automação de navegadores. Vamos criar um exemplo simples que acessa um site, preenche um formulário e extrai informações.

```python
# Exemplo: Automação de pesquisa no Google
# Requisitos: pip install selenium webdriver-manager

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def pesquisar_no_google(termo_pesquisa):
    """
    Realiza uma pesquisa no Google e retorna os títulos dos primeiros resultados.
    
    Parâmetros:
        termo_pesquisa (str): O termo a ser pesquisado
    
    Retorna:
        list: Lista com os títulos dos primeiros resultados
    """
    # Configurar o driver do Chrome
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico)
    
    try:
        # Acessar o Google
        navegador.get("https://www.google.com")
        
        # Encontrar o campo de pesquisa e digitar o termo
        campo_pesquisa = navegador.find_element(By.NAME, "q")
        campo_pesquisa.clear()
        campo_pesquisa.send_keys(termo_pesquisa)
        campo_pesquisa.send_keys(Keys.RETURN)
        
        # Aguardar o carregamento dos resultados
        time.sleep(2)
        
        # Extrair os títulos dos resultados
        resultados = navegador.find_elements(By.CSS_SELECTOR, "h3")
        titulos = [resultado.text for resultado in resultados if resultado.text]
        
        return titulos[:5]  # Retornar os primeiros 5 resultados
    
    finally:
        # Fechar o navegador
        navegador.quit()

# Exemplo de uso
if __name__ == "__main__":
    termo = input("Digite o termo que deseja pesquisar: ")
    resultados = pesquisar_no_google(termo)
    
    print(f"\nResultados da pesquisa para '{termo}':")
    for i, titulo in enumerate(resultados, 1):
        print(f"{i}. {titulo}")
```

### Explicação do Código:

1. Importamos as bibliotecas necessárias do Selenium e webdriver-manager.
2. Criamos uma função `pesquisar_no_google` que:
   - Configura o driver do Chrome usando o webdriver-manager (que gerencia a instalação do driver automaticamente)
   - Acessa o site do Google
   - Localiza o campo de pesquisa, digita o termo e pressiona Enter
   - Aguarda o carregamento dos resultados
   - Extrai os títulos dos resultados usando seletores CSS
   - Fecha o navegador e retorna os resultados
3. No bloco principal, solicitamos um termo de pesquisa ao usuário e exibimos os resultados.

## Exemplo 2: Automação de Interface Gráfica com PyAutoGUI

PyAutoGUI permite controlar o mouse e o teclado para automatizar interações com qualquer aplicativo de desktop.

```python
# Exemplo: Automação de captura de tela e desenho
# Requisitos: pip install pyautogui pillow

import pyautogui
import time
import random

def desenhar_forma():
    """
    Abre o Paint (ou similar) e desenha uma forma simples.
    """
    # Obter o tamanho da tela
    largura_tela, altura_tela = pyautogui.size()
    
    # Abrir o menu Iniciar e procurar pelo Paint
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write('paint')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)  # Aguardar o Paint abrir
    
    # Maximizar a janela
    pyautogui.hotkey('win', 'up')
    time.sleep(1)
    
    # Calcular o centro da tela
    centro_x = largura_tela // 2
    centro_y = altura_tela // 2
    
    # Mover para o centro
    pyautogui.moveTo(centro_x, centro_y, duration=0.5)
    
    # Desenhar uma forma (estrela simples)
    pyautogui.mouseDown()
    for _ in range(5):
        # Mover para criar uma ponta da estrela
        pyautogui.move(100, 0, duration=0.2)
        pyautogui.move(0, 100, duration=0.2)
        pyautogui.move(-100, 0, duration=0.2)
        pyautogui.move(0, -100, duration=0.2)
        
        # Girar para a próxima ponta
        pyautogui.move(20, 20, duration=0.1)
    
    pyautogui.mouseUp()
    
    # Tirar uma captura de tela
    screenshot = pyautogui.screenshot()
    screenshot.save('desenho_automatico.png')
    
    print("Desenho concluído! Captura de tela salva como 'desenho_automatico.png'")
    
    # Opcional: Fechar o Paint (sem salvar)
    time.sleep(2)
    pyautogui.hotkey('alt', 'f4')
    time.sleep(1)
    pyautogui.press('n')  # Não salvar

# Aviso de segurança
print("Este script vai controlar seu mouse e teclado para desenhar no Paint.")
print("Mova o mouse para um canto da tela para interromper a execução em caso de emergência.")
print("Iniciando em 5 segundos...")
time.sleep(5)

# Executar o desenho
try:
    desenhar_forma()
except Exception as e:
    print(f"Erro durante a execução: {e}")
```

### Explicação do Código:

1. Importamos o PyAutoGUI e outras bibliotecas necessárias.
2. Criamos uma função `desenhar_forma` que:
   - Obtém o tamanho da tela
   - Abre o Paint através do menu Iniciar
   - Maximiza a janela
   - Move o mouse para o centro da tela
   - Desenha uma forma simples controlando o mouse
   - Captura a tela e salva como imagem
   - Fecha o Paint
3. Adicionamos um aviso de segurança e um atraso antes de iniciar a automação.

**Observação de Segurança**: O PyAutoGUI tem uma função de segurança - se você mover o mouse para um dos cantos da tela, ele interromperá a execução do script.

## Exemplo 3: Manipulação de Planilhas Excel

Automatizar tarefas com planilhas Excel é um caso de uso comum para RPA. Vamos criar um exemplo que lê dados de uma planilha, processa-os e gera um relatório.

```python
# Exemplo: Processamento de dados de vendas em Excel
# Requisitos: pip install pandas openpyxl matplotlib

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

def processar_dados_vendas(arquivo_entrada, diretorio_saida):
    """
    Processa dados de vendas de uma planilha Excel e gera relatórios.
    
    Parâmetros:
        arquivo_entrada (str): Caminho para o arquivo Excel de entrada
        diretorio_saida (str): Diretório onde os relatórios serão salvos
    """
    # Criar o diretório de saída se não existir
    if not os.path.exists(diretorio_saida):
        os.makedirs(diretorio_saida)
    
    # Ler a planilha Excel
    print(f"Lendo dados de {arquivo_entrada}...")
    df = pd.read_excel(arquivo_entrada)
    
    # Exibir informações básicas
    print(f"Total de registros: {len(df)}")
    print(f"Colunas disponíveis: {', '.join(df.columns)}")
    
    # Processar os dados
    # 1. Calcular vendas totais por produto
    vendas_por_produto = df.groupby('Produto')['Valor'].sum().sort_values(ascending=False)
    
    # 2. Calcular vendas totais por mês
    df['Data'] = pd.to_datetime(df['Data'])
    df['Mês'] = df['Data'].dt.strftime('%Y-%m')
    vendas_por_mes = df.groupby('Mês')['Valor'].sum()
    
    # 3. Identificar os melhores vendedores
    vendas_por_vendedor = df.groupby('Vendedor')['Valor'].sum().sort_values(ascending=False)
    
    # Gerar relatório em Excel
    nome_arquivo = os.path.join(diretorio_saida, 'relatorio_vendas.xlsx')
    with pd.ExcelWriter(nome_arquivo) as writer:
        vendas_por_produto.to_excel(writer, sheet_name='Vendas por Produto')
        vendas_por_mes.to_excel(writer, sheet_name='Vendas por Mês')
        vendas_por_vendedor.to_excel(writer, sheet_name='Vendas por Vendedor')
        
        # Adicionar uma planilha de resumo
        resumo = pd.DataFrame({
            'Métrica': ['Total de Vendas', 'Média por Venda', 'Produto Mais Vendido', 'Melhor Vendedor'],
            'Valor': [
                f"R$ {df['Valor'].sum():.2f}",
                f"R$ {df['Valor'].mean():.2f}",
                vendas_por_produto.index[0],
                vendas_por_vendedor.index[0]
            ]
        })
        resumo.to_excel(writer, sheet_name='Resumo', index=False)
    
    print(f"Relatório Excel gerado: {nome_arquivo}")
    
    # Gerar gráficos
    # 1. Gráfico de barras para vendas por produto (top 5)
    plt.figure(figsize=(10, 6))
    vendas_por_produto.head(5).plot(kind='bar')
    plt.title('Top 5 Produtos Mais Vendidos')
    plt.xlabel('Produto')
    plt.ylabel('Valor Total (R$)')
    plt.tight_layout()
    plt.savefig(os.path.join(diretorio_saida, 'grafico_produtos.png'))
    
    # 2. Gráfico de linha para vendas por mês
    plt.figure(figsize=(10, 6))
    vendas_por_mes.plot(kind='line', marker='o')
    plt.title('Vendas por Mês')
    plt.xlabel('Mês')
    plt.ylabel('Valor Total (R$)')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(diretorio_saida, 'grafico_vendas_mensais.png'))
    
    print(f"Gráficos gerados no diretório: {diretorio_saida}")
    
    return {
        'total_vendas': df['Valor'].sum(),
        'produto_mais_vendido': vendas_por_produto.index[0],
        'melhor_vendedor': vendas_por_vendedor.index[0]
    }

# Exemplo de uso
if __name__ == "__main__":
    # Em um cenário real, você teria um arquivo Excel existente
    # Para este exemplo, vamos criar um arquivo de demonstração
    
    # Criar dados de exemplo
    dados = {
        'Data': pd.date_range(start='2023-01-01', periods=100),
        'Produto': ['Produto A', 'Produto B', 'Produto C', 'Produto D', 'Produto E'] * 20,
        'Vendedor': ['João', 'Maria', 'Pedro', 'Ana', 'Carlos'] * 20,
        'Quantidade': [round(pd.np.random.randint(1, 10)) for _ in range(100)],
        'Valor': [round(pd.np.random.uniform(50, 500), 2) for _ in range(100)]
    }
    
    df_exemplo = pd.DataFrame(dados)
    
    # Salvar dados de exemplo
    arquivo_exemplo = 'dados_vendas_exemplo.xlsx'
    df_exemplo.to_excel(arquivo_exemplo, index=False)
    print(f"Arquivo de exemplo criado: {arquivo_exemplo}")
    
    # Processar os dados
    diretorio_relatorios = 'relatorios_vendas'
    resultados = processar_dados_vendas(arquivo_exemplo, diretorio_relatorios)
    
    # Exibir resultados
    print("\nResumo dos Resultados:")
    print(f"Total de Vendas: R$ {resultados['total_vendas']:.2f}")
    print(f"Produto Mais Vendido: {resultados['produto_mais_vendido']}")
    print(f"Melhor Vendedor: {resultados['melhor_vendedor']}")
```

### Explicação do Código:

1. Importamos as bibliotecas necessárias: pandas para manipulação de dados, matplotlib para visualização e outras utilidades.
2. Criamos uma função `processar_dados_vendas` que:
   - Lê dados de uma planilha Excel
   - Processa os dados para extrair informações úteis (vendas por produto, por mês, por vendedor)
   - Gera um relatório Excel com várias planilhas
   - Cria gráficos para visualização dos dados
3. No bloco principal, criamos dados de exemplo, salvamos em um arquivo Excel e processamos esses dados.

## Exemplo 4: Web Scraping com Requests e BeautifulSoup

Web scraping é uma técnica comum em RPA para extrair dados de sites. Vamos criar um exemplo que extrai informações de um site de notícias.

```python
# Exemplo: Extração de notícias
# Requisitos: pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import time
import random

def extrair_noticias(url, num_paginas=1):
    """
    Extrai notícias de um site.
    
    Parâmetros:
        url (str): URL do site de notícias
        num_paginas (int): Número de páginas a serem extraídas
    
    Retorna:
        list: Lista de dicionários com as notícias extraídas
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    todas_noticias = []
    
    for pagina in range(1, num_paginas + 1):
        # Construir a URL da página (ajuste conforme o site alvo)
        if pagina == 1:
            pagina_url = url
        else:
            pagina_url = f"{url}/page/{pagina}"
        
        print(f"Extraindo dados da página {pagina}: {pagina_url}")
        
        try:
            # Fazer a requisição HTTP
            response = requests.get(pagina_url, headers=headers)
            response.raise_for_status()  # Verificar se a requisição foi bem-sucedida
            
            # Parsear o HTML
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Encontrar os elementos das notícias (ajuste os seletores conforme o site alvo)
            # Exemplo para um site genérico:
            artigos = soup.find_all('article')
            
            for artigo in artigos:
                try:
                    # Extrair informações (ajuste os seletores conforme o site alvo)
                    titulo_elem = artigo.find('h2')
                    link_elem = artigo.find('a')
                    resumo_elem = artigo.find('p', class_='excerpt')
                    data_elem = artigo.find('time')
                    
                    titulo = titulo_elem.text.strip() if titulo_elem else "Sem título"
                    link = link_elem['href'] if link_elem and 'href' in link_elem.attrs else ""
                    resumo = resumo_elem.text.strip() if resumo_elem else "Sem resumo"
                    data_publicacao = data_elem.text.strip() if data_elem else "Data desconhecida"
                    
                    # Armazenar os dados
                    noticia = {
                        'titulo': titulo,
                        'link': link,
                        'resumo': resumo,
                        'data_publicacao': data_publicacao,
                        'data_extracao': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    }
                    
                    todas_noticias.append(noticia)
                    
                except Exception as e:
                    print(f"Erro ao processar um artigo: {e}")
            
            # Pausa para não sobrecarregar o servidor
            time.sleep(random.uniform(1, 3))
            
        except Exception as e:
            print(f"Erro ao processar a página {pagina}: {e}")
    
    print(f"Total de notícias extraídas: {len(todas_noticias)}")
    return todas_noticias

def salvar_noticias_csv(noticias, nome_arquivo):
    """
    Salva as notícias extraídas em um arquivo CSV.
    
    Parâmetros:
        noticias (list): Lista de dicionários com as notícias
        nome_arquivo (str): Nome do arquivo CSV de
(Content truncated due to size limit. Use line ranges to read in chunks)