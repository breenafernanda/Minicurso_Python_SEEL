#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Exemplo Prático: Análise de dados de produtos com Pandas

Este script demonstra como usar o Pandas para analisar dados de produtos
extraídos de sites de e-commerce, realizando limpeza, transformação,
análise estatística e visualização dos dados.

Conceitos demonstrados:
- Leitura de dados de arquivos JSON
- Limpeza e transformação de dados
- Análise exploratória
- Filtragem e seleção de dados
- Agrupamento e agregação
- Visualização com Matplotlib e Seaborn
- Exportação de resultados

Autor: Equipe do Minicurso de Automação com Python
Data: Abril de 2025
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import json
import os
import re
from datetime import datetime

# Configurações de visualização
plt.style.use('seaborn-v0_8-whitegrid')
sns.set(font_scale=1.1)
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.family'] = 'DejaVu Sans'

# Diretórios
DADOS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dados')
IMAGENS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'imagens')
os.makedirs(IMAGENS_DIR, exist_ok=True)

def carregar_dados(arquivo=None):
    """
    Carrega dados de produtos de um arquivo JSON.
    
    Args:
        arquivo (str, optional): Nome do arquivo específico a ser carregado.
            Se None, tenta carregar qualquer arquivo de produtos disponível.
    
    Returns:
        pandas.DataFrame: DataFrame com os dados dos produtos
    """
    # Se nenhum arquivo específico foi fornecido, procurar por arquivos de produtos
    if arquivo is None:
        arquivos_json = [f for f in os.listdir(DADOS_DIR) if f.startswith('produtos_') and f.endswith('.json')]
        if not arquivos_json:
            print("Nenhum arquivo de produtos encontrado. Gerando dados de exemplo...")
            return gerar_dados_exemplo()
        
        # Usar o arquivo mais recente
        arquivo = max(arquivos_json, key=lambda f: os.path.getmtime(os.path.join(DADOS_DIR, f)))
    
    caminho_arquivo = os.path.join(DADOS_DIR, arquivo)
    print(f"Carregando dados de: {caminho_arquivo}")
    
    try:
        # Carregar dados do JSON
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            dados = json.load(f)
        
        # Converter para DataFrame
        df = pd.DataFrame(dados)
        print(f"Dados carregados com sucesso: {len(df)} produtos")
        return df
    
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho_arquivo}")
        return gerar_dados_exemplo()
    
    except Exception as e:
        print(f"Erro ao carregar dados: {str(e)}")
        return gerar_dados_exemplo()

def gerar_dados_exemplo():
    """
    Gera um DataFrame de exemplo com dados fictícios de produtos.
    
    Returns:
        pandas.DataFrame: DataFrame com dados fictícios
    """
    print("Gerando dados de exemplo...")
    
    # Criar dados fictícios
    dados = []
    categorias = ['Informática', 'Eletrônicos', 'Celulares', 'Acessórios', 'Casa']
    
    for i in range(50):
        categoria = np.random.choice(categorias)
        preco_original = np.random.uniform(100, 5000)
        desconto = np.random.uniform(0, 0.4)
        preco_atual = preco_original * (1 - desconto)
        
        produto = {
            'nome': f'Produto Exemplo {i+1} - {categoria}',
            'categoria': categoria,
            'preco_atual': round(preco_atual, 2),
            'preco_original': round(preco_original, 2),
            'desconto': round(desconto * 100, 2),
            'avaliacao': round(np.random.uniform(1, 5), 1),
            'num_avaliacoes': np.random.randint(0, 1000),
            'link': f'https://exemplo.com/produto{i+1}',
            'imagem': f'https://exemplo.com/imagens/produto{i+1}.jpg',
            'disponivel': np.random.choice([True, False], p=[0.9, 0.1])
        }
        dados.append(produto)
    
    # Criar DataFrame
    df = pd.DataFrame(dados)
    
    # Salvar dados de exemplo
    caminho_arquivo = os.path.join(DADOS_DIR, 'produtos_exemplo.json')
    df.to_json(caminho_arquivo, orient='records', force_ascii=False, indent=4)
    print(f"Dados de exemplo salvos em: {caminho_arquivo}")
    
    return df

