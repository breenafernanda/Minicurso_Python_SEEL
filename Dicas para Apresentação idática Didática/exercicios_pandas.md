# Exercícios Práticos: Pandas para Análise de Dados

## Exercício 1: Análise de Vendas

### Objetivo
Praticar a importação, limpeza e análise básica de dados com Pandas.

### Enunciado
Você recebeu um arquivo CSV com dados de vendas de uma loja e precisa analisar o desempenho das vendas. Sua tarefa é:
1. Importar os dados do arquivo CSV
2. Limpar e preparar os dados para análise
3. Calcular estatísticas básicas (total de vendas, média, etc.)
4. Analisar vendas por categoria e por mês
5. Criar visualizações para apresentar os resultados

### Dados de Entrada
Crie um arquivo `vendas.csv` com o seguinte conteúdo:
```
data,produto,categoria,preco,quantidade,vendedor
2025-01-05,Notebook Dell,Informática,3599.99,2,João
2025-01-12,Mouse sem fio,Informática,89.90,5,Maria
2025-01-18,Teclado mecânico,Informática,259.50,3,Pedro
2025-01-25,Monitor 24 polegadas,Informática,799.00,2,João
2025-02-03,Smartphone Samsung,Celulares,1899.00,1,Maria
2025-02-10,iPhone 13,Celulares,5999.00,1,Pedro
2025-02-15,Carregador wireless,Acessórios,99.90,8,João
2025-02-22,Capa para celular,Acessórios,49.90,10,Maria
2025-03-05,Película de vidro,Acessórios,29.90,15,Pedro
2025-03-12,Notebook Lenovo,Informática,2899.99,2,João
2025-03-18,Tablet Samsung,Informática,1299.00,3,Maria
2025-03-25,Fone de ouvido,Acessórios,199.90,7,Pedro
```

