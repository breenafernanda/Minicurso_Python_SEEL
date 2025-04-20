# Referência Rápida: ReportLab para Geração de PDFs

## Configuração Inicial

### Instalação
```python
# Instalar ReportLab
pip install reportlab

# Instalar Pillow (para suporte a imagens)
pip install pillow
```

### Importação
```python
# Importações básicas
from reportlab.lib.pagesizes import A4, letter, landscape
from reportlab.lib import colors
from reportlab.lib.units import cm, mm, inch
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak
```

## Abordagens de Criação de PDF

### Abordagem Canvas (Baixo Nível)
```python
# Criar um novo PDF
c = canvas.Canvas("documento_canvas.pdf", pagesize=A4)

# Definir fonte e tamanho
c.setFont("Helvetica", 12)

# Escrever texto
c.drawString(100, 750, "Olá, este é um documento PDF criado com ReportLab!")

# Desenhar linha
c.line(100, 740, 500, 740)

# Salvar o documento
c.save()
```

### Abordagem Platypus (Alto Nível)
```python
# Criar documento
doc = SimpleDocTemplate(
    "documento_platypus.pdf",
    pagesize=A4,
    rightMargin=2*cm,
    leftMargin=2*cm,
    topMargin=2*cm,
    bottomMargin=2*cm
)

# Criar lista de elementos
elementos = []

# Adicionar título
estilos = getSampleStyleSheet()
elementos.append(Paragraph("Título do Documento", estilos['Title']))

# Adicionar espaço
elementos.append(Spacer(1, 0.5*cm))

# Adicionar texto
elementos.append(Paragraph("Este é um parágrafo de texto normal.", estilos['Normal']))

# Construir o documento
doc.build(elementos)
```

## Texto e Formatação

### Estilos de Texto
```python
# Obter estilos padrão
estilos = getSampleStyleSheet()

# Estilos disponíveis
titulo = estilos['Title']
cabecalho1 = estilos['Heading1']
cabecalho2 = estilos['Heading2']
normal = estilos['Normal']
lista_item = estilos['BodyText']
codigo = estilos['Code']

# Criar estilo personalizado
estilo_personalizado = ParagraphStyle(
    'EstiloPersonalizado',
    parent=estilos['Normal'],
    fontSize=14,
    textColor=colors.blue,
    alignment=1,  # 0=esquerda, 1=centro, 2=direita
    spaceAfter=12,
    spaceBefore=12,
    leading=16,  # Espaçamento entre linhas
    backColor=colors.lightgrey,
    borderWidth=1,
    borderColor=colors.black,
    borderRadius=5,
    borderPadding=5
)
```

### Parágrafos e Formatação
```python
# Texto simples
elementos.append(Paragraph("Texto normal", estilos['Normal']))

# Texto com formatação HTML
texto_html = """
<para align="center">
    <font size="14" color="blue"><b>Texto em Negrito Azul</b></font><br/>
    <i>Texto em itálico</i><br/>
    <u>Texto sublinhado</u><br/>
    <strike>Texto tachado</strike>
</para>
"""
elementos.append(Paragraph(texto_html, estilos['Normal']))

# Texto com links
texto_link = 'Visite o <a href="https://www.python.org" color="blue">site do Python</a>'
elementos.append(Paragraph(texto_link, estilos['Normal']))
```

### Listas
```python
from reportlab.platypus import ListFlowable, ListItem

# Lista simples
itens = [
    Paragraph("Primeiro item", estilos['Normal']),
    Paragraph("Segundo item", estilos['Normal']),
    Paragraph("Terceiro item", estilos['Normal'])
]
lista = ListFlowable(
    itens,
    bulletType='bullet',  # 'bullet', 'number', 'lettern', 'letterupper', 'roman', 'romanupper'
    start=1,              # Número inicial para listas numeradas
    bulletFontSize=10,
    leftIndent=20
)
elementos.append(lista)
```

## Tabelas

### Tabela Básica
```python
# Dados da tabela
dados = [
    ['Nome', 'Idade', 'Cidade'],
    ['João', '25', 'São Paulo'],
    ['Maria', '30', 'Rio de Janeiro'],
    ['Carlos', '22', 'Belo Horizonte']
]

# Criar tabela
tabela = Table(dados)

# Adicionar tabela aos elementos
elementos.append(tabela)
```

