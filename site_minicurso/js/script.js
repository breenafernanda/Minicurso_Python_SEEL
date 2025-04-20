// Inicialização dos editores CodeMirror
let editors = {};
let solutions = {
    'intro-1': 'print("Olá, mundo!")',
    'intro-2': `def verificar_maioridade(idade):
    if idade >= 18:
        return "Você é maior de idade."
    else:
        return "Você é menor de idade."

# Teste da função
idade = int(input("Digite sua idade: "))
print(verificar_maioridade(idade))`,
    'selenium-1': `from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Inicializar o navegador Chrome
driver = webdriver.Chrome(Options())

# Acessar uma URL
driver.get("https://www.google.com")

# Encontrar um elemento na página (campo de pesquisa)
campo_pesquisa = driver.find_element(By.NAME, "q")

# Interagir com o elemento
campo_pesquisa.send_keys("Selenium Python")

# Esperar um pouco para visualizar
time.sleep(2)

# Fechar o navegador
driver.quit()`,
    'pandas-1': `import pandas as pd

# Criar um DataFrame de exemplo
dados = {
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Daniela'],
    'Idade': [25, 30, 22, 28],
    'Salário': [3500, 4200, 2800, 5100]
}

# Criar o DataFrame
df = pd.DataFrame(dados)

# Exibir as primeiras linhas
print("Primeiras linhas do DataFrame:")
print(df.head())

# Análise básica
print("\\nInformações estatísticas:")
print(df.describe())

# Média de salário por idade
print("\\nMédia de salário:")
print(df['Salário'].mean())`,
    'openpyxl-1': `from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill

# Criar um novo Workbook
wb = Workbook()
ws = wb.active
ws.title = "Relatório"

# Adicionar cabeçalhos
headers = ["Nome", "Departamento", "Salário"]
for col_num, header in enumerate(headers, 1):
    cell = ws.cell(row=1, column=col_num)
    cell.value = header
    cell.font = Font(bold=True)
    cell.alignment = Alignment(horizontal='center')
    cell.fill = PatternFill(start_color="FFFF00", end_color="FFFF00", fill_type="solid")

# Adicionar dados
data = [
    ["João Silva", "TI", 5000],
    ["Maria Santos", "RH", 4500],
    ["Pedro Alves", "Vendas", 4800]
]

for row_num, row_data in enumerate(data, 2):
    for col_num, cell_value in enumerate(row_data, 1):
        ws.cell(row=row_num, column=col_num).value = cell_value

# Ajustar largura das colunas
for col in ws.columns:
    max_length = 0
    column = col[0].column_letter
    for cell in col:
        if cell.value:
            max_length = max(max_length, len(str(cell.value)))
    adjusted_width = (max_length + 2)
    ws.column_dimensions[column].width = adjusted_width

# Salvar o arquivo
wb.save("relatorio.xlsx")
print("Arquivo Excel criado com sucesso!")`,
    'pdf-1': `from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# Criar um novo PDF
c = canvas.Canvas("exemplo.pdf", pagesize=letter)
width, height = letter

# Adicionar um título
c.setFont("Helvetica-Bold", 16)
c.drawString(50, height - 50, "Relatório de Exemplo")

# Adicionar uma linha abaixo do título
c.setStrokeColor(colors.blue)
c.line(50, height - 60, width - 50, height - 60)

# Adicionar texto
c.setFont("Helvetica", 12)
c.drawString(50, height - 100, "Este é um exemplo de PDF criado com Python.")
c.drawString(50, height - 120, "Podemos adicionar texto, imagens e formas.")

# Adicionar uma forma
c.setFillColor(colors.lightblue)
c.rect(50, height - 200, 100, 50, fill=True)

# Adicionar texto dentro da forma
c.setFillColor(colors.black)
c.drawString(70, height - 175, "Python PDF")

# Salvar o PDF
c.save()
print("PDF criado com sucesso!")`,
    'projeto': `from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import time
import os

# Função para extrair dados de produtos da Amazon
def extrair_dados_amazon():
    # Configurar o driver
    options = Options()
    options.add_argument("--headless")  # Modo headless para execução sem interface gráfica
    driver = webdriver.Chrome(options=options)
    
    # Lista de produtos para pesquisar
    produtos_pesquisa = ["notebook", "smartphone", "fone de ouvido"]
    resultados = []
    
    try:
        for produto in produtos_pesquisa:
            # Acessar a Amazon
            driver.get("https://www.amazon.com.br")
            
            # Encontrar o campo de pesquisa e pesquisar o produto
            campo_pesquisa = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
            )
            campo_pesquisa.clear()
            campo_pesquisa.send_keys(produto)
            campo_pesquisa.submit()
            
            # Esperar os resultados carregarem
            time.sleep(3)
            
            # Extrair informações dos 3 primeiros produtos
            produtos_elementos = driver.find_elements(By.CSS_SELECTOR, "div[data-component-type='s-search-result']")[:3]
            
            for elemento in produtos_elementos:
                try:
                    # Extrair nome, preço e avaliação
                    nome = elemento.find_element(By.CSS_SELECTOR, "h2 a span").text
                    
                    try:
                        preco = elemento.find_element(By.CSS_SELECTOR, ".a-price .a-offscreen").get_attribute("innerHTML")
                    except:
                        preco = "Indisponível"
                    
                    try:
                        avaliacao = elemento.find_element(By.CSS_SELECTOR, ".a-icon-star-small .a-icon-alt").get_attribute("innerHTML")
                    except:
                        avaliacao = "Sem avaliação"
                    
                    # Adicionar à lista de resultados
                    resultados.append({
                        "Categoria": produto,
                        "Nome": nome,
                        "Preço": preco,
                        "Avaliação": avaliacao
                    })
                except Exception as e:
                    print(f"Erro ao extrair dados de um produto: {e}")
    
    except Exception as e:
        print(f"Erro durante a extração: {e}")
    
    finally:
        # Fechar o driver
        driver.quit()
    
    return resultados

# Função para salvar dados em Excel
def salvar_excel(dados):
    # Criar DataFrame
    df = pd.DataFrame(dados)
    
    # Criar um novo Workbook
    wb = Workbook()
    ws = wb.active
    ws.title = "Produtos Amazon"
    
    # Adicionar cabeçalhos
    headers = ["Categoria", "Nome", "Preço", "Avaliação"]
    for col_num, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col_num)
        cell.value = header
        cell.font = Font(bold=True)
        cell.alignment = Alignment(horizontal='center')
        cell.fill = PatternFill(start_color="FFFF00", end_color="FFFF00", fill_type="solid")
    
    # Adicionar dados
    for row_num, produto in enumerate(dados, 2):
        ws.cell(row=row_num, column=1).value = produto["Categoria"]
        ws.cell(row=row_num, column=2).value = produto["Nome"]
        ws.cell(row=row_num, column=3).value = produto["Preço"]
        ws.cell(row=row_num, column=4).value = produto["Avaliação"]
    
    # Ajustar largura das colunas
    for col in ws.columns:
        max_length = 0
        column = col[0].column_letter
        for cell in col:
            if cell.value:
                max_length = max(max_length, len(str(cell.value)))
        adjusted_width = (max_length + 2)
        ws.column_dimensions[column].width = adjusted_width
    
    # Salvar o arquivo
    arquivo_excel = "produtos_amazon.xlsx"
    wb.save(arquivo_excel)
    print(f"Arquivo Excel salvo: {arquivo_excel}")
    return arquivo_excel

# Função para gerar relatório PDF
def gerar_pdf(dados, arquivo_excel):
    # Criar um novo PDF
    arquivo_pdf = "relatorio_produtos.pdf"
    c = canvas.Canvas(arquivo_pdf, pagesize=letter)
    width, height = letter
    
    # Adicionar um título
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "Relatório de Produtos da Amazon")
    
    # Adicionar uma linha abaixo do título
    c.setStrokeColor(colors.blue)
    c.line(50, height - 60, width - 50, height - 60)
    
    # Adicionar informações
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 100, f"Data de geração: {time.strftime('%d/%m/%Y %H:%M:%S')}")
    c.drawString(50, height - 120, f"Total de produtos: {len(dados)}")
    c.drawString(50, height - 140, f"Categorias pesquisadas: notebook, smartphone, fone de ouvido")
    
    # Adicionar informações sobre os arquivos
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, height - 180, "Arquivos Gerados:")
    
    c.setFont("Helvetica", 12)
    c.drawString(70, height - 200, f"- Excel: {arquivo_excel}")
    c.drawString(70, height - 220, f"- PDF: {arquivo_pdf}")
    
    # Adicionar uma tabela simples com alguns produtos
    y_position = height - 270
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y_position, "Amostra de Produtos:")
    y_position -= 30
    
    # Cabeçalhos da tabela
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y_position, "Categoria")
    c.drawString(150, y_position, "Nome")
    c.drawString(400, y_position, "Preço")
    
    # Linha separadora
    y_position -= 10
    c.line(50, y_position, width - 50, y_position)
    y_position -= 20
    
    # Dados da tabela (primeiros 5 produtos ou menos)
    c.setFont("Helvetica", 10)
    for produto in dados[:5]:
        c.drawString(50, y_position, produto["Categoria"])
        # Limitar o tamanho do nome para caber na página
        nome = produto["Nome"][:30] + "..." if len(produto["Nome"]) > 30 else produto["Nome"]
        c.drawString(150, y_position, nome)
        c.drawString(400, y_position, produto["Preço"])
        y_position -= 20
    
    # Salvar o PDF
    c.save()
    print(f"Arquivo PDF salvo: {arquivo_pdf}")
    return arquivo_pdf

# Função principal
def main():
    print("Iniciando extração de dados da Amazon...")
    dados = extrair_dados_amazon()
    
    if dados:
        print(f"Foram extraídos dados de {len(dados)} produtos.")
        
        print("Salvando dados em Excel...")
        arquivo_excel = salvar_excel(dados)
        
        print("Gerando relatório PDF...")
        arquivo_pdf = gerar_pdf(dados, arquivo_excel)
        
        print("Processo concluído com sucesso!")
        print(f"Arquivos gerados: {arquivo_excel} e {arquivo_pdf}")
    else:
        print("Não foi possível extrair dados. Verifique a conexão ou tente novamente mais tarde.")

# Executar o programa
if __name__ == "__main__":
    main()`
};

