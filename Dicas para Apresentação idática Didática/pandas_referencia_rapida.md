# Referência Rápida: Pandas para Análise de Dados

## Configuração Inicial

### Instalação
```python
# Instalar Pandas
pip install pandas

# Instalar dependências comuns
pip install numpy matplotlib seaborn openpyxl
```

### Importação
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

## Criação de DataFrames

### A partir de Dicionários
```python
# Criar DataFrame a partir de dicionário
dados = {
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Daniela'],
    'Idade': [25, 30, 22, 28],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba']
}
df = pd.DataFrame(dados)
```

### A partir de Listas
```python
# Criar DataFrame a partir de listas
nomes = ['Ana', 'Bruno', 'Carlos', 'Daniela']
idades = [25, 30, 22, 28]
cidades = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba']

df = pd.DataFrame(list(zip(nomes, idades, cidades)), 
                  columns=['Nome', 'Idade', 'Cidade'])
```

### A partir de Arquivos
```python
# CSV
df = pd.read_csv('dados.csv', encoding='utf-8')

# Excel
df = pd.read_excel('dados.xlsx', sheet_name='Planilha1')

# JSON
df = pd.read_json('dados.json')

# HTML (tabelas de páginas web)
dfs = pd.read_html('https://www.exemplo.com.br/tabela')
df = dfs[0]  # Primeira tabela encontrada
```

## Visualização e Exploração

### Visualização Básica
```python
# Exibir primeiras linhas
df.head()  # Padrão: 5 linhas
df.head(10)  # 10 linhas

# Exibir últimas linhas
df.tail()  # Padrão: 5 linhas

# Informações sobre o DataFrame
df.info()

# Estatísticas descritivas
df.describe()

# Dimensões (linhas, colunas)
df.shape

# Nomes das colunas
df.columns

# Tipos de dados
df.dtypes
```

### Exploração
```python
# Valores únicos em uma coluna
df['Cidade'].unique()

# Contagem de valores únicos
df['Cidade'].value_counts()

# Verificar valores nulos
df.isnull().sum()

# Correlação entre colunas numéricas
df.corr()

# Amostragem aleatória
df.sample(5)  # 5 linhas aleatórias
```

## Seleção de Dados

### Seleção de Colunas
```python
# Selecionar uma coluna (retorna Series)
idades = df['Idade']

# Selecionar múltiplas colunas (retorna DataFrame)
df_selecionado = df[['Nome', 'Idade']]
```

### Seleção de Linhas
```python
# Selecionar por índice (iloc)
primeira_linha = df.iloc[0]  # Primeira linha
tres_primeiras = df.iloc[0:3]  # Três primeiras linhas
ultima_linha = df.iloc[-1]  # Última linha

# Selecionar por rótulo (loc)
linha = df.loc[5]  # Linha com índice 5
intervalo = df.loc[2:5]  # Linhas com índices de 2 a 5
```

### Seleção Condicional
```python
# Filtrar por condição
maiores_25 = df[df['Idade'] > 25]

# Múltiplas condições (AND)
filtro = df[(df['Idade'] > 25) & (df['Cidade'] == 'São Paulo')]

# Múltiplas condições (OR)
filtro = df[(df['Idade'] > 30) | (df['Cidade'] == 'Rio de Janeiro')]

# Verificar se valor está em uma lista
cidades_interesse = ['São Paulo', 'Rio de Janeiro']
filtro = df[df['Cidade'].isin(cidades_interesse)]

# Filtrar por texto
filtro = df[df['Nome'].str.contains('Ana')]
```

## Manipulação de Dados

### Adicionar e Remover Colunas
```python
# Adicionar coluna
df['Salário'] = [3000, 4500, 2800, 5200]

# Adicionar coluna calculada
df['Faixa Etária'] = ['Jovem' if idade < 25 else 'Adulto' for idade in df['Idade']]

# Remover coluna
df = df.drop('Salário', axis=1)

# Remover múltiplas colunas
df = df.drop(['Salário', 'Faixa Etária'], axis=1)
```

