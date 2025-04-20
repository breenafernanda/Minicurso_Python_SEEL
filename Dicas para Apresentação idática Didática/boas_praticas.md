# Boas Práticas de Automação com Python

Este guia apresenta as melhores práticas para desenvolvimento de scripts de automação com Python, ajudando você a criar soluções mais robustas, eficientes e fáceis de manter.

## Estrutura de Código

### 1. Organização de Arquivos

Mantenha seus projetos de automação organizados seguindo uma estrutura clara:

```
projeto_automacao/
├── README.md                # Documentação do projeto
├── requirements.txt         # Dependências do projeto
├── config/                  # Arquivos de configuração
│   ├── config.ini
│   └── credentials.json
├── data/                    # Dados de entrada/saída
│   ├── input/
│   └── output/
├── logs/                    # Arquivos de log
├── scripts/                 # Scripts principais
│   ├── main.py
│   ├── web_scraper.py
│   └── data_processor.py
├── utils/                   # Funções utilitárias
│   ├── __init__.py
│   ├── helpers.py
│   └── validators.py
└── tests/                   # Testes automatizados
    ├── test_web_scraper.py
    └── test_data_processor.py
```

### 2. Modularização

Divida seu código em módulos com responsabilidades específicas:

```python
# web_scraper.py
def extract_data_from_website(url):
    """Extrai dados de um site específico."""
    # Implementação...
    return data

# data_processor.py
def process_data(data):
    """Processa os dados extraídos."""
    # Implementação...
    return processed_data

# main.py
from scripts.web_scraper import extract_data_from_website
from scripts.data_processor import process_data

def main():
    url = "https://exemplo.com"
    raw_data = extract_data_from_website(url)
    processed_data = process_data(raw_data)
    # Salvar ou utilizar os dados processados...

if __name__ == "__main__":
    main()
```

### 3. Funções e Classes

- **Funções**: Crie funções pequenas e focadas que façam apenas uma coisa
- **Classes**: Use classes para agrupar funcionalidades relacionadas

```python
class WebScraper:
    def __init__(self, base_url, timeout=30):
        self.base_url = base_url
        self.timeout = timeout
        self.session = self._create_session()
    
    def _create_session(self):
        """Cria uma sessão HTTP reutilizável."""
        # Implementação...
        
    def get_page(self, path):
        """Obtém uma página específica."""
        # Implementação...
        
    def extract_data(self, selector):
        """Extrai dados usando um seletor CSS."""
        # Implementação...
```

## Tratamento de Erros

### 1. Use Try-Except de Forma Específica

Capture exceções específicas em vez de usar blocos genéricos:

```python
# Ruim
try:
    data = process_data(raw_input)
except Exception as e:
    print(f"Erro: {e}")

# Bom
try:
    data = process_data(raw_input)
except ValueError as e:
    print(f"Erro de valor: {e}")
except FileNotFoundError as e:
    print(f"Arquivo não encontrado: {e}")
except Exception as e:
    print(f"Erro inesperado: {e}")
    # Registrar o erro detalhado em log
```

### 2. Implemente Retentativas

Para operações que podem falhar temporariamente (como requisições web):

```python
import time
from requests.exceptions import RequestException

def request_with_retry(url, max_retries=3, delay=2):
    """Faz uma requisição com retentativas em caso de falha."""
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response
        except RequestException as e:
            if attempt == max_retries - 1:
                raise
            print(f"Tentativa {attempt + 1} falhou: {e}. Tentando novamente em {delay} segundos...")
            time.sleep(delay)
            delay *= 2  # Backoff exponencial
```

### 3. Validação de Entrada

Sempre valide os dados de entrada antes de processá-los:

```python
def process_user_data(user_data):
    """Processa dados do usuário após validação."""
    # Validar dados de entrada
    if not isinstance(user_data, dict):
        raise TypeError("user_data deve ser um dicionário")
    
    required_fields = ["name", "email", "age"]
    for field in required_fields:
        if field not in user_data:
            raise ValueError(f"Campo obrigatório ausente: {field}")
    
    if not isinstance(user_data["age"], int) or user_data["age"] < 0:
        raise ValueError("Idade deve ser um número inteiro positivo")
    
    # Processar dados validados...
```

## Logging e Monitoramento

### 1. Configure Logging Adequado

