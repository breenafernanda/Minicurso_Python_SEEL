# Exercícios Práticos: OpenPyXL para Manipulação de Planilhas

## Exercício 1: Criação de Relatório de Vendas

### Objetivo
Praticar a criação e formatação de planilhas Excel usando OpenPyXL.

### Enunciado
Você precisa criar um relatório de vendas mensal em formato Excel. Sua tarefa é:
1. Criar uma nova planilha Excel
2. Adicionar dados de vendas com formatação adequada
3. Criar um gráfico de barras para visualizar as vendas por produto
4. Adicionar fórmulas para calcular totais e médias
5. Aplicar formatação condicional para destacar valores importantes

### Dados de Entrada
```python
# Dados de vendas para o relatório
dados_vendas = [
    ["Produto", "Janeiro", "Fevereiro", "Março", "Total", "Média"],
    ["Notebook", 12, 15, 18, 0, 0],
    ["Smartphone", 25, 30, 28, 0, 0],
    ["Tablet", 8, 12, 15, 0, 0],
    ["Monitor", 10, 8, 12, 0, 0],
    ["Teclado", 20, 22, 25, 0, 0],
    ["Mouse", 30, 28, 32, 0, 0],
    ["Headset", 15, 14, 18, 0, 0],
    ["Total", 0, 0, 0, 0, 0]
]

# Informações adicionais
titulo_relatorio = "Relatório de Vendas - 1º Trimestre 2025"
nome_empresa = "TechStore Ltda."
data_geracao = "10/04/2025"
```