def limpar_dados(df):
    """
    Realiza limpeza e transformação dos dados.
    
    Args:
        df (pandas.DataFrame): DataFrame original
    
    Returns:
        pandas.DataFrame: DataFrame limpo e transformado
    """
    print("Limpando e transformando dados...")
    
    # Criar uma cópia para não modificar o original
    df_limpo = df.copy()
    
    # Remover duplicatas
    df_limpo = df_limpo.drop_duplicates(subset=['nome', 'preco_atual'], keep='first')
    
    # Tratar valores ausentes
    if 'preco_original' in df_limpo.columns:
        # Se preço original for nulo, usar preço atual
        df_limpo['preco_original'] = df_limpo['preco_original'].fillna(df_limpo['preco_atual'])
    
    if 'desconto' in df_limpo.columns:
        # Calcular desconto se estiver ausente
        mask_sem_desconto = df_limpo['desconto'].isna()
        if mask_sem_desconto.any() and 'preco_original' in df_limpo.columns:
            df_limpo.loc[mask_sem_desconto, 'desconto'] = (
                (df_limpo.loc[mask_sem_desconto, 'preco_original'] - 
                 df_limpo.loc[mask_sem_desconto, 'preco_atual']) / 
                df_limpo.loc[mask_sem_desconto, 'preco_original'] * 100
            )
        
        # Garantir que desconto seja zero quando preço atual >= preço original
        mask_desconto_invalido = df_limpo['preco_atual'] >= df_limpo['preco_original']
        df_limpo.loc[mask_desconto_invalido, 'desconto'] = 0.0
    
    # Tratar avaliações
    if 'avaliacao' in df_limpo.columns:
        df_limpo['avaliacao'] = df_limpo['avaliacao'].fillna(0)
    
    if 'num_avaliacoes' in df_limpo.columns:
        df_limpo['num_avaliacoes'] = df_limpo['num_avaliacoes'].fillna(0).astype(int)
    
    # Extrair categoria do nome se não existir coluna de categoria
    if 'categoria' not in df_limpo.columns:
        # Tentar extrair categoria do nome ou de outro campo
        df_limpo['categoria'] = 'Não categorizado'
        
        # Exemplo: extrair categoria com base em palavras-chave no nome
        categorias_keywords = {
            'Informática': ['notebook', 'computador', 'mouse', 'teclado', 'monitor'],
            'Celulares': ['smartphone', 'celular', 'iphone', 'galaxy'],
            'Eletrônicos': ['tv', 'televisão', 'fone', 'headset', 'câmera', 'camera'],
            'Casa': ['panela', 'fogão', 'geladeira', 'sofá', 'cama', 'mesa']
        }
        
        for idx, row in df_limpo.iterrows():
            nome_lower = row['nome'].lower()
            for categoria, keywords in categorias_keywords.items():
                if any(keyword in nome_lower for keyword in keywords):
                    df_limpo.at[idx, 'categoria'] = categoria
                    break
    
    # Adicionar coluna de faixa de preço
    df_limpo['faixa_preco'] = pd.cut(
        df_limpo['preco_atual'],
        bins=[0, 100, 500, 1000, 2000, float('inf')],
        labels=['Até R$100', 'R$100-500', 'R$500-1000', 'R$1000-2000', 'Acima de R$2000']
    )
    
    # Adicionar coluna de faixa de desconto
    if 'desconto' in df_limpo.columns:
        df_limpo['faixa_desconto'] = pd.cut(
            df_limpo['desconto'],
            bins=[-0.1, 0, 10, 20, 30, 100],
            labels=['Sem desconto', 'Até 10%', '10-20%', '20-30%', 'Acima de 30%']
        )
    
    # Adicionar coluna de economia (valor economizado)
    if 'preco_original' in df_limpo.columns and 'preco_atual' in df_limpo.columns:
        df_limpo['economia'] = df_limpo['preco_original'] - df_limpo['preco_atual']
        df_limpo.loc[df_limpo['economia'] < 0, 'economia'] = 0
    
    print(f"Dados limpos: {len(df_limpo)} produtos após remoção de duplicatas")
    return df_limpo