Use o módulo `logging` em vez de `print`:

```python
import logging

# Configuração básica de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("logs/automation.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("automacao")

def process_data(data):
    logger.info(f"Iniciando processamento de {len(data)} itens")
    try:
        # Processamento...
        logger.info("Processamento concluído com sucesso")
    except Exception as e:
        logger.error(f"Erro durante processamento: {e}", exc_info=True)
        raise
```

### 2. Monitore o Desempenho

Acompanhe o tempo de execução das operações críticas:

```python
import time
from functools import wraps

def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logger.info(f"{func.__name__} executado em {end_time - start_time:.2f} segundos")
        return result
    return wrapper

@timing_decorator
def extract_large_dataset(url):
    # Implementação...
    return data
```

## Automação Web com Selenium

### 1. Use Esperas Explícitas

Evite `time.sleep()` fixo e use esperas explícitas:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://exemplo.com")

# Ruim
time.sleep(5)  # Espera fixa de 5 segundos
button = driver.find_element(By.ID, "submit-button")

# Bom
wait = WebDriverWait(driver, 10)
button = wait.until(EC.element_to_be_clickable((By.ID, "submit-button")))
button.click()
```

### 2. Implemente Padrão Page Object

Organize seu código Selenium usando o padrão Page Object:

```python
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://exemplo.com/login"
    
    def navigate(self):
        self.driver.get(self.url)
        return self
    
    def enter_username(self, username):
        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        username_field.clear()
        username_field.send_keys(username)
        return self
    
    def enter_password(self, password):
        password_field = self.driver.find_element(By.ID, "password")
        password_field.clear()
        password_field.send_keys(password)
        return self
    
    def click_login(self):
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()
        return DashboardPage(self.driver)

# Uso
login_page = LoginPage(driver)
dashboard_page = login_page.navigate().enter_username("user").enter_password("pass").click_login()
```

### 3. Lide com Popups e Frames

Gerencie adequadamente popups, alertas e frames:

```python
# Lidar com alertas
try:
    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert_text = alert.text
    alert.accept()  # ou alert.dismiss()
except TimeoutException:
    print("Nenhum alerta encontrado")

# Lidar com frames
driver.switch_to.frame("frame-id")
# Interagir com elementos dentro do frame
driver.switch_to.default_content()  # Voltar ao contexto principal
```

## Processamento de Dados com Pandas

### 1. Otimize a Leitura de Dados

```python
import pandas as pd

# Especifique tipos de dados para melhor desempenho
dtypes = {
    'id': 'int32',
    'name': 'str',
    'value': 'float32',
    'date': 'str'  # Converter para datetime depois
}

# Leia apenas as colunas necessárias
df = pd.read_csv(
    'large_file.csv',
    usecols=['id', 'name', 'value', 'date'],
    dtype=dtypes,
    parse_dates=['date']
)

# Para arquivos muito grandes, use chunks
chunk_size = 100000
for chunk in pd.read_csv('very_large_file.csv', chunksize=chunk_size):
    # Processar cada chunk
    process_data(chunk)
```

### 2. Use Operações Vetorizadas

Evite loops e prefira operações vetorizadas:

```python
# Ruim (lento)
for i in range(len(df)):
    df.loc[i, 'new_column'] = df.loc[i, 'value'] * 2

# Bom (rápido)
df['new_column'] = df['value'] * 2

# Aplicar função personalizada
def complex_calculation(x):
    # Cálculos complexos...
    return result

# Aplicar vetorialmente
df['result'] = df['input'].apply(complex_calculation)
```

### 3. Encadeie Operações

Encadeie operações para código mais limpo:

```python
# Processamento de dados em uma sequência clara
result_df = (df
    .dropna(subset=['important_column'])
    .query('value > 0')
    .assign(
        ratio=lambda x: x['value'] / x['total'],
        category=lambda x: pd.cut(x['value'], bins=[0, 10, 50, 100], labels=['low', 'medium', 'high'])
    )
    .groupby('category')
    .agg({
        'value': ['sum', 'mean'],
        'ratio': 'mean'
    })
    .reset_index()
)
```

## Geração de Relatórios

### 1. Separe Dados da Apresentação

```python
def generate_sales_data():
    """Gera os dados de vendas."""
    # Implementação...
    return sales_data