// Função para inicializar os editores CodeMirror
function initializeEditors() {
    document.querySelectorAll('.challenge-editor').forEach(function(textarea) {
        const id = textarea.id;
        const challengeId = id.replace('editor-', '');
        
        editors[challengeId] = CodeMirror.fromTextArea(textarea, {
            mode: 'python',
            theme: 'dracula',
            lineNumbers: true,
            autoCloseBrackets: true,
            matchBrackets: true,
            indentUnit: 4,
            tabSize: 4,
            indentWithTabs: false,
            lineWrapping: true
        });
    });
}

// Função para validar o código Python
function validatePythonCode(code, expectedOutput) {
    // Verificar erros de sintaxe básicos
    try {
        // Verificar aspas em strings
        if (code.includes('print(') && !code.includes('"') && !code.includes("'")) {
            return {
                success: false,
                message: "Erro de sintaxe: Strings devem estar entre aspas (\" ou ')."
            };
        }
        
        // Verificar parênteses não fechados
        const openParens = (code.match(/\(/g) || []).length;
        const closeParens = (code.match(/\)/g) || []).length;
        if (openParens !== closeParens) {
            return {
                success: false,
                message: "Erro de sintaxe: Parênteses não estão balanceados."
            };
        }
        
        // Verificar aspas não fechadas
        const doubleQuotes = (code.match(/"/g) || []).length;
        const singleQuotes = (code.match(/'/g) || []).length;
        if (doubleQuotes % 2 !== 0 || singleQuotes % 2 !== 0) {
            return {
                success: false,
                message: "Erro de sintaxe: Aspas não estão balanceadas."
            };
        }
        
        // Verificações específicas para cada desafio
        if (expectedOutput === "Olá, mundo!") {
            if (!code.includes('print(') || !code.includes('"Olá, mundo!"') && !code.includes("'Olá, mundo!'")) {
                return {
                    success: false,
                    message: "Seu código deve imprimir exatamente a mensagem 'Olá, mundo!'."
                };
            }
            return {
                success: true,
                message: "Parabéns! Seu código imprime \"Olá, mundo!\" corretamente."
            };
        }
        
        // Verificação genérica para outros desafios
        return {
            success: true,
            message: "Código validado com sucesso!"
        };
    } catch (e) {
        return {
            success: false,
            message: "Erro ao validar o código: " + e.message
        };
    }
}

// Função para executar o código
function runCode(challengeId) {
    const code = editors[challengeId].getValue();
    const resultElement = document.getElementById('result-' + challengeId);
    
    // Simulação de execução (em um ambiente real, isso seria feito no servidor)
    let expectedOutput = "";
    
    if (challengeId === 'intro-1') {
        expectedOutput = "Olá, mundo!";
    } else if (challengeId === 'intro-2') {
        expectedOutput = "Você é maior de idade.";
    }
    
    const result = validatePythonCode(code, expectedOutput);
    
    if (result.success) {
        resultElement.style.color = '#4CAF50';
    } else {
        resultElement.style.color = '#F44336';
    }
    
    resultElement.textContent = result.message;
}

// Função para mostrar a solução
function showSolution(challengeId) {
    if (solutions[challengeId]) {
        editors[challengeId].setValue(solutions[challengeId]);
    }
}

// Função para reiniciar o editor
function resetEditor(challengeId) {
    const originalCode = document.getElementById('editor-' + challengeId).textContent;
    editors[challengeId].setValue(originalCode);
    document.getElementById('result-' + challengeId).textContent = '';
}

// Adicionar event listeners aos botões
function setupButtons() {
    document.querySelectorAll('.btn-run').forEach(function(button) {
        const challengeId = button.getAttribute('data-challenge');
        button.addEventListener('click', function() {
            runCode(challengeId);
        });
    });
    
    document.querySelectorAll('.btn-solution').forEach(function(button) {
        const challengeId = button.getAttribute('data-challenge');
        button.addEventListener('click', function() {
            showSolution(challengeId);
        });
    });
    
    document.querySelectorAll('.btn-reset').forEach(function(button) {
        const challengeId = button.getAttribute('data-challenge');
        button.addEventListener('click', function() {
            resetEditor(challengeId);
        });
    });
}

// Inicializar quando o DOM estiver carregado
document.addEventListener('DOMContentLoaded', function() {
    initializeEditors();
    setupButtons();
});