def analisar_dados(df):
    """
    Realiza análise exploratória dos dados.
    
    Args:
        df (pandas.DataFrame): DataFrame com os dados
    """
    print("\n" + "="*50)
    print("ANÁLISE EXPLORATÓRIA DOS DADOS")
    print("="*50)
    
    # Informações gerais
    print("\nInformações gerais:")
    print(f"Total de produtos: {len(df)}")
    
    if 'categoria' in df.columns:
        categorias = df['categoria'].value_counts()
        print(f"\nDistribuição por categoria:")
        for categoria, count in categorias.items():
            print(f"  {categoria}: {count} produtos ({count/len(df)*100:.1f}%)")
    
    # Estatísticas de preço
    print("\nEstatísticas de preço (R$):")
    preco_stats = df['preco_atual'].describe()
    print(f"  Média: R$ {preco_stats['mean']:.2f}")
    print(f"  Mediana: R$ {preco_stats['50%']:.2f}")
    print(f"  Mínimo: R$ {preco_stats['min']:.2f}")
    print(f"  Máximo: R$ {preco_stats['max']:.2f}")
    
    # Estatísticas de desconto
    if 'desconto' in df.columns:
        print("\nEstatísticas de desconto (%):")
        desconto_stats = df['desconto'].describe()
        print(f"  Média: {desconto_stats['mean']:.2f}%")
        print(f"  Mediana: {desconto_stats['50%']:.2f}%")
        print(f"  Máximo: {desconto_stats['max']:.2f}%")
        print(f"  Produtos com desconto: {(df['desconto'] > 0).sum()} ({(df['desconto'] > 0).sum()/len(df)*100:.1f}%)")
    
    # Estatísticas de avaliação
    if 'avaliacao' in df.columns:
        # Filtrar produtos com avaliação
        df_com_avaliacao = df[df['avaliacao'] > 0]
        if not df_com_avaliacao.empty:
            print("\nEstatísticas de avaliação:")
            avaliacao_stats = df_com_avaliacao['avaliacao'].describe()
            print(f"  Média: {avaliacao_stats['mean']:.1f}/5.0")
            print(f"  Produtos com avaliação: {len(df_com_avaliacao)} ({len(df_com_avaliacao)/len(df)*100:.1f}%)")
    
    # Top 5 produtos mais caros
    print("\nTop 5 produtos mais caros:")
    top_caros = df.sort_values('preco_atual', ascending=False).head(5)
    for i, (_, row) in enumerate(top_caros.iterrows(), 1):
        print(f"  {i}. {row['nome']} - R$ {row['preco_atual']:.2f}")
    
    # Top 5 produtos com maior desconto
    if 'desconto' in df.columns:
        print("\nTop 5 produtos com maior desconto:")
        top_descontos = df[df['desconto'] > 0].sort_values('desconto', ascending=False).head(5)
        for i, (_, row) in enumerate(top_descontos.iterrows(), 1):
            print(f"  {i}. {row['nome']} - {row['desconto']:.2f}% de desconto")
    
    # Análise por categoria
    if 'categoria' in df.columns:
        print("\nPreço médio por categoria:")
        preco_medio_categoria = df.groupby('categoria')['preco_atual'].mean().sort_values(ascending=False)
        for categoria, preco in preco_medio_categoria.items():
            print(f"  {categoria}: R$ {preco:.2f}")
        
        if 'desconto' in df.columns:
            print("\nDesconto médio por categoria:")
            desconto_medio_categoria = df.groupby('categoria')['desconto'].mean().sort_values(ascending=False)
            for categoria, desconto in desconto_medio_categoria.items():
                print(f"  {categoria}: {desconto:.2f}%")