### Renomear Colunas
```python
# Renomear uma coluna
df = df.rename(columns={'Nome': 'Nome Completo'})

# Renomear múltiplas colunas
df = df.rename(columns={
    'Nome': 'Nome Completo',
    'Idade': 'Anos'
})

# Renomear todas as colunas
df.columns = ['nome', 'idade', 'cidade']
```

### Ordenação
```python
# Ordenar por uma coluna (crescente)
df = df.sort_values('Idade')

# Ordenar por uma coluna (decrescente)
df = df.sort_values('Idade', ascending=False)

# Ordenar por múltiplas colunas
df = df.sort_values(['Cidade', 'Idade'], ascending=[True, False])
```

### Tratamento de Valores Nulos
```python
# Remover linhas com valores nulos
df = df.dropna()

# Remover linhas com valores nulos em colunas específicas
df = df.dropna(subset=['Nome', 'Idade'])

# Preencher valores nulos
df['Idade'] = df['Idade'].fillna(0)  # Com zero
df['Cidade'] = df['Cidade'].fillna('Desconhecida')  # Com texto
df['Salário'] = df['Salário'].fillna(df['Salário'].mean())  # Com média
```

## Transformação de Dados

### Aplicar Funções
```python
# Aplicar função a uma coluna
df['Nome'] = df['Nome'].apply(lambda x: x.upper())

# Aplicar função a múltiplas colunas
df[['Nome', 'Cidade']] = df[['Nome', 'Cidade']].apply(lambda x: x.str.upper())

# Aplicar função a cada elemento do DataFrame
df = df.applymap(lambda x: str(x).strip() if isinstance(x, str) else x)
```

### Conversão de Tipos
```python
# Converter tipo de coluna
df['Idade'] = df['Idade'].astype(int)
df['Salário'] = df['Salário'].astype(float)
df['Data'] = pd.to_datetime(df['Data'])

# Converter múltiplas colunas
df = df.astype({'Idade': int, 'Salário': float})
```

### Manipulação de Texto
```python
# Converter para maiúsculas/minúsculas
df['Nome'] = df['Nome'].str.upper()
df['Nome'] = df['Nome'].str.lower()

# Extrair parte do texto
df['Primeiro Nome'] = df['Nome'].str.split(' ').str[0]

# Substituir texto
df['Cidade'] = df['Cidade'].str.replace('São Paulo', 'SP')

# Verificar se contém texto
df['Tem Rio'] = df['Cidade'].str.contains('Rio')
```

### Manipulação de Datas
```python
# Converter para datetime
df['Data'] = pd.to_datetime(df['Data'])

# Extrair componentes de data
df['Ano'] = df['Data'].dt.year
df['Mês'] = df['Data'].dt.month
df['Dia'] = df['Data'].dt.day
df['Dia da Semana'] = df['Data'].dt.day_name()

# Calcular diferença entre datas
df['Dias Passados'] = (pd.Timestamp.now() - df['Data']).dt.days
```

## Agregação e Agrupamento

### Funções de Agregação
```python
# Estatísticas básicas
media_idade = df['Idade'].mean()
soma_salarios = df['Salário'].sum()
contagem = df['Nome'].count()
valor_maximo = df['Idade'].max()
valor_minimo = df['Idade'].min()

# Múltiplas estatísticas
resumo = df['Idade'].agg(['min', 'max', 'mean', 'median', 'std'])
```

### Agrupamento
```python
# Agrupar por uma coluna
grupo = df.groupby('Cidade')

# Estatísticas por grupo
media_por_cidade = df.groupby('Cidade')['Idade'].mean()
contagem_por_cidade = df.groupby('Cidade').size()

# Múltiplas estatísticas por grupo
resumo_por_cidade = df.groupby('Cidade').agg({
    'Idade': ['mean', 'min', 'max', 'count'],
    'Salário': ['mean', 'sum']
})

# Agrupar por múltiplas colunas
grupo_multiplo = df.groupby(['Cidade', 'Faixa Etária'])
```