### Modelo de Solução
```python
# Solução do Exercício 1

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Configurar visualização
plt.style.use('ggplot')
sns.set(style="whitegrid")

# Importar dados
df = pd.read_csv('vendas.csv')

# Exibir primeiras linhas para verificar a importação
print("Primeiras linhas do DataFrame:")
print(df.head())

# Verificar informações do DataFrame
print("\nInformações do DataFrame:")
print(df.info())

# Verificar estatísticas básicas
print("\nEstatísticas descritivas:")
print(df.describe())

# Verificar valores nulos
print("\nValores nulos por coluna:")
print(df.isnull().sum())

# Preparação dos dados
# Converter a coluna de data para o tipo datetime
df['data'] = pd.to_datetime(df['data'])

# Criar colunas adicionais para análise
df['mes'] = df['data'].dt.month
df['mes_nome'] = df['data'].dt.strftime('%B')  # Nome do mês
df['valor_total'] = df['preco'] * df['quantidade']

# Análise de vendas totais
total_vendas = df['valor_total'].sum()
media_por_venda = df['valor_total'].mean()
maior_venda = df['valor_total'].max()
menor_venda = df['valor_total'].min()

print("\nAnálise de Vendas:")
print(f"Total de vendas: R$ {total_vendas:.2f}")
print(f"Média por venda: R$ {media_por_venda:.2f}")
print(f"Maior venda: R$ {maior_venda:.2f}")
print(f"Menor venda: R$ {menor_venda:.2f}")

# Análise por categoria
vendas_por_categoria = df.groupby('categoria')['valor_total'].sum().reset_index()
print("\nVendas por Categoria:")
print(vendas_por_categoria)

# Análise por mês
vendas_por_mes = df.groupby(['mes', 'mes_nome'])['valor_total'].sum().reset_index()
vendas_por_mes = vendas_por_mes.sort_values('mes')
print("\nVendas por Mês:")
print(vendas_por_mes)

# Análise por vendedor
vendas_por_vendedor = df.groupby('vendedor')['valor_total'].sum().reset_index()
vendas_por_vendedor = vendas_por_vendedor.sort_values('valor_total', ascending=False)
print("\nVendas por Vendedor:")
print(vendas_por_vendedor)

# Produtos mais vendidos (por quantidade)
produtos_mais_vendidos = df.groupby('produto')['quantidade'].sum().reset_index()
produtos_mais_vendidos = produtos_mais_vendidos.sort_values('quantidade', ascending=False).head(5)
print("\nProdutos Mais Vendidos (por quantidade):")
print(produtos_mais_vendidos)

# Produtos mais lucrativos (por valor total)
produtos_mais_lucrativos = df.groupby('produto')['valor_total'].sum().reset_index()
produtos_mais_lucrativos = produtos_mais_lucrativos.sort_values('valor_total', ascending=False).head(5)
print("\nProdutos Mais Lucrativos (por valor total):")
print(produtos_mais_lucrativos)

# Visualizações

# 1. Gráfico de barras - Vendas por Categoria
plt.figure(figsize=(10, 6))
sns.barplot(x='categoria', y='valor_total', data=vendas_por_categoria)
plt.title('Vendas por Categoria')
plt.xlabel('Categoria')
plt.ylabel('Valor Total (R$)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('vendas_por_categoria.png')
plt.close()

# 2. Gráfico de linha - Vendas por Mês
plt.figure(figsize=(10, 6))
sns.lineplot(x='mes_nome', y='valor_total', data=vendas_por_mes, marker='o')
plt.title('Vendas por Mês')
plt.xlabel('Mês')
plt.ylabel('Valor Total (R$)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('vendas_por_mes.png')
plt.close()

# 3. Gráfico de barras - Vendas por Vendedor
plt.figure(figsize=(10, 6))
sns.barplot(x='vendedor', y='valor_total', data=vendas_por_vendedor)
plt.title('Vendas por Vendedor')
plt.xlabel('Vendedor')
plt.ylabel('Valor Total (R$)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('vendas_por_vendedor.png')
plt.close()

# 4. Gráfico de pizza - Distribuição de Vendas por Categoria
plt.figure(figsize=(8, 8))
plt.pie(vendas_por_categoria['valor_total'], labels=vendas_por_categoria['categoria'], 
        autopct='%1.1f%%', startangle=90, shadow=True)
plt.title('Distribuição de Vendas por Categoria')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.tight_layout()
plt.savefig('distribuicao_vendas_categoria.png')
plt.close()

# 5. Gráfico de barras horizontais - Produtos Mais Lucrativos
plt.figure(figsize=(12, 6))
sns.barplot(y='produto', x='valor_total', data=produtos_mais_lucrativos)
plt.title('Produtos Mais Lucrativos')
plt.xlabel('Valor Total (R$)')
plt.ylabel('Produto')
plt.tight_layout()
plt.savefig('produtos_mais_lucrativos.png')
plt.close()

# Salvar análise em um arquivo Excel
with pd.ExcelWriter('analise_vendas.xlsx') as writer:
    df.to_excel(writer, sheet_name='Dados Brutos', index=False)
    vendas_por_categoria.to_excel(writer, sheet_name='Vendas por Categoria', index=False)
    vendas_por_mes.to_excel(writer, sheet_name='Vendas por Mês', index=False)
    vendas_por_vendedor.to_excel(writer, sheet_name='Vendas por Vendedor', index=False)
    produtos_mais_vendidos.to_excel(writer, sheet_name='Produtos Mais Vendidos', index=False)
    produtos_mais_lucrativos.to_excel(writer, sheet_name='Produtos Mais Lucrativos', index=False)

print("\nAnálise concluída! Resultados salvos em 'analise_vendas.xlsx' e gráficos gerados.")
```

## Exercício 2: Análise de Dados de E-commerce

### Objetivo
Praticar a limpeza, transformação e análise de dados de e-commerce com Pandas.

