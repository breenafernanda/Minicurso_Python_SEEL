# Guia de Instalação e Configuração

Este guia fornece instruções detalhadas para configurar o ambiente de desenvolvimento necessário para o minicurso de Automação com Python.

## Requisitos de Sistema

- **Sistema Operacional**: Windows 10/11, macOS 10.15+, ou Linux (Ubuntu 20.04+ recomendado)
- **Espaço em Disco**: Mínimo de 5GB livres
- **Memória RAM**: Mínimo de 4GB (8GB recomendado)
- **Conexão com Internet**: Necessária para download de pacotes e bibliotecas

## Instalação do Python

### Windows

1. Acesse [python.org](https://www.python.org/downloads/)
2. Baixe a versão mais recente do Python (3.10 ou superior)
3. Execute o instalador
4. **IMPORTANTE**: Marque a opção "Add Python to PATH"
5. Selecione "Install Now" para instalação padrão
6. Aguarde a conclusão da instalação

### macOS

1. Acesse [python.org](https://www.python.org/downloads/)
2. Baixe a versão mais recente do Python (3.10 ou superior)
3. Execute o instalador .pkg
4. Siga as instruções do assistente de instalação
5. Verifique a instalação abrindo o Terminal e digitando:
   ```
   python3 --version
   ```

### Linux (Ubuntu/Debian)

1. Abra o Terminal
2. Atualize os repositórios:
   ```
   sudo apt update
   ```
3. Instale o Python e ferramentas essenciais:
   ```
   sudo apt install python3 python3-pip python3-venv
   ```
4. Verifique a instalação:
   ```
   python3 --version
   ```

## Instalação do Visual Studio Code

### Windows/macOS/Linux

1. Acesse [code.visualstudio.com](https://code.visualstudio.com/)
2. Baixe a versão adequada para seu sistema operacional
3. Execute o instalador e siga as instruções
4. Após a instalação, abra o VS Code
5. Instale as extensões recomendadas:
   - Python (Microsoft)
   - Pylance
   - Jupyter
   - Python Indent

## Configuração do Ambiente Virtual

É recomendado usar ambientes virtuais para isolar as dependências do projeto.

### Windows

1. Abra o Prompt de Comando ou PowerShell
2. Navegue até a pasta do projeto:
   ```
   cd caminho\para\pasta\do\projeto
   ```
3. Crie um ambiente virtual:
   ```
   python -m venv venv
   ```
4. Ative o ambiente virtual:
   - No Prompt de Comando:
     ```
     venv\Scripts\activate
     ```
   - No PowerShell:
     ```
     .\venv\Scripts\Activate.ps1
     ```

### macOS/Linux

1. Abra o Terminal
2. Navegue até a pasta do projeto:
   ```
   cd caminho/para/pasta/do/projeto
   ```
3. Crie um ambiente virtual:
   ```
   python3 -m venv venv
   ```
4. Ative o ambiente virtual:
   ```
   source venv/bin/activate
   ```

## Instalação das Bibliotecas Necessárias

Com o ambiente virtual ativado, instale as bibliotecas necessárias:

```
pip install selenium pandas openpyxl reportlab pillow requests beautifulsoup4 matplotlib
```

## Configuração do WebDriver para Selenium

### Chrome

1. Verifique a versão do seu Chrome:
   - Abra o Chrome
   - Clique nos três pontos no canto superior direito
   - Vá para Ajuda > Sobre o Google Chrome

2. Baixe o ChromeDriver correspondente à sua versão:
   - Acesse [chromedriver.chromium.org](https://chromedriver.chromium.org/downloads)
   - Baixe a versão compatível com seu Chrome

3. Extraia o arquivo baixado

4. Adicione o ChromeDriver ao PATH:
   - **Windows**: Mova o arquivo para `C:\Windows\System32` ou adicione o diretório ao PATH
   - **macOS/Linux**: Mova o arquivo para `/usr/local/bin`

### Firefox

1. Baixe o GeckoDriver:
   - Acesse [github.com/mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases)
   - Baixe a versão mais recente para seu sistema operacional

2. Extraia o arquivo baixado

3. Adicione o GeckoDriver ao PATH:
   - **Windows**: Mova o arquivo para `C:\Windows\System32` ou adicione o diretório ao PATH
   - **macOS/Linux**: Mova o arquivo para `/usr/local/bin`

## Verificação da Instalação

Para verificar se tudo foi instalado corretamente, execute o seguinte script Python:

```python
# teste_instalacao.py

import sys
import pkg_resources

# Verificar versão do Python
print(f"Python versão: {sys.version}")

# Verificar bibliotecas instaladas
bibliotecas = [
    "selenium",
    "pandas",
    "openpyxl",
    "reportlab",
    "pillow",
    "requests",
    "beautifulsoup4",
    "matplotlib"
]

print("\nVerificando bibliotecas instaladas:")
for biblioteca in bibliotecas:
    try:
        versao = pkg_resources.get_distribution(biblioteca).version
        print(f"✓ {biblioteca}: {versao}")
    except pkg_resources.DistributionNotFound:
        print(f"✗ {biblioteca}: Não encontrada")

# Testar Selenium
print("\nTestando Selenium:")
try:
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    
    options = Options()
    options.add_argument("--headless")  # Modo invisível
    
    try:
        # Tentar com ChromeDriver
        service = Service()
        driver = webdriver.Chrome(service=service, options=options)
        print("✓ ChromeDriver: Funcionando")
        driver.quit()
    except Exception as e:
        print(f"✗ ChromeDriver: Erro - {str(e)}")
        
        try:
            # Tentar com GeckoDriver (Firefox)
            driver = webdriver.Firefox(options=options)
            print("✓ GeckoDriver: Funcionando")
            driver.quit()
        except Exception as e:
            print(f"✗ GeckoDriver: Erro - {str(e)}")
except Exception as e:
    print(f"✗ Selenium: Erro ao importar - {str(e)}")

print("\nVerificação concluída!")
```

Execute o script com:

```
python teste_instalacao.py
```

## Solução de Problemas Comuns

### Erro: "Python não é reconhecido como um comando interno"

- **Solução**: Verifique se o Python foi adicionado ao PATH durante a instalação. Reinstale o Python marcando a opção "Add Python to PATH".

### Erro: "pip não é reconhecido como um comando interno"

- **Solução**: Tente usar `python -m pip` em vez de apenas `pip`.

### Erro: "SessionNotCreatedException" no Selenium

- **Solução**: Verifique se a versão do WebDriver é compatível com a versão do seu navegador. Baixe a versão correta do WebDriver.

### Erro: "WebDriverException: Message: 'chromedriver' executable needs to be in PATH"

- **Solução**: Certifique-se de que o ChromeDriver está no PATH do sistema ou especifique o caminho completo ao criar o driver:
  ```python
  from selenium.webdriver.chrome.service import Service
  service = Service(executable_path='/caminho/para/chromedriver')
  driver = webdriver.Chrome(service=service)
  ```

### Erro ao instalar pacotes no Windows

- **Solução**: Tente executar o Prompt de Comando ou PowerShell como administrador.

## Recursos Adicionais

- [Documentação oficial do Python](https://docs.python.org/3/)
- [Documentação do Selenium](https://selenium-python.readthedocs.io/)
- [Documentação do Pandas](https://pandas.pydata.org/docs/)
- [Documentação do OpenPyXL](https://openpyxl.readthedocs.io/)
- [Documentação do ReportLab](https://www.reportlab.com/docs/reportlab-userguide.pdf)

## Suporte

Se encontrar problemas durante a instalação ou configuração, entre em contato pelo e-mail: suporte@exemplo.com
