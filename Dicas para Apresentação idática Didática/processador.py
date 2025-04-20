import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from datetime import datetime

def carregar_dados(arquivo_csv='dados/produtos_extraidos.csv'):
    """Carrega os dados extraídos do CSV."""
    print(f"Carregando dados de {arquivo_csv}...")
    
    # Verificar se o arquivo existe
    if not os.path.exists(arquivo_csv):
        raise FileNotFoundError(f"Arquivo {arquivo_csv} não encontrado. Execute o extrator primeiro.")
    
    # Carregar dados
    df = pd.read_csv(arquivo_csv)
    print(f"Dados carregados com sucesso. {len(df)} produtos encontrados.")
    
    return df

def limpar_dados(df):
    """Limpa e prepara os dados para análise."""
    print("Limpando e preparando dados...")
    
    # Criar cópia para não modificar o original
    df_limpo = df.copy()
    
    # Remover linhas com valores ausentes em campos críticos
    df_limpo = df_limpo.dropna(subset=['titulo', 'preco_atual'])
    
    # Garantir tipos de dados corretos
    df_limpo['preco_atual'] = pd.to_numeric(df_limpo['preco_atual'], errors='coerce')
    df_limpo['preco_antigo'] = pd.to_numeric(df_limpo['preco_antigo'], errors='coerce')
    
    # Calcular desconto onde estiver faltando
    mascara_sem_desconto = df_limpo['desconto'].isna() & df_limpo['preco_antigo'].notna()
    df_limpo.loc[mascara_sem_desconto, 'desconto'] = (
        (1 - df_limpo.loc[mascara_sem_desconto, 'preco_atual'] / 
         df_limpo.loc[mascara_sem_desconto, 'preco_antigo']) * 100
    )
    
    # Arredondar desconto para 2 casas decimais
    df_limpo['desconto'] = df_limpo['desconto'].round(2)
    
    # Extrair categoria do título (simplificado)
    df_limpo['categoria'] = df_limpo['titulo'].str.split().str[0]
    
    # Adicionar coluna de economia (valor absoluto economizado)
    df_limpo['economia'] = df_limpo['preco_antigo'] - df_limpo['preco_atual']
    
    # Adicionar timestamp de processamento
    df_limpo['data_processamento'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    print(f"Limpeza concluída. {len(df_limpo)} produtos após limpeza.")
    
    return df_limpo

def analisar_dados(df):
    """Realiza análises nos dados e retorna um dicionário com os resultados."""
    print("Analisando dados...")
    
    resultados = {}
    
    # Estatísticas básicas
    resultados['total_produtos'] = len(df)
    resultados['preco_medio'] = df['preco_atual'].mean()
    resultados['desconto_medio'] = df['desconto'].mean()
    resultados['economia_total'] = df['economia'].sum()
    
    # Melhores ofertas (maior desconto)
    melhores_ofertas = df.sort_values('desconto', ascending=False).head(10)
    resultados['melhores_ofertas'] = melhores_ofertas
    
    # Ofertas com maior economia absoluta
    maior_economia = df.sort_values('economia', ascending=False).head(10)
    resultados['maior_economia'] = maior_economia
    
    # Análise por site
    analise_por_site = df.groupby('site').agg({
        'preco_atual': 'mean',
        'desconto': 'mean',
        'economia': 'sum',
        'titulo': 'count'
    }).rename(columns={'titulo': 'quantidade'})
    
    resultados['analise_por_site'] = analise_por_site
    
    # Análise por categoria
    analise_por_categoria = df.groupby('categoria').agg({
        'preco_atual': 'mean',
        'desconto': 'mean',
        'economia': 'sum',
        'titulo': 'count'
    }).rename(columns={'titulo': 'quantidade'})
    
    # Filtrar categorias com pelo menos 2 produtos
    analise_por_categoria = analise_por_categoria[analise_por_categoria['quantidade'] >= 2]
    
    resultados['analise_por_categoria'] = analise_por_categoria
    
    print("Análise concluída.")
    
    return resultados

def gerar_graficos(df, resultados):
    """Gera gráficos para visualização dos dados."""
    print("Gerando gráficos...")
    
    # Criar diretório para gráficos
    os.makedirs('dados/graficos', exist_ok=True)
    
    # Gráfico de barras: Desconto médio por site
    plt.figure(figsize=(10, 6))
    resultados['analise_por_site']['desconto'].plot(kind='bar', color='skyblue')
    plt.title('Desconto Médio por Site')
    plt.xlabel('Site')
    plt.ylabel('Desconto Médio (%)')
    plt.tight_layout()
    plt.savefig('dados/graficos/desconto_por_site.png')
    
    # Gráfico de dispersão: Preço x Desconto
    plt.figure(figsize=(10, 6))
    plt.scatter(df['preco_atual'], df['desconto'], alpha=0.6)
    plt.title('Relação entre Preço e Desconto')
    plt.xlabel('Preço Atual (R$)')
    plt.ylabel('Desconto (%)')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('dados/graficos/preco_vs_desconto.png')
    
    # Gráfico de pizza: Distribuição de produtos por site
    contagem_por_site = df['site'].value_counts()
    plt.figure(figsize=(10, 6))
    plt.pie(contagem_por_site, labels=contagem_por_site.index, autopct='%1.1f%%', 
            startangle=90, shadow=True)
    plt.axis('equal')
    plt.title('Distribuição de Produtos por Site')
    plt.tight_layout()
    plt.savefig('dados/graficos/distribuicao_por_site.png')
    
    # Histograma: Distribuição de descontos
    plt.figure(figsize=(10, 6))
    plt.hist(df['desconto'].dropna(), bins=20, color='lightgreen', edgecolor='black')
    plt.title('Distribuição de Descontos')
    plt.xlabel('Desconto (%)')
    plt.ylabel('Frequência')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('dados/graficos/distribuicao_descontos.png')
    
    print("Gráficos gerados com sucesso.")
    
    return {
        'desconto_por_site': 'dados/graficos/desconto_por_site.png',
        'preco_vs_desconto': 'dados/graficos/preco_vs_desconto.png',
        'distribuicao_por_site': 'dados/graficos/distribuicao_por_site.png',
        'distribuicao_descontos': 'dados/graficos/distribuicao_descontos.png'
    }

def processar_dados():
    """Função principal que orquestra todo o processamento de dados."""
    # Carregar dados
    df_original = carregar_dados()
    
    # Limpar dados
    df_limpo = limpar_dados(df_original)
    
    # Analisar dados
    resultados = analisar_dados(df_limpo)
    
    # Gerar gráficos
    graficos = gerar_graficos(df_limpo, resultados)
    
    # Salvar dados processados
    os.makedirs('dados', exist_ok=True)
    df_limpo.to_csv('dados/produtos_processados.csv', index=False)
    
    print("Processamento de dados concluído com sucesso.")
    
    return df_limpo, resultados, graficos

if __name__ == "__main__":
    processar_dados()