### Enunciado
Você recebeu um conjunto de dados de vendas de um site de e-commerce e precisa realizar uma análise detalhada. Sua tarefa é:
1. Importar e limpar os dados
2. Analisar o comportamento de compra dos clientes
3. Identificar produtos mais populares e categorias mais lucrativas
4. Analisar tendências de vendas ao longo do tempo
5. Criar um dashboard com visualizações dos resultados

### Dados de Entrada
Crie um arquivo `ecommerce_vendas.csv` com o seguinte conteúdo:
```
id_pedido,data_pedido,id_cliente,cidade,estado,id_produto,categoria,preco_unitario,quantidade,frete,pagamento
1001,2025-01-05,C001,São Paulo,SP,P101,Eletrônicos,1299.99,1,25.50,Cartão de Crédito
1001,2025-01-05,C001,São Paulo,SP,P203,Acessórios,89.90,2,25.50,Cartão de Crédito
1002,2025-01-07,C002,Rio de Janeiro,RJ,P105,Eletrônicos,2499.99,1,32.80,Boleto
1003,2025-01-10,C003,Belo Horizonte,MG,P102,Eletrônicos,899.90,1,28.90,Cartão de Crédito
1004,2025-01-12,C004,Curitiba,PR,P304,Casa e Decoração,159.90,3,22.50,Pix
1005,2025-01-15,C005,Porto Alegre,RS,P201,Acessórios,129.90,1,30.00,Cartão de Crédito
1005,2025-01-15,C005,Porto Alegre,RS,P205,Acessórios,49.90,2,30.00,Cartão de Crédito
1006,2025-01-18,C001,São Paulo,SP,P301,Casa e Decoração,299.90,1,25.50,Pix
1007,2025-01-20,C006,Salvador,BA,P103,Eletrônicos,1899.90,1,35.80,Cartão de Crédito
1008,2025-01-22,C007,Recife,PE,P202,Acessórios,79.90,3,33.20,Boleto
1009,2025-01-25,C008,Brasília,DF,P104,Eletrônicos,3299.99,1,29.90,Cartão de Crédito
1010,2025-01-28,C009,Fortaleza,CE,P302,Casa e Decoração,199.90,2,34.50,Pix
1011,2025-01-30,C010,Manaus,AM,P204,Acessórios,149.90,1,45.00,Cartão de Crédito
1012,2025-02-02,C002,Rio de Janeiro,RJ,P303,Casa e Decoração,259.90,1,32.80,Cartão de Crédito
1013,2025-02-05,C011,Goiânia,GO,P101,Eletrônicos,1299.99,1,31.20,Boleto
1014,2025-02-08,C012,Florianópolis,SC,P305,Casa e Decoração,89.90,4,27.90,Pix
1015,2025-02-10,C003,Belo Horizonte,MG,P205,Acessórios,49.90,3,28.90,Cartão de Crédito
1016,2025-02-12,C013,Vitória,ES,P102,Eletrônicos,899.90,1,30.50,Cartão de Crédito
1017,2025-02-15,C014,Natal,RN,P201,Acessórios,129.90,2,36.80,Boleto
1018,2025-02-18,C001,São Paulo,SP,P104,Eletrônicos,3299.99,1,25.50,Cartão de Crédito
1019,2025-02-20,C015,João Pessoa,PB,P302,Casa e Decoração,199.90,2,35.20,Pix
1020,2025-02-22,C016,Teresina,PI,P203,Acessórios,89.90,3,38.50,Cartão de Crédito
```