def visualizar_dados(df):
    """
    Cria visualizações dos dados para análise.
    
    Args:
        df (pandas.DataFrame): DataFrame com os dados
    
    Returns:
        list: Lista de caminhos para as imagens geradas
    """
    print("\nCriando visualizações dos dados...")
    imagens = []
    
    # Configurar estilo
    sns.set_style("whitegrid")
    plt.rcParams['axes.labelsize'] = 12
    plt.rcParams['axes.titlesize'] = 14
    
    # 1. Distribuição de preços
    plt.figure(figsize=(12, 6))
    sns.histplot(data=df, x='preco_atual', bins=20, kde=True)
    plt.title('Distribuição de Preços')
    plt.xlabel('Preço (R$)')
    plt.ylabel('Frequência')
    plt.axvline(df['preco_atual'].mean(), color='red', linestyle='--', label=f'Média: R${df["preco_atual"].mean():.2f}')
    plt.axvline(df['preco_atual'].median(), color='green', linestyle='--', label=f'Mediana: R${df["preco_atual"].median():.2f}')
    plt.legend()
    plt.tight_layout()
    
    # Salvar figura
    caminho_fig1 = os.path.join(IMAGENS_DIR, 'distribuicao_precos.png')
    plt.savefig(caminho_fig1, dpi=300, bbox_inches='tight')
    imagens.append(caminho_fig1)
    plt.close()
    
    # 2. Preço médio por categoria
    if 'categoria' in df.columns:
        plt.figure(figsize=(12, 6))
        categoria_preco = df.groupby('categoria')['preco_atual'].mean().sort_values(ascending=False)
        
        ax = sns.barplot(x=categoria_preco.index, y=categoria_preco.values)
        plt.title('Preço Médio por Categoria')
        plt.xlabel('Categoria')
        plt.ylabel('Preço Médio (R$)')
        plt.xticks(rotation=45, ha='right')
        
        # Adicionar valores nas barras
        for i, v in enumerate(categoria_preco.values):
            ax.text(i, v + 50, f'R${v:.2f}', ha='center')
        
        plt.tight_layout()
        
        # Salvar figura
        caminho_fig2 = os.path.join(IMAGENS_DIR, 'preco_medio_categoria.png')
        plt.savefig(caminho_fig2, dpi=300, bbox_inches='tight')
        imagens.append(caminho_fig2)
        plt.close()
    
    # 3. Distribuição de descontos
    if 'desconto' in df.columns:
        plt.figure(figsize=(12, 6))
        # Filtrar apenas produtos com desconto
        df_com_desconto = df[df['desconto'] > 0]
        if not df_com_desconto.empty:
            sns.histplot(data=df_com_desconto, x='desconto', bins=10, kde=True)
            plt.title('Distribuição de Descontos')
            plt.xlabel('Desconto (%)')
            plt.ylabel('Frequência')
            plt.axvline(df_com_desconto['desconto'].mean(), color='red', linestyle='--', 
                       label=f'Média: {df_com_desconto["desconto"].mean():.2f}%')
            plt.legend()
        else:
            plt.text(0.5, 0.5, 'Não há produtos com desconto', 
                    horizontalalignment='center', verticalalignment='center',
                    transform=plt.gca().transAxes, fontsize=14)
        
        plt.tight_layout()
        
        # Salvar figura
        caminho_fig3 = os.path.join(IMAGENS_DIR, 'distribuicao_descontos.png')
        plt.savefig(caminho_fig3, dpi=300, bbox_inches='tight')
        imagens.append(caminho_fig3)
        plt.close()
    
    # 4. Relação entre preço e desconto
    if 'desconto' in df.columns:
        plt.figure(figsize=(12, 6))
        sns.scatterplot(data=df, x='preco_atual', y='desconto', hue='categoria' if 'categoria' in df.columns else None,
                       alpha=0.7, s=100)
        plt.title('Relação entre Preço e Desconto')
        plt.xlabel('Preço (R$)')
        plt.ylabel('Desconto (%)')
        if 'categoria' in df.columns:
            plt.legend(title='Categoria', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        
        # Salvar figura
        caminho_fig4 = os.path.join(IMAGENS_DIR, 'relacao_preco_desconto.png')
        plt.savefig(caminho_fig4, dpi=300, bbox_inches='tight')
        imagens.append(caminho_fig4)
        plt.close()
    
    # 5. Boxplot de preços por categoria
    if 'categoria' in df.columns:
        plt.figure(figsize=(12, 6))
        sns.boxplot(data=df, x='categoria', y='preco_atual')
        plt.title('Distribuição de Preços por Categoria')
        plt.xlabel('Categoria')
        plt.ylabel('Preço (R$)')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        
        # Salvar figura
        caminho_fig5 = os.path.join(IMAGENS_DIR, 'boxplot_precos_categoria.png')
        plt.savefig(caminho_fig5, dpi=300, bbox_inches='tight')
        imagens.append(caminho_fig5)
        plt.close()
    
    # 6. Contagem de produtos por faixa de preço
    plt.figure(figsize=(12, 6))
    sns.countplot(data=df, x='faixa_preco', order=df['faixa_preco'].value_counts().index)
    plt.title('Quantidade de Produtos por Faixa de Preço')
    pl
(Content truncated due to size limit. Use line ranges to read in chunks)