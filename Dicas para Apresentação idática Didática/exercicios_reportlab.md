# Exercícios Práticos: ReportLab para Geração de PDFs

## Exercício 1: Criação de Catálogo de Produtos

### Objetivo
Praticar a criação de documentos PDF com imagens, textos formatados e tabelas usando ReportLab.

### Enunciado
Você precisa criar um catálogo de produtos em PDF para uma loja. Sua tarefa é:
1. Criar um documento PDF com capa, índice e páginas de produtos
2. Adicionar imagens de produtos com descrições
3. Formatar textos com diferentes estilos e cores
4. Criar tabelas de especificações para cada produto
5. Adicionar cabeçalho, rodapé e numeração de páginas

### Dados de Entrada
```python
# Dados dos produtos para o catálogo
produtos = [
    {
        "id": 1,
        "nome": "Notebook Profissional",
        "descricao": "Notebook de alto desempenho para profissionais. Ideal para tarefas exigentes como edição de vídeo, design gráfico e desenvolvimento de software.",
        "preco": 4599.99,
        "categoria": "Informática",
        "especificacoes": {
            "Processador": "Intel Core i7 11ª Geração",
            "Memória RAM": "16GB DDR4",
            "Armazenamento": "SSD 512GB",
            "Tela": "15.6 polegadas Full HD",
            "Placa de Vídeo": "NVIDIA GeForce RTX 3050 4GB",
            "Sistema Operacional": "Windows 11 Pro"
        },
        "imagem": "notebook.jpg"  # Substitua pelo caminho de uma imagem real
    },
    {
        "id": 2,
        "nome": "Smartphone Premium",
        "descricao": "Smartphone de última geração com câmera profissional e bateria de longa duração. Perfeito para fotografia, jogos e uso intensivo.",
        "preco": 3299.99,
        "categoria": "Celulares",
        "especificacoes": {
            "Processador": "Snapdragon 8 Gen 2",
            "Memória RAM": "12GB",
            "Armazenamento": "256GB",
            "Tela": "6.7 polegadas AMOLED",
            "Câmera Principal": "108MP + 12MP Ultra-wide + 10MP Telephoto",
            "Bateria": "5000mAh"
        },
        "imagem": "smartphone.jpg"  # Substitua pelo caminho de uma imagem real
    },
    {
        "id": 3,
        "nome": "Monitor Ultrawide",
        "descricao": "Monitor ultrawide curvo para máxima produtividade e experiência imersiva em jogos. Proporciona amplo espaço de trabalho e qualidade de imagem excepcional.",
        "preco": 2499.99,
        "categoria": "Informática",
        "especificacoes": {
            "Tamanho": "34 polegadas",
            "Resolução": "3440 x 1440 (UWQHD)",
            "Taxa de Atualização": "144Hz",
            "Tempo de Resposta": "1ms",
            "Tecnologia": "IPS",
            "Conexões": "2x HDMI, 1x DisplayPort, USB-C"
        },
        "imagem": "monitor.jpg"  # Substitua pelo caminho de uma imagem real
    },
    {
        "id": 4,
        "nome": "Fone de Ouvido Bluetooth",
        "descricao": "Fone de ouvido sem fio com cancelamento de ruído ativo e qualidade de áudio premium. Ideal para música, chamadas e jogos.",
        "preco": 899.99,
        "categoria": "Áudio",
        "especificacoes": {
            "Tipo": "Over-ear",
            "Conectividade": "Bluetooth 5.2",
            "Autonomia": "Até 30 horas",
            "Cancelamento de Ruído": "Ativo (ANC)",
            "Microfone": "Integrado com redução de ruído",
            "Controles": "Touch na lateral"
        },
        "imagem": "fone.jpg"  # Substitua pelo caminho de uma imagem real
    },
    {
        "id": 5,
        "nome": "Teclado Mecânico Gamer",
        "descricao": "Teclado mecânico com switches premium, iluminação RGB personalizável e construção robusta. Projetado para gamers e digitadores intensivos.",
        "preco": 499.99,
        "categoria": "Periféricos",
        "especificacoes": {
            "Tipo": "Mecânico",
            "Switches": "Cherry MX Red",
            "Layout": "ABNT2",
            "Iluminação": "RGB por tecla",
            "Conexão": "USB-C destacável",
            "Extras": "Apoio de pulso e teclas multimídia"
        },
        "imagem": "teclado.jpg"  # Substitua pelo caminho de uma imagem real
    }
]

# Informações da loja
info_loja = {
    "nome": "TechStore",
    "slogan": "Tecnologia de ponta ao seu alcance",
    "endereco": "Av. Tecnologia, 1234 - São Paulo/SP",
    "telefone": "(11) 3456-7890",
    "site": "www.techstore.com.br",
    "email": "contato@techstore.com.br"
}
```