### Estilização de Tabela
```python
# Criar tabela com larguras específicas
tabela = Table(dados, colWidths=[4*cm, 2*cm, 5*cm])

# Definir estilo da tabela
estilo_tabela = TableStyle([
    # Estilo do cabeçalho
    ('BACKGROUND', (0, 0), (-1, 0), colors.blue),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    
    # Estilo das células
    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ('ALIGN', (1, 1), (1, -1), 'CENTER'),  # Centralizar coluna de idade
    ('ALIGN', (2, 1), (2, -1), 'LEFT'),    # Alinhar à esquerda coluna de cidade
    
    # Bordas
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('BOX', (0, 0), (-1, -1), 2, colors.black),
    
    # Cores alternadas nas linhas
    ('BACKGROUND', (0, 1), (-1, 1), colors.lightgrey),
    ('BACKGROUND', (0, 3), (-1, 3), colors.lightgrey),
])

# Aplicar estilo à tabela
tabela.setStyle(estilo_tabela)

# Adicionar tabela aos elementos
elementos.append(tabela)
```

### Mesclar Células
```python
# Dados da tabela
dados = [
    ['Relatório de Vendas', '', ''],
    ['Produto', 'Quantidade', 'Valor'],
    ['Produto A', '10', 'R$ 100,00'],
    ['Produto B', '5', 'R$ 75,00'],
    ['Total', '', 'R$ 175,00']
]

# Criar tabela
tabela = Table(dados)

# Definir estilo com células mescladas
estilo_tabela = TableStyle([
    # Mesclar células do título
    ('SPAN', (0, 0), (2, 0)),
    
    # Mesclar células do total
    ('SPAN', (1, 4), (1, 4)),
    
    # Outros estilos
    ('ALIGN', (0, 0), (0, 0), 'CENTER'),
    ('FONTNAME', (0, 0), (0, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (0, 0), 14),
    
    ('BACKGROUND', (0, 1), (2, 1), colors.grey),
    ('TEXTCOLOR', (0, 1), (2, 1), colors.white),
    
    ('ALIGN', (1, 2), (2, -1), 'RIGHT'),
    ('GRID', (0, 1), (2, -1), 1, colors.black),
])

# Aplicar estilo à tabela
tabela.setStyle(estilo_tabela)
```

## Imagens

### Adicionar Imagem
```python
from reportlab.platypus import Image

# Adicionar imagem com tamanho específico
logo = Image('logo.png', width=5*cm, height=3*cm)
elementos.append(logo)

# Imagem com máscara (transparência)
logo = Image('logo.png', width=5*cm, height=3*cm, mask='auto')
elementos.append(logo)

# Imagem com posicionamento
logo = Image('logo.png', width=5*cm, height=3*cm)
logo.hAlign = 'CENTER'  # LEFT, CENTER, RIGHT
elementos.append(logo)
```

### Fluxo de Texto ao Redor de Imagens
```python
from reportlab.platypus import ImageAndFlowables, Paragraph

# Texto para fluxo
texto = """
Este é um texto longo que irá fluir ao redor da imagem. 
O texto continuará a ser exibido ao lado da imagem até 
que não haja mais espaço, e então continuará abaixo da imagem.
"""

# Criar parágrafos
paragrafos = [
    Paragraph(texto, estilos['Normal']),
    Paragraph(texto, estilos['Normal'])
]

# Imagem com texto ao redor
img_com_texto = ImageAndFlowables(
    Image('logo.png', width=4*cm, height=4*cm),
    paragrafos,
    imageSide='left'  # 'left' ou 'right'
)
elementos.append(img_com_texto)
```

## Gráficos e Desenhos

### Gráfico de Barras
```python
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart

# Criar desenho
desenho = Drawing(400, 200)

# Criar gráfico de barras
grafico = VerticalBarChart()
grafico.x = 50
grafico.y = 50
grafico.height = 125
grafico.width = 300
grafico.data = [[10, 20, 30, 40, 50]]
grafico.categoryAxis.categoryNames = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai']
grafico.valueAxis.valueMin = 0
grafico.valueAxis.valueMax = 60
grafico.valueAxis.valueStep = 10
grafico.bars[0].fillColor = colors.blue

# Adicionar gráfico ao desenho
desenho.add(grafico)

# Adicionar desenho aos elementos
elementos.append(desenho)
```

### Gráfico de Pizza
```python
from reportlab.graphics.charts.piecharts import Pie

# Criar desenho
desenho = Drawing(400, 200)

# Criar gráfico de pizza
grafico = Pie()
grafico.x = 150
grafico.y = 100
grafico.width = 150
grafico.height = 150
grafico.data = [20, 30, 40, 10]
grafico.labels = ['A', 'B', 'C', 'D']
grafico.slices.strokeWidth = 0.5
grafico.slices[0].fillColor = colors.blue
grafico.slices[1].fillColor = colors.red
grafico.slices[2].fillColor = colors.green
grafico.slices[3].fillColor = colors.yellow

# Adicionar gráfico ao desenho
desenho.add(grafico)

# Adicionar desenho aos elementos
elementos.append(desenho)
```

