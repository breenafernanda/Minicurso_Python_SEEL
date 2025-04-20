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

if __name__ == "__main__":
    # Verificar diretório atual
    diretorio_atual = os.getcwd()
    print(f"Diretório atual: {diretorio_atual}")
    
    # Criar arquivos auxiliares
    criar_config()
    criar_requirements()
    
    print("Todos os arquivos auxiliares foram criados com sucesso.")
