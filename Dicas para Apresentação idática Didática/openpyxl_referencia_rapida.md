# Referência Rápida: OpenPyXL para Manipulação de Planilhas Excel

## Configuração Inicial

### Instalação
```python
# Instalar OpenPyXL
pip install openpyxl
```

### Importação
```python
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.chart import BarChart, PieChart, LineChart, Reference
from openpyxl.utils import get_column_letter
from openpyxl.drawing.image import Image
```

## Criação e Carregamento de Planilhas

### Criar Nova Planilha
```python
# Criar um novo workbook
wb = Workbook()

# Acessar a planilha ativa
ws = wb.active

# Definir nome da planilha
ws.title = "Relatório de Vendas"

# Criar nova planilha
ws2 = wb.create_sheet(title="Dados Brutos")

# Listar todas as planilhas
planilhas = wb.sheetnames
```

### Carregar Planilha Existente
```python
# Carregar workbook existente
wb = load_workbook('planilha_existente.xlsx')

# Acessar planilha por nome
ws = wb['Relatório de Vendas']

# Acessar planilha por índice
ws = wb.worksheets[0]  # Primeira planilha
```

## Manipulação de Células

### Escrita em Células
```python
# Escrever em célula por coordenada
ws['A1'] = 'Produto'
ws['B1'] = 'Quantidade'
ws['C1'] = 'Preço'

# Escrever em célula por linha e coluna
ws.cell(row=1, column=4, value='Total')

# Escrever em múltiplas células
for i in range(2, 6):
    ws.cell(row=i, column=1, value=f'Produto {i-1}')
    ws.cell(row=i, column=2, value=i*10)
    ws.cell(row=i, column=3, value=i*5.5)
    # Fórmula para calcular o total
    ws.cell(row=i, column=4, value=f'=B{i}*C{i}')
```

### Leitura de Células
```python
# Ler valor de célula
valor_a1 = ws['A1'].value

# Ler valor por linha e coluna
valor = ws.cell(row=1, column=1).value

# Verificar se célula contém fórmula
formula = ws['D2'].value  # Retorna a fórmula como string

# Obter valor calculado de fórmula (apenas ao carregar planilha existente)
wb = load_workbook('planilha_com_formulas.xlsx', data_only=True)
ws = wb.active
valor_calculado = ws['D2'].value  # Retorna o resultado da fórmula
```

### Iteração sobre Células
```python
# Iterar por todas as linhas
for row in ws.rows:
    for cell in row:
        print(cell.value)

# Iterar por todas as colunas
for column in ws.columns:
    for cell in column:
        print(cell.value)

# Iterar por intervalo de células
for row in ws['A1:D5']:
    for cell in row:
        print(cell.value)

# Iterar por linhas com valores
for row in ws.iter_rows(min_row=2, max_row=5, min_col=1, max_col=4, values_only=True):
    produto, quantidade, preco, total = row
    print(f"Produto: {produto}, Total: {total}")
```

## Formatação de Células

### Fontes
```python
from openpyxl.styles import Font

# Criar estilo de fonte
fonte_titulo = Font(
    name='Arial',
    size=14,
    bold=True,
    italic=False,
    color='0000FF'  # Azul
)

# Aplicar fonte a uma célula
ws['A1'].font = fonte_titulo

# Aplicar fonte a múltiplas células
for cell in ws[1]:  # Primeira linha
    cell.font = fonte_titulo
```

### Alinhamento
```python
from openpyxl.styles import Alignment

# Criar estilo de alinhamento
alinhamento = Alignment(
    horizontal='center',  # left, center, right
    vertical='center',    # top, center, bottom
    wrap_text=True,       # Quebra de texto
    shrink_to_fit=False,  # Reduzir para caber
    indent=0              # Recuo
)

# Aplicar alinhamento
ws['A1'].alignment = alinhamento

# Alinhar múltiplas células
for row in ws.iter_rows(min_row=1, max_row=5):
    for cell in row:
        cell.alignment = alinhamento
```

### Preenchimento (Cor de Fundo)
```python
from openpyxl.styles import PatternFill

# Criar estilo de preenchimento
preenchimento_cabecalho = PatternFill(
    start_color='FFFF00',  # Amarelo
    end_color='FFFF00',
    fill_type='solid'
)

# Aplicar preenchimento
ws['A1'].fill = preenchimento_cabecalho

# Aplicar a múltiplas células
for cell in ws[1]:  # Primeira linha
    cell.fill = preenchimento_cabecalho
```

### Bordas
```python
from openpyxl.styles import Border, Side

# Definir estilo de borda
borda_fina = Side(style='thin', color='000000')
borda_grossa = Side(style='thick', color='000000')

# Criar objeto de borda
borda_completa = Border(
    left=borda_fina,
    right=borda_fina,
    top=borda_grossa,
    bottom=borda_fina
)

# Aplicar borda
ws['A1'].border = borda_completa

# Aplicar a múltiplas células
for row in ws.iter_rows(min_row=1, max_row=5, min_col=1, max_col=4):
    for cell in row:
        cell.border = borda_completa
```