### Tabelas Dinâmicas
```python
# Criar tabela dinâmica
tabela_dinamica = pd.pivot_table(
    df,
    values='Salário',
    index='Cidade',
    columns='Faixa Etária',
    aggfunc='mean'
)

# Tabela dinâmica com múltiplas métricas
tabela_dinamica = pd.pivot_table(
    df,
    values=['Salário', 'Idade'],
    index=['Cidade'],
    columns=['Faixa Etária'],
    aggfunc={'Salário': 'mean', 'Idade': 'max'},
    fill_value=0
)
```

## Combinação de DataFrames

### Concatenação
```python
# Concatenar verticalmente (empilhar)
df_combinado = pd.concat([df1, df2])

# Concatenar horizontalmente (lado a lado)
df_combinado = pd.concat([df1, df2], axis=1)
```

### Merge (Join)
```python
# Inner join (apenas registros correspondentes)
df_merged = pd.merge(df_clientes, df_pedidos, on='ID_Cliente')

# Left join (todos de df_clientes + correspondentes de df_pedidos)
df_merged = pd.merge(df_clientes, df_pedidos, on='ID_Cliente', how='left')

# Right join (todos de df_pedidos + correspondentes de df_clientes)
df_merged = pd.merge(df_clientes, df_pedidos, on='ID_Cliente', how='right')

# Outer join (todos os registros de ambos os DataFrames)
df_merged = pd.merge(df_clientes, df_pedidos, on='ID_Cliente', how='outer')

# Merge com colunas de nomes diferentes
df_merged = pd.merge(
    df_clientes, 
    df_pedidos, 
    left_on='ID_Cliente', 
    right_on='Cliente_ID'
)
```

## Exportação de Dados

### Salvar em Arquivos
```python
# CSV
df.to_csv('dados_exportados.csv', index=False, encoding='utf-8')

# Excel
df.to_excel('dados_exportados.xlsx', sheet_name='Dados', index=False)

# JSON
df.to_json('dados_exportados.json', orient='records')

# HTML
df.to_html('dados_exportados.html')
```

## Visualização com Pandas

### Gráficos Básicos
```python
# Gráfico de linha
df.plot(x='Data', y='Valor')

# Gráfico de barras
df['Cidade'].value_counts().plot(kind='bar')

# Gráfico de dispersão
df.plot.scatter(x='Idade', y='Salário')

# Histograma
df['Idade'].plot.hist(bins=10)

# Gráfico de pizza
df['Cidade'].value_counts().plot.pie(autopct='%1.1f%%')
```

### Personalização de Gráficos
```python
# Tamanho da figura
plt.figure(figsize=(10, 6))

# Título e rótulos
df.plot(x='Data', y='Valor')
plt.title('Evolução do Valor ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Valor (R$)')

# Salvar gráfico
plt.savefig('grafico.png', dpi=300, bbox_inches='tight')
```

## Dicas para Análise de Dados

### Boas Práticas
1. **Faça cópias** antes de modificar DataFrames originais: `df_novo = df.copy()`
2. **Use métodos encadeados** para operações sequenciais
3. **Verifique tipos de dados** antes de operações matemáticas
4. **Trate valores nulos** adequadamente
5. **Use `.loc` e `.iloc`** em vez de indexação simples para evitar warnings
6. **Documente seu código** com comentários explicativos
7. **Crie funções auxiliares** para operações repetitivas

### Otimização de Desempenho
```python
# Usar tipos de dados otimizados
df['ID'] = pd.to_numeric(df['ID'], downcast='integer')
df['Valor'] = pd.to_numeric(df['Valor'], downcast='float')

# Processar em chunks para arquivos grandes
chunks = pd.read_csv('arquivo_grande.csv', chunksize=10000)
for chunk in chunks:
    # Processar cada chunk
    resultado = processar_dados(chunk)
    
# Usar query para filtros complexos (mais eficiente)
df_filtrado = df.query('Idade > 25 and Cidade == "São Paulo"')
```
