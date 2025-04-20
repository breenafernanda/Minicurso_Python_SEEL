import os
import sys

def criar_config():
    """Cria o arquivo de configuração do projeto."""
    conteudo = """# Configurações do Projeto Integrador

# Sites para extração de dados
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

# Configurações de extração
EXTRACAO = {
    'max_produtos_por_site': 10,
    'timeout_padrao': 10,
    'modo_headless': True,
    'tentativas_maximas': 3
}

# Configurações de processamento
PROCESSAMENTO = {
    'desconto_minimo': 10.0,  # Percentual mínimo de desconto para considerar uma boa oferta
    'categorias_interesse': [],  # Deixar vazio para considerar todas as categorias
    'ordenar_por': 'desconto'  # Opções: 'desconto', 'economia', 'preco_atual'
}

# Configurações de relatórios
RELATORIOS = {
    'incluir_graficos': True,
    'formato_excel': True,
    'formato_pdf': True,
    'diretorio_saida': 'output/'
}

# Configurações de notificação (para futuras implementações)
NOTIFICACOES = {
    'enviar_email': False,
    'email_destinatario': '',
    'assunto_email': 'Relatório de Ofertas',
    'mensagem_email': 'Segue em anexo o relatório de ofertas gerado automaticamente.'
}
"""
    
    with open('config.py', 'w') as f:
        f.write(conteudo)
    
    print("Arquivo de configuração criado com sucesso.")

def criar_requirements():
    """Cria o arquivo de requisitos do projeto."""
    conteudo = """# Requisitos do Projeto Integrador

# Bibliotecas principais
selenium==4.10.0
pandas==2.0.3
openpyxl==3.1.2
reportlab==3.6.13
pillow==10.0.0
requests==2.31.0
matplotlib==3.7.2

# Bibliotecas auxiliares
beautifulsoup4==4.12.2
webdriver-manager==3.8.6
numpy==1.24.3
"""
    
    with open('requirements.txt', 'w') as f:
        f.write(conteudo)
    
    print("Arquivo de requisitos criado com sucesso.")

def criar_utils():
    """Cria o arquivo de utilidades do projeto."""
    conteudo = """import os
import logging
import requests
from io import BytesIO
from PIL import Image
import re

def configurar_logger(nome, arquivo_log=None):
    """Configura e retorna um logger."""
    logger = logging.getLogger(nome)
    logger.setLevel(logging.INFO)
    
    # Formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # File Handler (opcional)
    if arquivo_log:
        os.makedirs(os.path.dirname(arquivo_log), exist_ok=True)
        file_handler = logging.FileHandler(arquivo_log)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger

def baixar_imagem(url, diretorio_destino, nome_arquivo, tamanho_max=None):
    """
    Baixa uma imagem da web e salva no diretório especificado.
    
    Args:
        url: URL da imagem
        diretorio_destino: Diretório onde a imagem será salva
        nome_arquivo: Nome do arquivo (sem extensão)
        tamanho_max: Tupla (largura, altura) para redimensionar a imagem
        
    Returns:
        Caminho completo da imagem salva ou None em caso de erro
    """
    try:
        # Criar diretório se não existir
        os.makedirs(diretorio_destino, exist_ok=True)
        
        # Baixar imagem
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Determinar extensão
        content_type = response.headers.get('Content-Type', '')
        if 'jpeg' in content_type or 'jpg' in content_type:
            extensao = 'jpg'
        elif 'png' in content_type:
            extensao = 'png'
        elif 'gif' in content_type:
            extensao = 'gif'
        elif 'webp' in content_type:
            extensao = 'webp'
        else:
            extensao = 'jpg'  # Padrão
        
        # Caminho completo
        caminho_completo = os.path.join(diretorio_destino, f"{nome_arquivo}.{extensao}")
        
        # Processar imagem
        img = Image.open(BytesIO(response.content))
        
        # Redimensionar se necessário
        if tamanho_max and (img.width > tamanho_max[0] or img.height > tamanho_max[1]):
            img.thumbnail(tamanho_max)
        
        # Salvar imagem
        img.save(caminho_completo)
        
        return caminho_completo
    except Exception as e:
        print(f"Erro ao baixar imagem {url}: {e}")
        return None

def limpar_texto(texto):
    """Remove caracteres especiais e formata o texto."""
    if not texto:
        return ""
    
    # Remover tags HTML
    texto = re.sub(r'<[^>]+>', '', texto)
    
    # Remover espaços extras
    texto = re.sub(r'\\s+', ' ', texto)
    
    # Remover caracteres especiais
    texto = re.sub(r'[^\\w\\s\\-.,;:!?()]', '', texto)
    
    return texto.strip()

def formatar_preco(valor):
    """Formata um valor numérico como preço."""
    if valor is None:
        return "N/A"
    
    try:
        return f"R$ {float(valor):.2f}".replace('.', ',')
    except (ValueError, TypeError):
        return str(valor)

def calcular_desconto(preco_atual, preco_antigo):
    """Calcula o percentual de desconto entre dois preços."""
    try:
        preco_atual = float(preco_atual)
        preco_antigo = float(preco_antigo)
        
        if preco_antigo <= 0 or preco_atual <= 0:
            return None
        
        desconto = (1 - preco_atual / preco_antigo) * 100
        return round(desconto, 2)
    except (ValueError, TypeError, ZeroDivisionError):
        return None

def gerar_nome_arquivo_seguro(texto):
    """Gera um nome de arquivo seguro a partir de um texto."""
    # Remover caracteres não permitidos em nomes de arquivo
    nome_seguro = re.sub(r'[^\\w\\-.]', '_', texto)
    
    # Limitar tamanho
    if len(nome_seguro) > 50:
        nome_seguro = nome_seguro[:50]
    
    return nome_seguro
"""
    
    with open('utils.py', 'w') as f:
        f.write(conteudo)
    
    print("Arquivo de utilidades criado com sucesso.")

if __name__ == "__main__":
    # Verificar diretório atual
    diretorio_atual = os.getcwd()
    print(f"Diretório atual: {diretorio_atual}")
    
    # Criar arquivos auxiliares
    criar_config()
    criar_requirements()
    criar_utils()
    
    print("Todos os arquivos auxiliares foram criados com sucesso.")