### Formatação Numérica
```python
# Formato de número
ws['C2'].number_format = '#,##0.00'  # Duas casas decimais com separador de milhar

# Formato de porcentagem
ws['E2'].number_format = '0.00%'  # Porcentagem com duas casas decimais

# Formato de data
ws['F2'].number_format = 'dd/mm/yyyy'

# Formato de moeda
ws['D2'].number_format = 'R$ #,##0.00'
```

### Estilos Predefinidos
```python
from openpyxl.styles import NamedStyle

# Criar estilo nomeado
estilo_cabecalho = NamedStyle(name='estilo_cabecalho')
estilo_cabecalho.font = Font(bold=True, size=12, color='FFFFFF')
estilo_cabecalho.fill = PatternFill(start_color='0000FF', end_color='0000FF', fill_type='solid')
estilo_cabecalho.alignment = Alignment(horizontal='center', vertical='center')

# Adicionar estilo ao workbook
wb.add_named_style(estilo_cabecalho)

# Aplicar estilo
ws['A1'].style = 'estilo_cabecalho'
```

## Manipulação de Linhas e Colunas

### Dimensões
```python
# Definir altura da linha
ws.row_dimensions[1].height = 30  # Altura em pontos

# Definir largura da coluna
ws.column_dimensions['A'].width = 20  # Largura em caracteres

# Definir largura usando letra da coluna
col_letter = get_column_letter(3)  # 'C'
ws.column_dimensions[col_letter].width = 15
```

### Inserção e Remoção
```python
# Inserir linha
ws.insert_rows(2)  # Insere linha na posição 2

# Inserir múltiplas linhas
ws.insert_rows(5, 3)  # Insere 3 linhas a partir da posição 5

# Inserir coluna
ws.insert_cols(2)  # Insere coluna na posição 2

# Inserir múltiplas colunas
ws.insert_cols(3, 2)  # Insere 2 colunas a partir da posição 3

# Remover linha
ws.delete_rows(3)  # Remove linha 3

# Remover múltiplas linhas
ws.delete_rows(5, 2)  # Remove 2 linhas a partir da posição 5

# Remover coluna
ws.delete_cols(2)  # Remove coluna B

# Remover múltiplas colunas
ws.delete_cols(3, 2)  # Remove 2 colunas a partir da posição 3
```

### Mesclar e Separar Células
```python
# Mesclar células
ws.merge_cells('A1:D1')  # Mescla células de A1 até D1

# Mesclar por coordenadas
ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=4)

# Separar células mescladas
ws.unmerge_cells('A1:D1')
```

## Fórmulas e Funções

### Fórmulas Básicas
```python
# Soma
ws['D6'] = '=SUM(D2:D5)'

# Média
ws['D7'] = '=AVERAGE(D2:D5)'

# Máximo e Mínimo
ws['D8'] = '=MAX(D2:D5)'
ws['D9'] = '=MIN(D2:D5)'

# Contagem
ws['D10'] = '=COUNT(D2:D5)'

# Condicionais
ws['E2'] = '=IF(D2>100,"Alto","Baixo")'
```

### Referências Relativas e Absolutas
```python
# Referência relativa (muda ao copiar)
ws['D2'] = '=B2*C2'

# Referência absoluta (não muda ao copiar)
ws['D2'] = '=$B$2*C2'  # Coluna B fixa
ws['D2'] = '=B$2*C2'   # Linha 2 fixa
```

## Gráficos

### Gráfico de Barras
```python
from openpyxl.chart import BarChart, Reference

# Criar gráfico de barras
chart = BarChart()
chart.title = "Vendas por Produto"
chart.x_axis.title = "Produto"
chart.y_axis.title = "Valor (R$)"

# Definir dados
data = Reference(ws, min_row=1, max_row=5, min_col=1, max_col=1)  # Rótulos (produtos)
values = Reference(ws, min_row=2, max_row=5, min_col=4, max_col=4)  # Valores (totais)

# Adicionar dados ao gráfico
chart.add_data(values)
chart.set_categories(data)

# Adicionar gráfico à planilha
ws.add_chart(chart, "F1")
```

### Gráfico de Pizza
```python
from openpyxl.chart import PieChart

# Criar gráfico de pizza
chart = PieChart()
chart.title = "Distribuição de Vendas"

# Definir dados
data = Reference(ws, min_row=1, max_row=5, min_col=1, max_col=1)  # Rótulos
values = Reference(ws, min_row=2, max_row=5, min_col=4, max_col=4)  # Valores

# Adicionar dados ao gráfico
chart.add_data(values)
chart.set_categories(data)

# Adicionar gráfico à planilha
ws.add_chart(chart, "F15")
```

