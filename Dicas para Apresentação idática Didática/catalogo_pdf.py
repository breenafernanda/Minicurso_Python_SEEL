import os
import requests
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak
from reportlab.platypus.flowables import HRFlowable
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from datetime import datetime
import pandas as pd
from PIL import Image as PILImage

def baixar_imagem(url, tamanho_max=(200, 200)):
    """Baixa uma imagem da web e redimensiona para o tamanho especificado."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Abrir imagem com PIL
        img = PILImage.open(BytesIO(response.content))
        
        # Redimensionar mantendo proporção
        img.thumbnail(tamanho_max, PILImage.LANCZOS)
        
        # Salvar em buffer de memória
        img_buffer = BytesIO()
        if img.mode != 'RGB':
            img = img.convert('RGB')
        img.save(img_buffer, format='JPEG')
        img_buffer.seek(0)
        
        return img_buffer
    except Exception as e:
        print(f"Erro ao baixar imagem {url}: {e}")
        return None

def criar_primeira_pagina(canvas, doc):
    """Cria a primeira página do catálogo com capa personalizada."""
    canvas.saveState()
    
    # Fundo colorido
    canvas.setFillColorRGB(0.2, 0.4, 0.6)
    canvas.rect(0, 0, A4[0], A4[1], fill=1)
    
    # Título
    canvas.setFillColorRGB(1, 1, 1)
    canvas.setFont("Helvetica-Bold", 30)
    title = "CATÁLOGO DE OFERTAS"
    title_width = canvas.stringWidth(title, "Helvetica-Bold", 30)
    canvas.drawString((A4[0] - title_width) / 2, A4[1] - 150, title)
    
    # Subtítulo
    canvas.setFont("Helvetica", 16)
    subtitle = "As melhores promoções encontradas para você"
    subtitle_width = canvas.stringWidth(subtitle, "Helvetica", 16)
    canvas.drawString((A4[0] - subtitle_width) / 2, A4[1] - 180, subtitle)
    
    # Data
    data_atual = datetime.now().strftime("%d/%m/%Y")
    canvas.setFont("Helvetica", 12)
    canvas.drawString(A4[0] - 120, 30, f"Data: {data_atual}")
    
    canvas.restoreState()

def criar_cabecalho_rodape(canvas, doc):
    """Adiciona cabeçalho e rodapé às páginas do catálogo."""
    canvas.saveState()
    
    # Cabeçalho
    canvas.setFillColorRGB(0.2, 0.4, 0.6)
    canvas.rect(0, A4[1] - 40, A4[0], 40, fill=1)
    
    canvas.setFillColorRGB(1, 1, 1)
    canvas.setFont("Helvetica-Bold", 12)
    canvas.drawString(30, A4[1] - 25, "CATÁLOGO DE OFERTAS")
    
    # Rodapé
    canvas.setFillColorRGB(0.2, 0.4, 0.6)
    canvas.rect(0, 0, A4[0], 30, fill=1)
    
    canvas.setFillColorRGB(1, 1, 1)
    canvas.setFont("Helvetica", 10)
    canvas.drawString(30, 15, "Gerado automaticamente com Python")
    canvas.drawString(A4[0] - 100, 15, f"Página {doc.page}")
    
    canvas.restoreState()

def criar_catalogo_pdf(df, caminho_saida='output/catalogo_ofertas.pdf'):
    """
    Cria um catálogo em PDF com os produtos em promoção.
    
    Args:
        df: DataFrame com os dados dos produtos
        caminho_saida: Caminho onde o arquivo PDF será salvo
    """
    print(f"Criando catálogo PDF em {caminho_saida}...")
    
    # Criar diretório de saída se não existir
    os.makedirs(os.path.dirname(caminho_saida), exist_ok=True)
    
    # Configurar documento
    doc = SimpleDocTemplate(
        caminho_saida,
        pagesize=A4,
        leftMargin=2*cm,
        rightMargin=2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm
    )
    
    # Estilos
    styles = getSampleStyleSheet()
    
    # Estilo personalizado para título de produto
    styles.add(ParagraphStyle(
        name='ProdutoTitulo',
        parent=styles['Heading2'],
        textColor=colors.darkblue,
        spaceAfter=5
    ))
    
    # Estilo personalizado para preço
    styles.add(ParagraphStyle(
        name='Preco',
        parent=styles['Normal'],
        fontSize=14,
        textColor=colors.red,
        fontName='Helvetica-Bold'
    ))
    
    # Estilo personalizado para desconto
    styles.add(ParagraphStyle(
        name='Desconto',
        parent=styles['Normal'],
        fontSize=12,
        textColor=colors.green,
        fontName='Helvetica-Bold'
    ))
    
    # Estilo personalizado para descrição
    styles.add(ParagraphStyle(
        name='Descricao',
        parent=styles['Normal'],
        fontSize=10,
        leading=12
    ))
    
    # Elementos do documento
    elementos = []
    
    # Adicionar página de capa (será substituída pelo callback)
    elementos.append(Spacer(1, 1))
    elementos.append(PageBreak())
    
    # Introdução
    elementos.append(Paragraph("Ofertas Selecionadas", styles['Heading1']))
    elementos.append(Spacer(1, 0.5*cm))
    elementos.append(Paragraph(
        "Este catálogo apresenta as melhores ofertas encontradas em diversos sites de e-commerce. "
        "Os produtos foram selecionados com base no percentual de desconto e na economia proporcionada. "
        "Aproveite estas oportunidades!",
        styles['Normal']
    ))
    elementos.append(Spacer(1, 1*cm))
    
    # Filtrar produtos com os maiores descontos
    if 'desconto' in df.columns:
        df_catalogo = df.sort_values('desconto', ascending=False).head(15)
    else:
        df_catalogo = df.head(15)
    
    # Adicionar cada produto ao catálogo
    for i, (_, produto) in enumerate(df_catalogo.iterrows()):
        # Separador entre produtos
        if i > 0:
            elementos.append(HRFlowable(
                width="100%",
                thickness=1,
                color=colors.lightgrey,
                spaceBefore=0.5*cm,
                spaceAfter=0.5*cm
            ))
        
        # Título do produto
        titulo = produto['titulo']
        elementos.append(Paragraph(titulo, styles['ProdutoTitulo']))
        
        # Tabela com imagem e informações
        dados_tabela = []
        
        # Tentar baixar a imagem
        imagem_buffer = None
        if 'imagem_url' in produto and pd.notna(produto['imagem_url']):
            imagem_buffer = baixar_imagem(produto['imagem_url'])
        
        if imagem_buffer:
            img = Image(imagem_buffer, width=150, height=150)
            
            # Informações do produto
            info = []
            
            # Site
            info.append(Paragraph(f"<b>Site:</b> {produto['site']}", styles['Normal']))
            info.append(Spacer(1, 0.2*cm))
            
            # Preços
            preco_atual = f"R$ {produto['preco_atual']:.2f}" if pd.notna(produto['preco_atual']) else "N/A"
            info.append(Paragraph(f"<b>Preço Atual:</b> {preco_atual}", styles['Preco']))
            
            if 'preco_antigo' in produto and pd.notna(produto['preco_antigo']):
                preco_antigo = f"R$ {produto['preco_antigo']:.2f}"
                info.append(Paragraph(f"<b>Preço Antigo:</b> <strike>{preco_antigo}</strike>", styles['Normal']))
            
            info.append(Spacer(1, 0.2*cm))
            
            # Desconto e economia
            if 'desconto' in produto and pd.notna(produto['desconto']):
                info.append(Paragraph(f"<b>Desconto:</b> {produto['desconto']:.2f}%", styles['Desconto']))
            
            if 'economia' in produto and pd.notna(produto['economia']):
                info.append(Paragraph(f"<b>Economia:</b> R$ {produto['economia']:.2f}", styles['Normal']))
            
            # Link
            if 'link' in produto and pd.notna(produto['link']):
                link_text = produto['link']
                if len(link_text) > 50:
                    link_text = link_text[:47] + "..."
                info.append(Spacer(1, 0.2*cm))
                info.append(Paragraph(f"<b>Link:</b> <font color='blue'><u>{link_text}</u></font>", styles['Normal']))
            
            # Adicionar linha à tabela
            dados_tabela.append([img, info])
            
            # Criar tabela
            tabela = Table(dados_tabela, colWidths=[160, 300])
            tabela.setStyle(TableStyle([
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('ALIGN', (0, 0), (0, -1), 'CENTER'),
                ('LEFTPADDING', (0, 0), (-1, -1), 0),
                ('RIGHTPADDING', (0, 0), (-1, -1), 0),
            ]))
            
            elementos.append(tabela)
        else:
            # Se não conseguir baixar a imagem, mostrar apenas as informações
            elementos.append(Paragraph(f"<b>Site:</b> {produto['site']}", styles['Normal']))
            
            preco_atual = f"R$ {produto['preco_atual']:.2f}" if pd.notna(produto['preco_atual']) else "N/A"
            elementos.append(Paragraph(f"<b>Preço Atual:</b> {preco_atual}", styles['Preco']))
            
            if 'preco_antigo' in produto and pd.notna(produto['preco_antigo']):
                preco_antigo = f"R$ {produto['preco_antigo']:.2f}"
                elementos.append(Paragraph(f"<b>Preço Antigo:</b> <strike>{preco_antigo}</strike>", styles['Normal']))
            
            if 'desconto' in produto and pd.notna(produto['desconto']):
                elementos.append(Paragraph(f"<b>Desconto:</b> {produto['desconto']:.2f}%", styles['Desconto']))
            
            if 'economia' in produto and pd.notna(produto['economia']):
                elementos.append(Paragraph(f"<b>Economia:</b> R$ {produto['economia']:.2f}", styles['Normal']))
            
            if 'link' in produto and pd.notna(produto['link']):
                link_text = produto['link']
                if len(link_text) > 50:
                    link_text = link_text[:47] + "..."
                elementos.append(Paragraph(f"<b>Link:</b> <font color='blue'><u>{link_text}</u></font>", styles['Normal']))
        
        # Espaço após o produto
        elementos.append(Spacer(1, 0.5*cm))
    
    # Página final com estatísticas
    elementos.append(PageBreak())
    elementos.append(Paragraph("Resumo das Ofertas", styles['Heading1']))
    elementos.append(Spacer(1, 0.5*cm))
    
    # Estatísticas básicas
    estatisticas = [
        ["Total de Produtos", str(len(df))],
        ["Desconto Médio", f"{df['desconto'].mean():.2f}%" if 'desconto' in df.columns else "N/A"],
        ["Economia Total", f"R$ {df['economia'].sum():.2f}" if 'economia' in df.columns else "N/A"],
        ["Preço Médio", f"R$ {df['preco_atual'].mean():.2f}" if 'preco_atual' in df.columns else "N/A"]
    ]
    
    tabela_estatisticas = Table(estatisticas, colWidths=[200, 200])
    tabela_estatisticas.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.lightblue),
        ('TEXTCOLOR', (0, 0), (0, -1), colors.darkblue),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    
    elementos.append(tabela_estatisticas)
    elementos.append(Spacer(1, 1*cm))
    
    # Nota final
    elementos.append(Paragraph(
        "Nota: Os preços e disponibilidade dos produtos podem mudar a qualquer momento. "
        "Este catálogo foi gerado automaticamente em " + datetime.now().strftime("%d/%m/%Y às %H:%M") + ".",
        styles['Italic']
    ))
    
    # Construir o documento com callbacks para primeira página e páginas subsequentes
    doc.build(
        elementos,
        onFirstPage=criar_primeira_pagina,
        onLaterPages=criar_cabecalho_rodape
    )
    
    print(f"Catálogo PDF criado com sucesso em {caminho_saida}")
    
    return caminho_saida

def gerar_catalogo_pdf(df=None):
    """Função principal para gerar o catálogo PDF."""
    # Se não foram fornecidos dados, carregar do arquivo
    if df is None:
        import processador
        df, _, _ = processador.processar_dados()
    
    # Criar catálogo PDF
    caminho_catalogo = criar_catalogo_pdf(df)
    
    return caminho_catalogo

if __name__ == "__main__":
    gerar_catalogo_pdf()