### Modelo de Solução
```python
# Solução do Exercício 1

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak, ListFlowable, ListItem
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.platypus.frames import Frame
from reportlab.platypus.doctemplate import PageTemplate, BaseDocTemplate
from reportlab.pdfgen import canvas
import os
from datetime import datetime

# Criar diretório para imagens de exemplo se não existir
if not os.path.exists("imagens"):
    os.makedirs("imagens")

# Criar imagens de exemplo se não existirem
def criar_imagem_exemplo(nome, cor):
    from PIL import Image, ImageDraw, ImageFont
    import os
    
    # Verificar se a imagem já existe
    if os.path.exists(f"imagens/{nome}"):
        return
    
    # Criar uma imagem de exemplo
    img = Image.new('RGB', (400, 300), color=cor)
    d = ImageDraw.Draw(img)
    
    # Tentar carregar uma fonte
    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except IOError:
        font = ImageFont.load_default()
    
    # Adicionar texto à imagem
    produto_nome = nome.split('.')[0].capitalize()
    d.text((100, 150), produto_nome, fill="white", font=font)
    
    # Salvar a imagem
    img.save(f"imagens/{nome}")

# Criar imagens de exemplo para os produtos
criar_imagem_exemplo("notebook.jpg", (41, 128, 185))  # Azul
criar_imagem_exemplo("smartphone.jpg", (39, 174, 96))  # Verde
criar_imagem_exemplo("monitor.jpg", (142, 68, 173))  # Roxo
criar_imagem_exemplo("fone.jpg", (211, 84, 0))  # Laranja
criar_imagem_exemplo("teclado.jpg", (192, 57, 43))  # Vermelho

# Dados dos produtos para o catálogo
produtos = [
    {
        "id": 1,
        "nome": "Notebook Profissional",
        "descricao": "Notebook de alto desempenho para profissionais. Ideal para tarefas exigentes como edição de vídeo, design gráfico e desenvolvimento de software.",
        "preco": 4599.99,
        "categoria": "Informática",
        "especificacoes": {
            "Processador": "Intel Core i7 11ª Geração",
            "Memória RAM": "16GB DDR4",
            "Armazenamento": "SSD 512GB",
            "Tela": "15.6 polegadas Full HD",
            "Placa de Vídeo": "NVIDIA GeForce RTX 3050 4GB",
            "Sistema Operacional": "Windows 11 Pro"
        },
        "imagem": "imagens/notebook.jpg"
    },
    {
        "id": 2,
        "nome": "Smartphone Premium",
        "descricao": "Smartphone de última geração com câmera profissional e bateria de longa duração. Perfeito para fotografia, jogos e uso intensivo.",
        "preco": 3299.99,
        "categoria": "Celulares",
        "especificacoes": {
            "Processador": "Snapdragon 8 Gen 2",
            "Memória RAM": "12GB",
            "Armazenamento": "256GB",
            "Tela": "6.7 polegadas AMOLED",
            "Câmera Principal": "108MP + 12MP Ultra-wide + 10MP Telephoto",
            "Bateria": "5000mAh"
        },
        "imagem": "imagens/smartphone.jpg"
    },
    {
        "id": 3,
        "nome": "Monitor Ultrawide",
        "descricao": "Monitor ultrawide curvo para máxima produtividade e experiência imersiva em jogos. Proporciona amplo espaço de trabalho e qualidade de imagem excepcional.",
        "preco": 2499.99,
        "categoria": "Informática",
        "especificacoes": {
            "Tamanho": "34 polegadas",
            "Resolução": "3440 x 1440 (UWQHD)",
            "Taxa de Atualização": "144Hz",
            "Tempo de Resposta": "1ms",
            "Tecnologia": "IPS",
            "Conexões": "2x HDMI, 1x DisplayPort, USB-C"
        },
        "imagem": "imagens/monitor.jpg"
    },
    {
        "id": 4,
        "nome": "Fone de Ouvido Bluetooth",
        "descricao": "Fone de ouvido sem fio com cancelamento de ruído ativo e qualidade de áudio premium. Ideal para música, chamadas e jogos.",
        "preco": 899.99,
        "categoria": "Áudio",
        "especificacoes": {
            "Tipo": "Over-ear",
            "Conectividade": "Bluetooth 5.2",
            "Autonomia": "Até 30 horas",
            "Cancelamento de Ruído": "Ativo (ANC)",
            "Microfone": "Integrado com redução de ruído",
            "Controles": "Touch na lateral"
        },
        "imagem": "imagens/fone.jpg"
    },
    {
        "id": 5,
        "nome": "Teclado Mecânico Gamer",
        "descricao": "Teclado mecânico com switches premium, iluminação RGB personalizável e construção robusta. Projetado para gamers e digitadores intensivos.",
        "preco": 499.99,
        "categoria": "Periféricos",
        "especificacoes": {
            "Tipo": "Mecânico",
            "Switches": "Cherry MX Red",
            "Layout": "ABNT2",
            "Iluminação": "RGB por tecla",
            "Conexão": "USB-C destacável",
            "Extras": "Apoio de pulso e teclas multimídia"
        },
        "imagem": "imagens/teclado.jpg"
    }
]

# Informações da loja
info_loja = {
    "nome": "TechStore",
    "slogan": "Tecnologia de ponta ao seu alcance",
    "endereco": "Av. Tecnologia, 1234 - São Paulo/SP",
    "telefone": "(11) 3456-7890",
    "site": "www.techstore.com.br",
    "email": "contato@techstore.com.br"
}

# Classe para criar o documento com cabeçalho e rodapé
class CatalogoPDF(BaseDocTemplate):
    def __init__(self, filename, **kwargs):
        BaseDocTemplate.__init__(self, filename, **kwargs)
        self.addPageTemplates(self._create_page_template())
        
    def _create_page_template(self):
        # Função para desenhar o cabeçalho
        def header(canvas, doc):
            canvas.saveState()
            # Não desenhar cabeçalho na primeira página (capa)
            if doc.page > 1:
                canvas.setFont('Helvetica-Bold', 10)
                canvas.setFillColor(colors.darkblue)
                canvas.drawString(inch, A4[1] - 0.5*inch, info_loja["nome"])
                canvas.setFont('Helvetica', 8)
                canvas.setFillColor(colors.black)
                canvas.drawString(inch, A4[1] - 0.7*inch, "Catálogo de Produtos")
                canvas.drawRightString(A4[0] - inch, A4[1] - 0.5*inch, datetime.now().strftime("%d/%m/%Y"))
                canvas.line(inch, A4[1] - 0.8*inch, A4[0] - inch, A4[1] - 0.8*inch)
            canvas.restoreState()
        
        # Função para desenhar o rodapé
        def footer(canvas, doc):
            canvas.saveState()
            # Não desenhar rodapé na primeira página (capa)
            if doc.page > 1:
                canvas.setFont('Helvetica', 8)
                canvas.setFillColor(colors.black)
                canvas.drawString(inch, 0.5*inch, f"Tel: {info_loja['telefone']} | Email: {info_loja['email']}")
                canvas.drawRightString(A4[0] - inch, 0.5*inch, f"Página {doc.page}")
                canvas.line(inch, 0.7*inch, A4[0] - inch, 0.7*inch)
            canvas.restoreState()
        
        # Criar frame para o conteúdo
        frame = Frame(
            inch, 
            inch, 
            A4[0] - 2*inch, 
            A4[1] - 2*inch, 
            leftPadding=0, 
            bottomPadding=0, 
            rightPadding=0, 
            topPadding=0
        )
        
        # Criar template de página com cabeçalho e rodapé
        template = PageTemplate(
            id='normal',
            frames=[frame],
            onPage=lambda canvas, doc: (header(canvas, doc), footer(canvas, doc))
        )
        
        return template

# Criar o documento PDF
pdf_filename = "catalogo_produtos.pdf"
doc = CatalogoPDF(
    pdf_filename,
    pagesize=A4,
    title="Catálogo de Produtos",
    author=info_loja["nome"]
)

# Definir estilos
styles = getSampleStyleSheet()

# Criar estilos personalizados
styles.add(ParagraphStyle(
    name='Titulo',
    parent=styles['Heading1'],
    fontSize=24,
    alignment=1,  # Centralizado
    spaceAfter=20,
    textColor=colors.darkblue
))

styles.add(ParagraphStyle(
    name='Subtitulo',
    parent=styles['Heading2'],
    fontSize=18,
    alignment=1,  # Centralizado
    spaceAfter=15,
    textColor=colors.darkblue
))

styles.add(ParagraphStyle(
    name='ProdutoTitulo',
    parent=styles['Heading2'],
    fontSize=16,
    textColor=colors.darkblue,
    spaceAfter=10
))

styles.add(ParagraphStyle(
    name='ProdutoCategoria',
    parent=styles['Normal'],
    fontSize=12,
    textColor=colors.darkgreen,
    spaceAfter=5
))

styles.add(ParagraphStyle(
    name='ProdutoPreco',
    parent=styles['Normal'],
    fontSize=14,
    textColor=colors.red,
    spaceAfter=10,
    fontName='Helvetica-Bold'
))

styles.add(ParagraphStyle(
    name='ProdutoDescricao',
    parent=styles['Normal'],
    fontSize=10,
    spaceAfter=15,
    leading=14
))

styles.add(ParagraphStyle(
    name='Rodape',
    parent=styles['Normal'],
    fontSize=8,
    textColor=colors.gray
))

styles.add(ParagraphStyle(
    name='Indice',
    parent=styles['Normal'],
    fontSize=12,
    spaceAfter=5
))

# Lista para armazenar os elementos do documento
elementos = []

# Adicionar capa
elementos.append(Spacer(1, 2*inch))
elementos.append(Paragraph(info_loja["nome"].upper(), styles["Titulo"]))
elementos.append(Paragraph(info_loja["slogan"], styles["Subtitulo"]))
elementos.append(Spacer(1, 1*inch))

# Adicionar imagem de logo na capa (usando a primeira imagem de produto como exemplo)
logo = Image(produtos[0]["imagem"], width=3*inch, height=2*inch)
logo.hAlign = 'CENTER'
elementos.append(logo)

elementos.append(Spacer(1, 1*inch))
elementos.append(Paragraph("CATÁLOGO DE PRODUTOS", styles["Titulo"]))
elementos.append(Paragraph(datetime.now().strftime("%B %Y"), styles["Subtitulo"]))
elementos.append(PageBreak())

# Adicionar índice
elementos.append(Paragraph("Índice", styles["Titulo"]))
toc = TableOfContents()
toc.levelStyles = [
    ParagraphStyle(name='TOCHeading1', fontSize=14, fontName='Helvetica-Bold'),
    ParagraphStyle(name='TOCHeading2', fontSize=12, fontName='Helvetica', leftIndent=20)
]
elementos.append(toc)
elementos.append(PageBreak())

# Adicionar introdução
elementos.append(Paragraph("Sobre Nossa Loja", styles["Titulo"]))
elementos.append(Paragraph(
    f"""Bem-vindo ao catálogo de produtos da {info_loja["nome"]}! 
    Somos especializados em produtos de tecnologia de alta qualidade, oferecendo as melhores marcas e modelos do mercado.
    Nossa missão é proporcionar a melhor experiência de compra, com atendimento personalizado e produtos que atendam às suas necessidades.
    """,
    styles["Normal"]
))

elementos.append(Spacer(1, 0.5*inch))

# Adicionar informações de contato
dados_contato = [
    ["Endereço:", info_loja["endereco"]],
    ["Telefone:", info_loja["telefone"]],
    ["Site:", info_loja["site"]],
    ["Email:", info_loja["email"]]
]

tabela_contato = Table(dados_contato, colWidths=[1.5*inch, 4*inch])
tabela_contato.setStyle(TableStyle([
    ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 10),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
]))

elementos.append(tabela_contato)
elementos.append(PageBreak())

# Adicionar páginas de produtos
for produto in produtos:
    # Adicionar título do produto (com bookmark para o índice)
    elementos.append(Paragraph(produto["nome"], styles["ProdutoTitulo"]))
    
    # Adicionar categoria e preço
    elementos.append(Paragraph(f"Categoria: {produto['categoria']}", styles["ProdutoCategoria"]))
    elementos.append(Paragraph(f"Preço: R$ {produto['preco']:.2f}", styles["ProdutoPreco"]))
    
    # Criar layout 
(Content truncated due to size limit. Use line ranges to read in chunks)