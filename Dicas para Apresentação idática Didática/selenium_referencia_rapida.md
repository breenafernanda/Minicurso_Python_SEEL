# Referência Rápida: Selenium para Automação Web

## Configuração Inicial

### Instalação
```python
# Instalar Selenium
pip install selenium

# Instalar WebDriver Manager (gerencia drivers automaticamente)
pip install webdriver-manager
```

### Configuração Básica
```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Configurar opções do Chrome
options = Options()
options.add_argument("--start-maximized")  # Maximizar janela
options.add_argument("--disable-notifications")  # Desabilitar notificações
# options.add_argument("--headless")  # Modo sem interface (descomente se necessário)

# Inicializar o driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Definir tempo de espera implícito (em segundos)
driver.implicitly_wait(10)

# Acessar uma URL
driver.get("https://www.exemplo.com.br")

# Fechar o navegador ao final
driver.quit()
```

## Localização de Elementos

### Métodos de Localização
```python
from selenium.webdriver.common.by import By

# Localizar por ID
elemento = driver.find_element(By.ID, "meu-id")

# Localizar por nome
elemento = driver.find_element(By.NAME, "meu-nome")

# Localizar por classe CSS
elemento = driver.find_element(By.CLASS_NAME, "minha-classe")

# Localizar por seletor CSS
elemento = driver.find_element(By.CSS_SELECTOR, "div.produto > span.preco")

# Localizar por XPath
elemento = driver.find_element(By.XPATH, "//div[@class='produto']/span[1]")

# Localizar por texto do link
elemento = driver.find_element(By.LINK_TEXT, "Clique aqui")

# Localizar por texto parcial do link
elemento = driver.find_element(By.PARTIAL_LINK_TEXT, "Clique")

# Localizar por tag HTML
elemento = driver.find_element(By.TAG_NAME, "button")
```

### Localizar Múltiplos Elementos
```python
# Retorna uma lista de elementos
elementos = driver.find_elements(By.CSS_SELECTOR, ".produto")

# Iterar sobre os elementos
for elemento in elementos:
    nome = elemento.find_element(By.CSS_SELECTOR, ".nome").text
    preco = elemento.find_element(By.CSS_SELECTOR, ".preco").text
    print(f"Produto: {nome}, Preço: {preco}")
```

## Interação com Elementos

### Ações Básicas
```python
# Clicar em um elemento
elemento.click()

# Digitar texto
elemento.send_keys("Texto a ser digitado")

# Limpar campo de texto
elemento.clear()

# Enviar formulário
elemento.submit()

# Verificar se elemento está visível
if elemento.is_displayed():
    print("Elemento está visível")

# Verificar se elemento está habilitado
if elemento.is_enabled():
    print("Elemento está habilitado")

# Verificar se checkbox/radio está selecionado
if elemento.is_selected():
    print("Elemento está selecionado")
```

### Ações Avançadas
```python
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# Criar objeto ActionChains
actions = ActionChains(driver)

# Mover para um elemento (hover)
actions.move_to_element(elemento).perform()

# Arrastar e soltar
actions.drag_and_drop(origem, destino).perform()

# Clicar com botão direito
actions.context_click(elemento).perform()

# Duplo clique
actions.double_click(elemento).perform()

# Pressionar tecla
actions.send_keys(Keys.ESCAPE).perform()

# Pressionar combinação de teclas
actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
```

## Esperas e Sincronização

### Espera Explícita
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Esperar até que um elemento seja clicável (máximo 10 segundos)
elemento = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "botao-enviar"))
)

# Esperar até que um elemento esteja visível
elemento = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".mensagem-sucesso"))
)

# Esperar até que um elemento desapareça
WebDriverWait(driver, 10).until(
    EC.invisibility_of_element_located((By.CSS_SELECTOR, ".carregando"))
)

# Esperar até que o título da página contenha um texto
WebDriverWait(driver, 10).until(
    EC.title_contains("Confirmação")
)

# Esperar até que uma URL contenha um texto
WebDriverWait(driver, 10).until(
    EC.url_contains("sucesso")
)
```

### Condições de Espera Comuns
```python
# Principais condições de espera:
# - presence_of_element_located: elemento existe no DOM
# - visibility_of_element_located: elemento existe e está visível
# - element_to_be_clickable: elemento está visível e clicável
# - text_to_be_present_in_element: elemento contém um texto específico
# - alert_is_present: um alerta está presente
# - title_contains/title_is: título da página contém/é um texto
# - url_contains/url_matches: URL contém/corresponde a um texto/padrão
```

## Navegação e Janelas

### Navegação Básica
```python
# Navegar para uma URL
driver.get("https://www.exemplo.com.br")

# Navegar para frente/trás
driver.back()
driver.forward()

# Atualizar página
driver.refresh()

# Obter URL atual
url_atual = driver.current_url