def create_excel_report(data, output_path):
    """Cria relatório Excel a partir dos dados."""
    # Implementação com openpyxl...

def create_pdf_report(data, output_path):
    """Cria relatório PDF a partir dos dados."""
    # Implementação com reportlab...

# Uso
data = generate_sales_data()
create_excel_report(data, "reports/sales_report.xlsx")
create_pdf_report(data, "reports/sales_report.pdf")
```

### 2. Use Templates para Relatórios

Para relatórios complexos, considere usar templates:

```python
from jinja2 import Environment, FileSystemLoader

def generate_html_report(data, template_name, output_path):
    """Gera relatório HTML usando template Jinja2."""
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(f"{template_name}.html")
    
    html_content = template.render(
        title="Relatório de Vendas",
        data=data,
        generation_date=datetime.now().strftime("%d/%m/%Y %H:%M")
    )
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    return output_path

# Converter HTML para PDF
import pdfkit

def html_to_pdf(html_path, pdf_path):
    """Converte relatório HTML para PDF."""
    pdfkit.from_file(html_path, pdf_path)
```

## Segurança

### 1. Gerencie Credenciais com Segurança

Nunca armazene senhas diretamente no código:

```python
# Ruim
username = "admin"
password = "senha123"  # NUNCA faça isso!

# Bom - Usar variáveis de ambiente
import os
username = os.environ.get("API_USERNAME")
password = os.environ.get("API_PASSWORD")

# Alternativa - Arquivo de configuração seguro
import configparser
import keyring

config = configparser.ConfigParser()
config.read('config/settings.ini')

username = config['credentials']['username']
# Obter senha do gerenciador de credenciais do sistema
password = keyring.get_password("my_app", username)
```

### 2. Sanitize Dados de Entrada

Sempre valide e sanitize dados de entrada, especialmente em automações web:

```python
import re

def sanitize_input(text):
    """Remove caracteres potencialmente perigosos."""
    # Remover tags HTML, scripts, etc.
    sanitized = re.sub(r'<[^>]*>', '', text)
    # Remover caracteres especiais
    sanitized = re.sub(r'[^\w\s\-.,]', '', sanitized)
    return sanitized

# Uso em automação web
search_term = sanitize_input(user_input)
search_box.send_keys(search_term)
```

## Manutenção e Escalabilidade

### 1. Documente seu Código

Use docstrings e comentários significativos:

```python
def extract_product_data(url, selector):
    """
    Extrai informações de produtos de uma página web.
    
    Args:
        url (str): URL da página do produto
        selector (str): Seletor CSS para localizar os elementos do produto
        
    Returns:
        dict: Dicionário contendo informações do produto (nome, preço, disponibilidade)
        
    Raises:
        RequestException: Se houver erro ao acessar a URL
        ValueError: Se o seletor não encontrar elementos
    """
    # Implementação...
```

### 2. Implemente Testes Automatizados

Crie testes unitários para suas funções principais:

```python
# test_data_processor.py
import unittest
from scripts.data_processor import process_data

class TestDataProcessor(unittest.TestCase):
    def test_process_valid_data(self):
        input_data = {"name": "Test", "value": 100}
        result = process_data(input_data)
        self.assertEqual(result["processed_value"], 200)
    
    def test_process_invalid_data(self):
        input_data = {"name": "Test"}  # Falta o campo 'value'
        with self.assertRaises(ValueError):
            process_data(input_data)

if __name__ == "__main__":
    unittest.main()
```

### 3. Use Controle de Versão

Mantenha seu código em um sistema de controle de versão como Git:

- Faça commits pequenos e frequentes
- Use mensagens de commit descritivas
- Crie branches para novas funcionalidades
- Considere usar tags para marcar versões estáveis

## Conclusão

Seguir estas boas práticas ajudará você a criar scripts de automação mais robustos, eficientes e fáceis de manter. Lembre-se de que a automação deve economizar tempo no longo prazo, então investir em código de qualidade desde o início trará benefícios significativos.

## Recursos Adicionais

- [PEP 8 - Guia de Estilo para Python](https://pep8.org/)
- [The Hitchhiker's Guide to Python](https://docs.python-guide.org/)
- [Effective Python: 90 Specific Ways to Write Better Python](https://effectivepython.com/)
- [Python Testing with pytest](https://pragprog.com/titles/bopytest/python-testing-with-pytest/)