### Modelo de Solução
```python
# Solução do Exercício 2

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import matplotlib.dates as mdates

# Configurar visualização
plt.style.use('ggplot')
sns.set(style="whitegrid")
pd.set_option('display.max_columns', None)

# Importar dados
df = pd.read_csv('ecommerce_vendas.csv')

# Exibir primeiras linhas para verificar a importação
print("Primeiras linhas do DataFrame:")
print(df.head())

# Verificar informações do DataFrame
print("\nInformações do DataFrame:")
print(df.info())

# Verificar estatísticas básicas
print("\nEstatísticas descritivas:")
print(df.describe())

# Verificar valores nulos
print("\nValores nulos por coluna:")
print(df.isnull().sum())

# Preparação dos dados
# Converter a coluna de data para o tipo datetime
df['data_pedido'] = pd.to_datetime(df['data_pedido'])

# Criar colunas adicionais para análise
df['mes'] = df['data_pedido'].dt.month
df['mes_nome'] = df['data_pedido'].dt.strftime('%B')  # Nome do mês
df['dia_semana'] = df['data_pedido'].dt.day_name()  # Nome do dia da semana
df['valor_total'] = df['preco_unitario'] * df['quantidade']
df['valor_total_com_frete'] = df['valor_total'] + df['frete']

# 1. Análise de Vendas Gerais

# Total de vendas
total_vendas = df['valor_total'].sum()
total_pedidos = df['id_pedido'].nunique()
ticket_medio = total_vendas / total_pedidos
total_clientes = df['id_cliente'].nunique()
total_produtos_vendidos = df['quantidade'].sum()

print("\n=== ANÁLISE DE VENDAS GERAIS ===")
print(f"Total de vendas: R$ {total_vendas:.2f}")
print(f"Total de pedidos: {total_pedidos}")
print(f"Ticket médio: R$ {ticket_medio:.2f}")
print(f"Total de clientes: {total_clientes}")
print(f"Total de produtos vendidos: {total_produtos_vendidos}")

# 2. Análise por Categoria

# Vendas por categoria
vendas_por_categoria = df.groupby('categoria').agg({
    'valor_total': 'sum',
    'quantidade': 'sum',
    'id_pedido': pd.Series.nunique
}).rename(columns={'id_pedido': 'num_pedidos'}).reset_index()

vendas_por_categoria = vendas_por_categoria.sort_values('valor_total', ascending=False)

print("\n=== VENDAS POR CATEGORIA ===")
print(vendas_por_categoria)

# 3. Análise por Produto

# Produtos mais vendidos (por quantidade)
produtos_mais_vendidos = df.groupby('id_produto').agg({
    'quantidade': 'sum',
    'valor_total': 'sum'
}).sort_values('quantidade', ascending=False).reset_index()

print("\n=== PRODUTOS MAIS VENDIDOS (POR QUANTIDADE) ===")
print(produtos_mais_vendidos.head(5))

# Produtos mais lucrativos (por valor total)
produtos_mais_lucrativos = df.groupby('id_produto').agg({
    'valor_total': 'sum',
    'quantidade': 'sum'
}).sort_values('valor_total', ascending=False).reset_index()

print("\n=== PRODUTOS MAIS LUCRATIVOS (POR VALOR TOTAL) ===")
print(produtos_mais_lucrativos.head(5))

# 4. Análise por Cliente

# Clientes que mais compram (por valor)
clientes_mais_compram = df.groupby('id_cliente').agg({
    'valor_total': 'sum',
    'id_pedido': pd.Series.nunique
}).rename(columns={'id_pedido': 'num_pedidos'}).reset_index()

clientes_mais_compram['ticket_medio'] = clientes_mais_compram['valor_total'] / clientes_mais_compram['num_pedidos']
clientes_mais_compram = clientes_mais_compram.sort_values('valor_total', ascending=False)

print("\n=== CLIENTES QUE MAIS COMPRAM (POR VALOR) ===")
print(clientes_mais_compram.head(5))

# 5. Análise por Região

# Vendas por estado
vendas_por_estado = df.groupby('estado').agg({
    'valor_total': 'sum',
    'id_pedido': pd.Series.nunique,
    'id_cliente': pd.Series.nunique
}).rename(columns={
    'id_pedido': 'num_pedidos',
    'id_cliente': 'num_clientes'
}).reset_index()

vendas_por_estado = vendas_por_estado.sort_values('valor_total', ascending=False)

print("\n=== VENDAS POR ESTADO ===")
print(vendas_por_estado)

# 6. Análise por Método de Pagamento

# Vendas por método de pagamento
vendas_por_pagamento = df.groupby('pagamento').agg({
    'valor_total': 'sum',
    'id_pedido': pd.Series.nunique
}).rename(columns={'id_pedido': 'num_pedidos'}).reset_index()

vendas_por_pagamento['percentual'] = (vendas_por_pagamento['valor_total'] / total_vendas) * 100
vendas_por_pagamento = vendas_por_pagamento.sort_values('valor_total', ascending=False)

print("\n=== VENDAS POR MÉTODO DE PAGAMENTO ===")
print(vendas_por_pagamento)

# 7. Análise Temporal

# Vendas por mês
vendas_por_mes = df.groupby(['mes', 'mes_nome']).agg({
    'valor_total': 'sum',
    'id_pedido': pd.Series.nunique
}).rename(columns={'id_pedido': 'num_pedidos'}).reset_index()

vendas_por_mes = vendas_por_mes.sort_values('mes')

print("\n=== VENDAS POR MÊS ===")
print(vendas_por_mes)

# Vendas por dia da semana
vendas_por_dia_semana = df.groupby('dia_semana').agg({
    'valor_total': 'sum',
    'id_pedido': pd.Series.nunique
}).rename(columns={'id_pedido': 'num_pedidos'}).reset_index()

# Ordenar dias da semana
ordem_dias = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
vendas_por_dia_semana['dia_semana'] = pd.Categorical(vendas_por_dia_semana['dia_semana'], categories=ordem_dias, ordered=True)
vendas_por_dia_semana = vendas_por_dia_semana.sort_values('dia_semana')

print("\n=== VENDAS POR DIA DA SEMANA ===")
print(vendas_por_dia_semana)

# 8. Análise de Frete

# Frete médio por estado
frete_por_estado = df.groupby('estado')['frete'].mean().reset_index()
frete_por_estado = frete_por_estado.sort_values('frete', ascending=False)

print("\n=== FRETE MÉDIO POR ESTADO ===")
print(frete_por_estado)

# Relação entre frete e valor do pedido
df_pedidos = df.groupby('id_pedido').agg({
    'valor_total': 'sum',
    'frete': 'first'  # Assumindo que o frete é o mesmo para todos os itens do pedido
}).reset_index()

df_pedidos['percentual_frete'] = (df_pedidos['frete'] / df_pedidos['valor_total']) * 100

print("\n=== RELAÇÃO FRETE/VALOR DO PEDIDO ===")
print(f"Percentual médio do frete sobre o valor do pedido: {df_pedidos['percentual_frete'].mean():.2f}%")
print(f"Percentual mínimo: {df_pedidos['percentual_frete'].min():.2f}%")
print(f"Percentual máximo: {df_pedidos['percentual_frete'].max():.2f}%")

# Visualizações

# 1. Gráfico de barras - Vendas por Categoria
plt.figure(figsize=(10, 6))
sns.barplot(x='categoria', y='valor_total', data=vendas_por_categoria)
plt.title('Vendas por Categoria')
plt.xlabel('Categoria')
plt.ylabel('Valor Total (R$)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('ecommerce_vendas_por_categoria.png')
plt.close()

# 2. Gráfico de pizza - Distribuição de Vendas por Método de Pagamento
plt.figure(figsize=(8, 8))
plt.pie(vendas_por_pagamento['valor_total'], labels=vendas_por_pagamento['pagamento'], 
        autopct='%1.1f%%', startangle=90, shadow=True)
plt.title('Distribuição de Vendas por Método de Pagamento')
plt.axis('equal')
plt.tight_layout()
plt.savefig('ecommerce_vendas_por_pagamento.png')
plt.close()

# 3. Gráfico de linha - Vendas por Mês
plt.figure(figsize=(10, 6))
sns.lineplot(x='mes_nome', y='valor_total', data=vendas_por_mes, marker='o')
plt.title('Vendas por Mê
(Content truncated due to size limit. Use line ranges to read in chunks)