### Modelo de Solução
```python
# Solução do Exercício 1

from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.styles.differential import DifferentialStyle
from openpyxl.formatting.rule import Rule
from openpyxl.chart import BarChart, Reference
from openpyxl.drawing.image import Image
from openpyxl.utils import get_column_letter
import os

# Dados de vendas para o relatório
dados_vendas = [
    ["Produto", "Janeiro", "Fevereiro", "Março", "Total", "Média"],
    ["Notebook", 12, 15, 18, 0, 0],
    ["Smartphone", 25, 30, 28, 0, 0],
    ["Tablet", 8, 12, 15, 0, 0],
    ["Monitor", 10, 8, 12, 0, 0],
    ["Teclado", 20, 22, 25, 0, 0],
    ["Mouse", 30, 28, 32, 0, 0],
    ["Headset", 15, 14, 18, 0, 0],
    ["Total", 0, 0, 0, 0, 0]
]

# Informações adicionais
titulo_relatorio = "Relatório de Vendas - 1º Trimestre 2025"
nome_empresa = "TechStore Ltda."
data_geracao = "10/04/2025"

# Criar uma nova planilha
wb = Workbook()
ws = wb.active
ws.title = "Relatório de Vendas"

# Adicionar título e informações
ws.merge_cells('A1:F1')
ws['A1'] = titulo_relatorio
ws['A1'].font = Font(name='Arial', size=16, bold=True)
ws['A1'].alignment = Alignment(horizontal='center', vertical='center')

ws.merge_cells('A2:C2')
ws['A2'] = f"Empresa: {nome_empresa}"
ws['A2'].font = Font(name='Arial', size=12)

ws.merge_cells('D2:F2')
ws['D2'] = f"Data: {data_geracao}"
ws['D2'].font = Font(name='Arial', size=12)
ws['D2'].alignment = Alignment(horizontal='right')

# Definir altura das linhas de cabeçalho
ws.row_dimensions[1].height = 30
ws.row_dimensions[2].height = 20

# Adicionar espaço antes dos dados
ws.row_dimensions[3].height = 10

# Adicionar dados de vendas
for row_idx, row_data in enumerate(dados_vendas, start=4):
    for col_idx, cell_value in enumerate(row_data, start=1):
        ws.cell(row=row_idx, column=col_idx, value=cell_value)

# Calcular totais e médias
num_produtos = len(dados_vendas) - 2  # Excluindo cabeçalho e linha de total
for row in range(5, 5 + num_produtos):
    # Fórmula para total (soma de janeiro a março)
    ws.cell(row=row, column=5, value=f"=SUM(B{row}:D{row})")
    
    # Fórmula para média
    ws.cell(row=row, column=6, value=f"=AVERAGE(B{row}:D{row})")

# Calcular totais por mês (última linha)
last_row = 4 + num_produtos + 1
for col in range(2, 6):  # Colunas B a E
    col_letter = get_column_letter(col)
    ws.cell(row=last_row, column=col, value=f"=SUM({col_letter}5:{col_letter}{last_row-1})")

# Aplicar formatação ao cabeçalho
header_fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
header_font = Font(name='Arial', size=12, bold=True, color="FFFFFF")
header_alignment = Alignment(horizontal='center', vertical='center')

for col in range(1, 7):
    cell = ws.cell(row=4, column=col)
    cell.fill = header_fill
    cell.font = header_font
    cell.alignment = header_alignment

# Aplicar formatação à coluna de produtos e linha de totais
product_font = Font(name='Arial', size=11, bold=True)
for row in range(5, last_row + 1):
    ws.cell(row=row, column=1).font = product_font

total_fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")
for col in range(1, 7):
    ws.cell(row=last_row, column=col).fill = total_fill
    ws.cell(row=last_row, column=col).font = product_font

# Aplicar formatação às colunas de total e média
total_col_fill = PatternFill(start_color="E2EFDA", end_color="E2EFDA", fill_type="solid")
for row in range(5, last_row):
    ws.cell(row=row, column=5).fill = total_col_fill
    ws.cell(row=row, column=6).fill = total_col_fill

# Aplicar bordas a todas as células com dados
thin_border = Border(
    left=Side(style='thin'),
    right=Side(style='thin'),
    top=Side(style='thin'),
    bottom=Side(style='thin')
)

for row in range(4, last_row + 1):
    for col in range(1, 7):
        ws.cell(row=row, column=col).border = thin_border

# Aplicar formatação numérica
for row in range(5, last_row + 1):
    for col in range(2, 7):
        cell = ws.cell(row=row, column=col)
        cell.number_format = '#,##0'
        cell.alignment = Alignment(horizontal='center')

# Aplicar formatação condicional para destacar valores altos
# Regra para valores acima de 25
red_fill = PatternFill(start_color="FFCCCC", end_color="FFCCCC", fill_type="solid")
dxf = DifferentialStyle(fill=red_fill)
rule = Rule(type="cellIs", operator="greaterThan", formula=["25"], dxf=dxf)
ws.conditional_formatting.add(f"B5:D{last_row-1}", rule)

# Regra para valores abaixo de 10
yellow_fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
dxf = DifferentialStyle(fill=yellow_fill)
rule = Rule(type="cellIs", operator="lessThan", formula=["10"], dxf=dxf)
ws.conditional_formatting.add(f"B5:D{last_row-1}", rule)

# Ajustar largura das colunas
for col in range(1, 7):
    ws.column_dimensions[get_column_letter(col)].width = 15

# Criar gráfico de barras
chart = BarChart()
chart.title = "Vendas por Produto - 1º Trimestre"
chart.style = 10
chart.x_axis.title = "Produtos"
chart.y_axis.title = "Quantidade Vendida"

# Definir dados para o gráfico
data = Reference(ws, min_row=4, max_row=last_row-1, min_col=2, max_col=4)
cats = Reference(ws, min_row=5, max_row=last_row-1, min_col=1)
chart.add_data(data, titles_from_data=True)
chart.set_categories(cats)

# Adicionar gráfico à planilha
ws.add_chart(chart, "H4")

# Adicionar uma nova planilha com análise adicional
ws2 = wb.create_sheet(title="Análise de Desempenho")

# Adicionar título à segunda planilha
ws2.merge_cells('A1:D1')
ws2['A1'] = "Análise de Desempenho de Vendas"
ws2['A1'].font = Font(name='Arial', size=16, bold=True)
ws2['A1'].alignment = Alignment(horizontal='center', vertical='center')

# Adicionar dados de análise
ws2['A3'] = "Produto"
ws2['B3'] = "Total Vendido"
ws2['C3'] = "% do Total"
ws2['D3'] = "Classificação"

# Formatar cabeçalho
for col in range(1, 5):
    cell = ws2.cell(row=3, column=col)
    cell.fill = header_fill
    cell.font = header_font
    cell.alignment = header_alignment

# Adicionar fórmulas para análise
for i, produto in enumerate(dados_vendas[1:-1], start=4):
    # Nome do produto
    ws2.cell(row=i, column=1, value=produto[0])
    
    # Total vendido (referência à primeira planilha)
    ws2.cell(row=i, column=2, value=f"='Relatório de Vendas'!E{i+1}")
    
    # Porcentagem do total
    ws2.cell(row=i, column=3, value=f"=B{i}/'Relatório de Vendas'!E{last_row}")
    ws2.cell(row=i, column=3).number_format = '0.00%'
    
    # Classificação baseada no total vendido
    ws2.cell(row=i, column=4, value=f'=IF(B{i}>50,"Excelente",IF(B{i}>30,"Bom",IF(B{i}>15,"Regular","Baixo")))')

# Aplicar bordas e formatação
for row in range(3, 3 + num_produtos + 1):
    for col in range(1, 5):
        cell = ws2.cell(row=row, column=col)
        cell.border = thin_border
        if col == 2:
            cell.number_format = '#,##0'
        cell.alignment = Alignment(horizontal='center')

# Ajustar largura das colunas
for col in range(1, 5):
    ws2.column_dimensions[get_column_letter(col)].width = 15

# Criar gráfico de pizza para a segunda planilha
from openpyxl.chart import PieChart

pie = PieChart()
pie.title = "Distribuição de Vendas por Produto"
labels = Reference(ws2, min_col=1, min_row=4, max_row=3 + num_produtos)
data = Reference(ws2, min_col=2, min_row=3, max_row=3 + num_produtos)
pie.add_data(data, titles_from_data=True)
pie.set_categories(labels)
pie.height = 15
pie.width = 10

# Adicionar gráfico à segunda planilha
ws2.add_chart(pie, "F3")

# Salvar a planilha
wb.save("relatorio_vendas.xlsx")

print("Relatório de vendas criado com sucesso em 'relatorio_vendas.xlsx'!")
```