### Gráfico de Linha
```python
from openpyxl.chart import LineChart

# Criar gráfico de linha
chart = LineChart()
chart.title = "Tendência de Vendas"
chart.x_axis.title = "Período"
chart.y_axis.title = "Vendas"

# Definir dados
data = Reference(ws, min_row=1, max_row=1, min_col=2, max_col=6)  # Rótulos (períodos)
values = Reference(ws, min_row=2, max_row=2, min_col=2, max_col=6)  # Valores (vendas)

# Adicionar dados ao gráfico
chart.add_data(values)
chart.set_categories(data)

# Adicionar gráfico à planilha
ws.add_chart(chart, "A15")
```

## Imagens e Elementos Visuais

### Adicionar Imagem
```python
from openpyxl.drawing.image import Image

# Adicionar imagem
img = Image('logo.png')
img.width = 150  # Largura em pixels
img.height = 75  # Altura em pixels

# Posicionar imagem
ws.add_image(img, 'A1')
```

### Hiperlinks
```python
# Adicionar hiperlink para URL
ws['A1'].hyperlink = 'https://www.exemplo.com.br'
ws['A1'].value = 'Clique Aqui'
ws['A1'].style = 'Hyperlink'  # Estilo padrão de hiperlink

# Adicionar hiperlink para outra planilha
ws['B1'].hyperlink = f"#'{ws2.title}'!A1"
ws['B1'].value = 'Ir para Dados Brutos'
```

## Proteção e Validação

### Proteção de Planilha
```python
# Proteger planilha
ws.protection.sheet = True
ws.protection.password = 'senha123'

# Permitir edição de células específicas
ws['B2'].protection = Protection(locked=False)
```

### Validação de Dados
```python
from openpyxl.worksheet.datavalidation import DataValidation

# Validação de lista
dv = DataValidation(type="list", formula1='"Sim,Não,Talvez"')
ws.add_data_validation(dv)
dv.add('E2:E10')

# Validação numérica
dv_num = DataValidation(type="whole", operator="between", formula1=1, formula2=100)
ws.add_data_validation(dv_num)
dv_num.add('B2:B10')
```

## Operações Avançadas

### Filtros e Classificação
```python
# Adicionar filtro automático
ws.auto_filter.ref = 'A1:D5'

# Congelar painéis
ws.freeze_panes = 'A2'  # Congela a primeira linha
```

### Comentários
```python
from openpyxl.comments import Comment

# Adicionar comentário
comment = Comment('Este é um comentário', 'Autor')
ws['A1'].comment = comment
```

### Impressão
```python
# Configurar área de impressão
ws.print_area = 'A1:D10'

# Configurar orientação da página
ws.page_setup.orientation = ws.ORIENTATION_LANDSCAPE

# Configurar tamanho do papel
ws.page_setup.paperSize = ws.PAPERSIZE_A4

# Ajustar para caber em uma página
ws.page_setup.fitToPage = True
ws.page_setup.fitToHeight = 1
ws.page_setup.fitToWidth = 1

# Adicionar cabeçalho/rodapé
ws.oddHeader.center.text = "Relatório de Vendas"
ws.oddFooter.right.text = "Página &[Page] de &[Pages]"
```

## Salvamento e Exportação

### Salvar Workbook
```python
# Salvar como novo arquivo
wb.save('relatorio_vendas.xlsx')

# Salvar com senha
wb.security.workbookPassword = 'senha123'
wb.security.lockStructure = True
wb.save('relatorio_protegido.xlsx')
```

### Exportar como Template
```python
# Salvar como template
wb.template = True
wb.save('template_relatorio.xltx')
```

## Dicas para Manipulação de Planilhas

### Boas Práticas
1. **Sempre feche os arquivos** após manipulação para liberar recursos
2. **Use `with` para carregar workbooks** quando possível
3. **Faça backup** antes de modificar planilhas importantes
4. **Agrupe operações de estilo** para melhorar performance
5. **Use estilos nomeados** para formatação consistente
6. **Documente seu código** com comentários explicativos
7. **Teste com arquivos pequenos** antes de processar grandes planilhas

### Otimização de Desempenho
```python
# Desativar cálculo automático para melhorar performance
wb.calculation.calcMode = 'manual'

# Reativar cálculo ao finalizar
wb.calculation.calcMode = 'auto'
wb.calculate()

# Usar write_only para grandes volumes de dados
from openpyxl import Workbook
wb = Workbook(write_only=True)
ws = wb.create_sheet()

# Adicionar linhas em lote (mais eficiente)
for i in range(1000):
    ws.append([f'Dado {i}', i, i*2])
```

### Exemplo de Função Auxiliar
```python
def aplicar_estilo_cabecalho(planilha, linha, colunas_inicio_fim):
    """Aplica estilo de cabeçalho a uma linha."""
    inicio, fim = colunas_inicio_fim
    fonte = Font(bold=True, color="FFFFFF")
    preenchimento = PatternFill(start_color="0066CC", end_color="0066CC", fill_type="solid")
    alinhamento = Alignment(horizontal="center", vertical="center")
    
    for col in range(inicio, fim + 1):
        cell = planilha.cell(row=linha, column=col)
        cell.font = fonte
        cell.fill = preenchimento
        cell.alignment = alinhamento
        
    return planilha
```