# Obter título da página
titulo = driver.title

# Obter código-fonte da página
html = driver.page_source
```

### Manipulação de Janelas e Abas
```python
# Obter identificador da janela atual
janela_atual = driver.current_window_handle

# Obter identificadores de todas as janelas abertas
janelas = driver.window_handles

# Alternar para nova aba/janela (última aberta)
driver.switch_to.window(janelas[-1])

# Alternar para uma janela específica
driver.switch_to.window(janelas[0])  # Primeira janela

# Abrir nova aba
driver.execute_script("window.open('https://www.novosite.com.br', '_blank');")

# Fechar aba/janela atual
driver.close()

# Fechar todas as abas/janelas e encerrar sessão
driver.quit()
```

### Frames e Iframes
```python
# Alternar para um frame por índice
driver.switch_to.frame(0)  # Primeiro frame

# Alternar para um frame por ID ou nome
driver.switch_to.frame("nome-do-frame")

# Alternar para um frame por elemento
frame_elemento = driver.find_element(By.CSS_SELECTOR, "iframe.conteudo")
driver.switch_to.frame(frame_elemento)

# Voltar ao conteúdo principal
driver.switch_to.default_content()

# Voltar ao frame pai (quando dentro de frames aninhados)
driver.switch_to.parent_frame()
```

## Alertas e Diálogos

### Manipulação de Alertas
```python
from selenium.webdriver.common.alert import Alert

# Alternar para o alerta
alerta = driver.switch_to.alert

# Obter texto do alerta
texto = alerta.text

# Aceitar alerta (clicar em OK)
alerta.accept()

# Dispensar alerta (clicar em Cancelar)
alerta.dismiss()

# Digitar texto em prompt
alerta.send_keys("Texto de resposta")

# Esperar até que um alerta esteja presente
alerta = WebDriverWait(driver, 10).until(EC.alert_is_present())
```

## Captura de Tela e Cookies

### Screenshots
```python
# Capturar tela inteira
driver.save_screenshot("captura_tela.png")

# Capturar elemento específico
elemento = driver.find_element(By.ID, "minha-div")
elemento.screenshot("elemento.png")
```

### Manipulação de Cookies
```python
# Obter todos os cookies
cookies = driver.get_cookies()

# Adicionar cookie
driver.add_cookie({
    "name": "session_id",
    "value": "abc123",
    "domain": "exemplo.com.br"
})

# Obter cookie específico
cookie = driver.get_cookie("session_id")

# Excluir cookie específico
driver.delete_cookie("session_id")

# Excluir todos os cookies
driver.delete_all_cookies()
```

## JavaScript e Scroll

### Executar JavaScript
```python
# Executar JavaScript simples
driver.execute_script("return document.title;")

# Modificar elemento com JavaScript
driver.execute_script("arguments[0].style.border='3px solid red'", elemento)

# Clicar em elemento com JavaScript
driver.execute_script("arguments[0].click();", elemento)

# Rolar até um elemento
driver.execute_script("arguments[0].scrollIntoView(true);", elemento)

# Rolar até o final da página
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Rolar até o topo da página
driver.execute_script("window.scrollTo(0, 0);")
```

## Tratamento de Erros

### Exceções Comuns
```python
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    ElementClickInterceptedException,
    StaleElementReferenceException
)

try:
    elemento = driver.find_element(By.ID, "elemento-inexistente")
except NoSuchElementException:
    print("Elemento não encontrado")

try:
    elemento = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "elemento-demorado"))
    )
except TimeoutException:
    print("Tempo esgotado esperando pelo elemento")

try:
    elemento.click()
except ElementClickInterceptedException:
    print("Clique interceptado por outro elemento")
except StaleElementReferenceException:
    print("Elemento não está mais anexado ao DOM")
```

## Dicas para Automação Web

### Boas Práticas
1. **Use esperas explícitas** em vez de `time.sleep()`
2. **Localize elementos de forma robusta** (IDs são mais estáveis que XPaths complexos)
3. **Trate exceções** para lidar com comportamentos inesperados
4. **Implemente retry logic** para operações propensas a falhas
5. **Adicione logs detalhados** para facilitar a depuração
6. **Crie funções auxiliares** para operações repetitivas
7. **Use modos headless** para automações em produção/servidores

### Exemplo de Função de Retry
```python
def click_com_retry(driver, locator, max_attempts=3):
    """Tenta clicar em um elemento com retry em caso de falha."""
    for attempt in range(max_attempts):
        try:
            elemento = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(locator)
            )
            elemento.click()
            return True
        except (TimeoutException, ElementClickInterceptedException, StaleElementReferenceException) as e:
            if attempt == max_attempts - 1:
                print(f"Falha ao clicar após {max_attempts} tentativas: {str(e)}")
                return False
            print(f"Tentativa {attempt+1} falhou, tentando novamente...")
            time.sleep(1)
```