## Exercício 2: Automação de Processamento de Dados

### Objetivo
Praticar a leitura, processamento e escrita de dados em planilhas Excel usando OpenPyXL.

### Enunciado
Você recebeu uma planilha Excel com dados de funcionários e precisa processá-la para gerar um relatório de folha de pagamento. Sua tarefa é:
1. Ler a planilha de dados de funcionários
2. Calcular salários, descontos e valores líquidos
3. Criar uma nova planilha com os resultados calculados
4. Aplicar formatação adequada para um relatório profissional
5. Adicionar fórmulas e validações para garantir a integridade dos dados

### Dados de Entrada
Crie um arquivo `funcionarios.xlsx` com os seguintes dados:

| ID | Nome | Cargo | Departamento | Salário Base | Horas Extras | Faltas | Data Admissão |
|----|------|-------|--------------|--------------|--------------|--------|---------------|
| 1 | João Silva | Analista | TI | 5000 | 10 | 0 | 2020-03-15 |
| 2 | Maria Santos | Gerente | RH | 8000 | 5 | 1 | 2018-07-22 |
| 3 | Pedro Oliveira | Desenvolvedor | TI | 6500 | 15 | 0 | 2021-01-10 |
| 4 | Ana Costa | Analista | Financeiro | 4800 | 8 | 2 | 2019-11-05 |
| 5 | Carlos Souza | Assistente | Administrativo | 3200 | 12 | 1 | 2022-02-28 |
| 6 | Juliana Lima | Desenvolvedor | TI | 6200 | 20 | 0 | 2020-09-14 |
| 7 | Roberto Alves | Analista | Marketing | 4500 | 6 | 1 | 2021-05-20 |
| 8 | Fernanda Dias | Gerente | Comercial | 7800 | 8 | 0 | 2017-12-03 |
| 9 | Marcelo Gomes | Assistente | RH | 3000 | 4 | 3 | 2022-01-15 |
| 10 | Patrícia Rocha | Analista | Financeiro | 5200 | 12 | 1 | 2019-08-07 |