### Formas Básicas (com Canvas)
```python
# Exemplo com Canvas
c = canvas.Canvas("formas.pdf", pagesize=A4)

# Retângulo
c.rect(100, 700, 200, 100, fill=0)  # x, y, largura, altura

# Retângulo preenchido
c.setFillColor(colors.blue)
c.rect(100, 550, 200, 100, fill=1)

# Círculo
c.setFillColor(colors.red)
c.circle(200, 400, 50, fill=1)  # x, y, raio

# Linha
c.setStrokeColor(colors.green)
c.setLineWidth(2)
c.line(100, 300, 300, 300)  # x1, y1, x2, y2

# Curva
c.bezier(100, 200, 150, 250, 250, 150, 300, 200)  # x1, y1, x2, y2, x3, y3, x4, y4

# Polígono
c.setFillColor(colors.yellow)
pontos = [100, 100, 200, 150, 300, 100, 250, 50, 150, 50]
c.polygon(pontos, fill=1)

c.save()
```

## Cabeçalhos, Rodapés e Paginação

### Cabeçalho e Rodapé com Platypus
```python
from reportlab.platypus import PageTemplate, Frame, BaseDocTemplate
from reportlab.platypus.flowables import Flowable

class Cabecalho(Flowable):
    def __init__(self, width=None, height=None):
        Flowable.__init__(self)
        self.width = width or A4[0]
        self.height = height or 2*cm
        
    def draw(self):
        # Desenhar cabeçalho
        self.canv.setFillColor(colors.blue)
        self.canv.rect(0, 0, self.width, self.height, fill=1)
        self.canv.setFillColor(colors.white)
        self.canv.setFont("Helvetica-Bold", 16)
        self.canv.drawCentredString(self.width/2, self.height/2, "RELATÓRIO DE VENDAS")

class Rodape(Flowable):
    def __init__(self, width=None, height=None, page_number=None):
        Flowable.__init__(self)
        self.width = width or A4[0]
        self.height = height or 1*cm
        self.page_number = page_number
        
    def draw(self):
        # Desenhar rodapé
        self.canv.setStrokeColor(colors.black)
        self.canv.line(0, self.height, self.width, self.height)
        self.canv.setFont("Helvetica", 9)
        self.canv.drawRightString(self.width - 1*cm, 0.5*cm, f"Página {self.page_number}")
        self.canv.drawString(1*cm, 0.5*cm, "Confidencial")

# Função para adicionar cabeçalho e rodapé
def adicionar_cabecalho_rodape(canvas, doc):
    canvas.saveState()
    
    # Adicionar cabeçalho
    cabecalho = Cabecalho(doc.width + doc.leftMargin + doc.rightMargin)
    cabecalho.canv = canvas
    cabecalho.draw()
    
    # Adicionar rodapé
    rodape = Rodape(doc.width + doc.leftMargin + doc.rightMargin, page_number=doc.page)
    rodape.canv = canvas
    rodape.draw()
    
    canvas.restoreState()

# Criar documento com cabeçalho e rodapé
doc = SimpleDocTemplate("documento_com_cabecalho.pdf", pagesize=A4)
doc.build(elementos, onFirstPage=adicionar_cabecalho_rodape, onLaterPages=adicionar_cabecalho_rodape)
```

### Numeração de Páginas
```python
# Adicionar numeração de páginas com Canvas
def adicionar_numero_pagina(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica', 10)
    texto = f"Página {doc.page} de {doc.pageCount}"
    canvas.drawRightString(A4[0] - 2*cm, 2*cm, texto)
    canvas.restoreState()

# Construir documento com numeração de páginas
doc.build(elementos, onFirstPage=adicionar_numero_pagina, onLaterPages=adicionar_numero_pagina)
```

## Marcas d'água e Fundos

### Adicionar Marca d'água
```python
def adicionar_marca_dagua(canvas, doc):
    canvas.saveState()
    
    # Configurar fonte e cor
    canvas.setFont('Helvetica', 70)
    canvas.setFillColor(colors.lightgrey)
    
    # Rotacionar e posicionar
    canvas.translate(A4[0]/2, A4[1]/2)
    canvas.rotate(45)
    canvas.drawCentredString(0, 0, "CONFIDENCIAL")
    
    canvas.restoreState()

# Construir documento com marca d'água
doc.build(elementos, onFirstPage=adicionar_marca_dagua, onLaterPages=adicionar_marca_dagua)
```