### Modelo de Solução
```python
# Solução do Exercício 2

from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.styles.differential import DifferentialStyle
from openpyxl.formatting.rule import Rule
from openpyxl.chart import BarChart, PieChart, Reference
from openpyxl.utils import get_column_letter
from datetime import datetime
import os

# Verificar se o arquivo de entrada existe
arquivo_entrada = "funcionarios.xlsx"
if not os.path.exists(arquivo_entrada):
    print(f"Arquivo {arquivo_entrada} não encontrado. Criando arquivo de exemplo...")
    
    # Criar arquivo de exemplo
    wb = Workbook()
    ws = wb.active
    ws.title = "Funcionários"
    
    # Adicionar cabeçalho
    cabecalho = ["ID", "Nome", "Cargo", "Departamento", "Salário Base", "Horas Extras", "Faltas", "Data Admissão"]
    for col, titulo in enumerate(cabecalho, start=1):
        ws.cell(row=1, column=col, value=titulo)
    
    # Adicionar dados
    dados = [
        [1, "João Silva", "Analista", "TI", 5000, 10, 0, "2020-03-15"],
        [2, "Maria Santos", "Gerente", "RH", 8000, 5, 1, "2018-07-22"],
        [3, "Pedro Oliveira", "Desenvolvedor", "TI", 6500, 15, 0, "2021-01-10"],
        [4, "Ana Costa", "Analista", "Financeiro", 4800, 8, 2, "2019-11-05"],
        [5, "Carlos Souza", "Assistente", "Administrativo", 3200, 12, 1, "2022-02-28"],
        [6, "Juliana Lima", "Desenvolvedor", "TI", 6200, 20, 0, "2020-09-14"],
        [7, "Roberto Alves", "Analista", "Marketing", 4500, 6, 1, "2021-05-20"],
        [8, "Fernanda Dias", "Gerente", "Comercial", 7800, 8, 0, "2017-12-03"],
        [9, "Marcelo Gomes", "Assistente", "RH", 3000, 4, 3, "2022-01-15"],
        [10, "Patrícia Rocha", "Analista", "Financeiro", 5200, 12, 1, "2019-08-07"]
    ]
    
    for row_idx, row_data in enumerate(dados, start=2):
        for col_idx, cell_value in enumerate(row_data, start=1):
            ws.cell(row=row_idx, column=col_idx, value=cell_value)
    
    # Formatar cabeçalho
    header_fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
    header_font = Font(name='Arial', size=12, bold=True, color="FFFFFF")
    
    for col in range(1, len(cabecalho) + 1):
        cell = ws.cell(row=1, column=col)
        cell.fill = header_fill
        cell.font = header_font
    
    # Ajustar largura das colunas
    for col in range(1, len(cabecalho) + 1):
        ws.column_dimensions[get_column_letter(col)].width = 15
    
    # Salvar arquivo de exemplo
    wb.save(arquivo_entrada)
    print(f"Arquivo de exemplo {arquivo_entrada} criado com sucesso!")

# Carregar planilha de funcionários
print(f"Carregando dados de {arquivo_entrada}...")
wb_funcionarios = load_workbook(arquivo_entrada)
ws_funcionarios = wb_funcionarios.active

# Criar nova planilha para o relatório de folha de pagamento
wb_relatorio = Workbook()
ws_relatorio = wb_relatorio.active
ws_relatorio.title = "Folha de Pagamento"

# Adicionar cabeçalho ao relatório
ws_relatorio.merge_cells('A1:K1')
ws_relatorio['A1'] = "RELATÓRIO DE FOLHA DE PAGAMENTO"
ws_relatorio['A1'].font = Font(name='Arial', size=16, bold=True)
ws_relatorio['A1'].alignment = Alignment(horizontal='center', vertical='center')

# Adicionar informações adicionais
data_atual = datetime.now().strftime("%d/%m/%Y")
ws_relatorio.merge_cells('A2:E2')
ws_relatorio['A2'] = "Empresa: Exemplo Corporação Ltda."
ws_relatorio['A2'].font = Font(name='Arial', size=12)

ws_relatorio.merge_cells('F2:K2')
ws_relatorio['F2'] = f"Data de Geração: {data_atual}"
ws_relatorio['F2'].font = Font(name='Arial', size=12)
ws_relatorio['F2'].alignment = Alignment(horizontal='right')

# Definir cabeçalho da tabela
cabecalho_relatorio = [
    "ID", "Nome", "Cargo", "Departamento", "Salário Base", "Valor Hora Extra", 
    "Total Horas Extras", "Desconto Faltas", "INSS", "IRRF", "Salário Líquido"
]

for col, titulo in enumerate(cabecalho_relatorio, start=1):
    ws_relatorio.cell(row=4, column=col, value=titulo)

# Definir estilos
header_fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
header_font = Font(name='Arial', size=12, bold=True, color="FFFFFF")
header_alignment = Alignment(horizontal='center', vertical='center')

# Aplicar estilos ao cabeçalho
for col in range(1, len(cabecalho_relatorio) + 1):
    cell = ws_relatorio.cell(row=4, column=col)
    cell.fill = header_fill
    cell.font = header_font
    cell.alignment = header_alignment

# Processar dados e calcular valores
row_relatorio = 5  # Começar a partir da linha 5 (após o cabeçalho)

# Definir bordas
thin_border = Border(
    left=Side(style='thin'),
    right=Side(style='thin'),
    top=Side(style='thin'),
    bottom=Side(style='thin')
)

# Iterar sobre as linhas da planilha de funcionários (pulando o cabeçalho)
for row in range(2, ws_funcionarios.max_row + 1):
    # Extrair dados
    id_func = ws_funcionarios.cell(row=row, column=1).value
    nome = ws_funcionarios.cell(row=row, column=2).value
    cargo = ws_funcionarios.cell(row=row, column=3).value
    departamento = ws_funcionarios.cell(row=row, column=4).value
    salario_base = ws_funcionarios.cell(row=row, column=5).value
    horas_extras = ws_funcionarios.cell(row=row, column=6).value
    faltas = ws_funcionarios.cell(row=row, column=7).value
    
    # Calcular valores
    valor_hora = salario_base / 220  # Considerando 220 horas mensais
    valor_hora_extra = valor_hora * 1.5  # 50% de adicional
    total_horas_extras = valor_hora_extra * horas_extras
    
    # Calcular desconto por faltas 
(Content truncated due to size limit. Use line ranges to read in chunks)