### Adicionar Fundo Colorido
```python
def adicionar_fundo(canvas, doc):
    canvas.saveState()
    
    # Desenhar retângulo de fundo
    canvas.setFillColor(colors.lightgrey)
    canvas.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
    
    canvas.restoreState()

# Construir documento com fundo
doc.build(elementos, onFirstPage=adicionar_fundo, onLaterPages=adicionar_fundo)
```

## Índice e Referências

### Criar Índice
```python
from reportlab.platypus.tableofcontents import TableOfContents

# Criar índice
toc = TableOfContents()
toc.levelStyles = [
    ParagraphStyle(name='TOCHeading1', fontSize=14, fontName='Helvetica-Bold'),
    ParagraphStyle(name='TOCHeading2', fontSize=12, fontName='Helvetica', leftIndent=20),
    ParagraphStyle(name='TOCHeading3', fontSize=10, fontName='Helvetica', leftIndent=40)
]

# Adicionar índice aos elementos
elementos.append(Paragraph("Índice", estilos['Title']))
elementos.append(toc)
elementos.append(PageBreak())

# Adicionar entradas que aparecerão no índice
elementos.append(Paragraph("1. Introdução", estilos['Heading1']))
elementos.append(Paragraph("Este é o conteúdo da introdução...", estilos['Normal']))
elementos.append(Paragraph("1.1 Contexto", estilos['Heading2']))
elementos.append(Paragraph("Este é o conteúdo do contexto...", estilos['Normal']))

# Construir documento com índice
doc.multiBuild(elementos)  # Use multiBuild em vez de build
```

### Referências Cruzadas
```python
from reportlab.platypus.flowables import Flowable

class Bookmark(Flowable):
    def __init__(self, title, key):
        Flowable.__init__(self)
        self.title = title
        self.key = key
        self.width = 0
        self.height = 0
        
    def draw(self):
        self.canv.bookmarkPage(self.key)
        self.canv.addOutlineEntry(self.title, self.key, 0, 0)

# Adicionar marcadores
elementos.append(Bookmark("Introdução", "intro"))
elementos.append(Paragraph("1. Introdução", estilos['Heading1']))
elementos.append(Paragraph("Este é o conteúdo da introdução...", estilos['Normal']))

elementos.append(Bookmark("Metodologia", "metodo"))
elementos.append(Paragraph("2. Metodologia", estilos['Heading1']))
elementos.append(Paragraph("Este é o conteúdo da metodologia...", estilos['Normal']))

# Adicionar link interno
link_texto = 'Veja a <a href="#metodo" color="blue">Metodologia</a> para mais detalhes.'
elementos.append(Paragraph(link_texto, estilos['Normal']))
```

## Formulários e Campos Interativos

### Criar Formulário Interativo
```python
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.colors import magenta, pink, blue, green

# Criar canvas
c = Canvas("formulario.pdf", pagesize=A4)
c.setFont("Helvetica", 12)

# Título
c.drawString(100, 750, "Formulário de Cadastro")
c.line(100, 747, 500, 747)

# Campo de texto
c.drawString(100, 700, "Nome:")
c.rect(100, 675, 400, 25, fill=0)
c.acroForm.textfield(name='nome', tooltip='Digite seu nome',
                    x=100, y=675, width=400, height=25,
                    borderWidth=1, borderColor=magenta,
                    fillColor=pink, textColor=blue,
                    forceBorder=True)

# Campo de senha
c.drawString(100, 650, "Senha:")
c.rect(100, 625, 400, 25, fill=0)
c.acroForm.textfield(name='senha', tooltip='Digite sua senha',
                    x=100, y=625, width=400, height=25,
                    borderWidth=1, borderColor=magenta,
                    fillColor=pink, textColor=blue,
                    forceBorder=True, password=True)

# Checkbox
c.drawString(100, 600, "Interesses:")
c.rect(100, 575, 20, 20, fill=0)
c.acroForm.checkbox(name='python', tooltip='Python',
                   x=100, y=575, size=20,
                   borderWidth=1, borderColor=magenta,
                   fillColor=pink, textColor=blue,
                   forceBorder=True)
c.drawString(125, 580, "Python")

# Radio buttons
c.drawString(100, 550, "Gênero:")
c.rect(100, 525, 20, 20, fill=0)
c.acroForm.radio(name='genero', tooltip='Masculino',
                value='M', selected=False,
                x=100, y=525, size=20,
                borderWidth=1, borderColor=magenta,
                fillColor=pink,
(Content truncated due to size limit. Use line ranges to read in chunks)