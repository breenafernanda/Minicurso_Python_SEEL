# Exercícios Práticos: Python para Automação

## Exercício 1: Manipulação de Strings e Listas

### Objetivo
Praticar manipulação básica de strings e listas em Python, habilidades fundamentais para automação.

### Enunciado
Você recebeu uma lista de produtos com seus preços em formato de texto. Sua tarefa é:
1. Extrair o nome e o preço de cada produto
2. Converter os preços para valores numéricos
3. Calcular o preço total e o preço médio
4. Identificar o produto mais caro e o mais barato

### Dados de Entrada
```python
produtos = [
    "Notebook Dell - R$ 3.599,99",
    "Mouse sem fio - R$ 89,90",
    "Teclado mecânico - R$ 259,50",
    "Monitor 24 polegadas - R$ 799,00",
    "Headset gamer - R$ 199,90"
]
```

### Modelo de Solução
```python
# Solução do Exercício 1

# Lista de produtos
produtos = [
    "Notebook Dell - R$ 3.599,99",
    "Mouse sem fio - R$ 89,90",
    "Teclado mecânico - R$ 259,50",
    "Monitor 24 polegadas - R$ 799,00",
    "Headset gamer - R$ 199,90"
]

# Listas para armazenar dados extraídos
nomes = []
precos = []

# Extrair nomes e preços
for produto in produtos:
    # Dividir a string pelo separador " - R$ "
    partes = produto.split(" - R$ ")
    nome = partes[0]
    preco_texto = partes[1]
    
    # Converter preço para float (substituindo vírgula por ponto)
    preco = float(preco_texto.replace(".", "").replace(",", "."))
    
    # Adicionar às listas
    nomes.append(nome)
    precos.append(preco)

# Calcular preço total e médio
preco_total = sum(precos)
preco_medio = preco_total / len(precos)

# Encontrar produto mais caro e mais barato
indice_mais_caro = precos.index(max(precos))
indice_mais_barato = precos.index(min(precos))

# Exibir resultados
print(f"Produtos processados: {len(produtos)}")
print(f"Preço total: R$ {preco_total:.2f}")
print(f"Preço médio: R$ {preco_medio:.2f}")
print(f"Produto mais caro: {nomes[indice_mais_caro]} (R$ {precos[indice_mais_caro]:.2f})")
print(f"Produto mais barato: {nomes[indice_mais_barato]} (R$ {precos[indice_mais_barato]:.2f})")

# Exibir lista formatada
print("\nLista de produtos:")
for i in range(len(nomes)):
    print(f"- {nomes[i]}: R$ {precos[i]:.2f}")
```

## Exercício 2: Manipulação de Arquivos

### Objetivo
Praticar leitura e escrita de arquivos, processamento de dados e geração de relatórios.

### Enunciado
Você recebeu um arquivo CSV com dados de vendas de uma loja. Sua tarefa é:
1. Ler o arquivo CSV e processar os dados
2. Calcular o total de vendas por categoria
3. Identificar o produto mais vendido
4. Gerar um relatório em formato de texto

### Dados de Entrada
Crie um arquivo `vendas.csv` com o seguinte conteúdo:
```
produto,categoria,preco,quantidade
Notebook Dell,Informática,3599.99,5
Mouse sem fio,Informática,89.90,15
Teclado mecânico,Informática,259.50,8
Monitor 24 polegadas,Informática,799.00,10
Headset gamer,Informática,199.90,12
Smartphone Samsung,Celulares,1899.00,7
iPhone 13,Celulares,5999.00,3
Carregador wireless,Acessórios,99.90,20
Capa para celular,Acessórios,49.90,25
Película de vidro,Acessórios,29.90,30
```

### Modelo de Solução
```python
# Solução do Exercício 2

import csv
from collections import defaultdict

# Função para ler o arquivo CSV
def ler_vendas(arquivo):
    vendas = []
    with open(arquivo, 'r', encoding='utf-8') as f:
        leitor = csv.DictReader(f)
        for linha in leitor:
            # Converter tipos de dados
            linha['preco'] = float(linha['preco'])
            linha['quantidade'] = int(linha['quantidade'])
            vendas.append(linha)
    return vendas

# Função para calcular total de vendas por categoria
def calcular_vendas_por_categoria(vendas):
    vendas_por_categoria = defaultdict(float)
    for venda in vendas:
        categoria = venda['categoria']
        valor_total = venda['preco'] * venda['quantidade']
        vendas_por_categoria[categoria] += valor_total
    return vendas_por_categoria

# Função para encontrar produto mais vendido
def encontrar_produto_mais_vendido(vendas):
    mais_vendido = None
    maior_quantidade = 0
    
    for venda in vendas:
        if venda['quantidade'] > maior_quantidade:
            maior_quantidade = venda['quantidade']
            mais_vendido = venda
    
    return mais_vendido

# Função para gerar relatório
def gerar_relatorio(vendas, vendas_por_categoria, mais_vendido):
    total_geral = sum(venda['preco'] * venda['quantidade'] for venda in vendas)
    
    relatorio = []
    relatorio.append("RELATÓRIO DE VENDAS")
    relatorio.append("=" * 30)
    relatorio.append(f"Total de produtos: {len(vendas)}")
    relatorio.append(f"Total geral de vendas: R$ {total_geral:.2f}")
    relatorio.append("\nVendas por categoria:")
    
    for categoria, total in vendas_por_categoria.items():
        relatorio.append(f"- {categoria}: R$ {total:.2f}")
    
    relatorio.append(f"\nProduto mais vendido: {mais_vendido['produto']}")
    relatorio.append(f"Categoria: {mais_vendido['categoria']}")
    relatorio.append(f"Preço unitário: R$ {mais_vendido['preco']:.2f}")
    relatorio.append(f"Quantidade vendida: {mais_vendido['quantidade']}")
    relatorio.append(f"Valor total: R$ {mais_vendido['preco'] * mais_vendido['quantidade']:.2f}")
    
    relatorio.append("\nDetalhamento de vendas:")
    for venda in vendas:
        valor_total = venda['preco'] * venda['quantidade']
        relatorio.append(f"- {venda['produto']}: {venda['quantidade']} unidades, R$ {valor_total:.2f}")
    
    return "\n".join(relatorio)

# Programa principal
arquivo_vendas = 'vendas.csv'

try:
    # Ler dados
    vendas = ler_vendas(arquivo_vendas)
    
    # Processar dados
    vendas_por_categoria = calcular_vendas_por_categoria(vendas)
    mais_vendido = encontrar_produto_mais_vendido(vendas)
    
    # Gerar relatório
    relatorio = gerar_relatorio(vendas, vendas_por_categoria, mais_vendido)
    
    # Salvar relatório
    with open('relatorio_vendas.txt', 'w', encoding='utf-8') as f:
        f.write(relatorio)
    
    print("Relatório gerado com sucesso!")
    print(relatorio)
    
except FileNotFoundError:
    print(f"Erro: O arquivo {arquivo_vendas} não foi encontrado.")
except Exception as e:
    print(f"Erro ao processar o arquivo: {str(e)}")
```

## Exercício 3: Automação de Tarefas com Funções

### Objetivo
Praticar a criação de funções para automatizar tarefas repetitivas e processar dados de forma estruturada.

### Enunciado
Você precisa automatizar o processamento de notas fiscais. Sua tarefa é:
1. Criar funções para extrair informações de notas fiscais
2. Calcular impostos e totais
3. Gerar um resumo das notas processadas
4. Identificar possíveis inconsistências nos dados

### Dados de Entrada
```python
notas_fiscais = [
    {
        "numero": "NF-001",
        "data": "2025-01-15",
        "cliente": "Empresa A",
        "itens": [
            {"produto": "Serviço de Consultoria", "valor": 1500.00, "quantidade": 10},
            {"produto": "Licença de Software", "valor": 800.00, "quantidade": 5}
        ],
        "imposto": 0.15  # 15% de imposto
    },
    {
        "numero": "NF-002",
        "data": "2025-01-20",
        "cliente": "Empresa B",
        "itens": [
            {"produto": "Manutenção de Equipamentos", "valor": 350.00, "quantidade": 3},
            {"produto": "Peças de Reposição", "valor": 120.00, "quantidade": 12}
        ],
        "imposto": 0.12  # 12% de imposto
    },
    {
        "numero": "NF-003",
        "data": "2025-01-25",
        "cliente": "Empresa C",
        "itens": [
            {"produto": "Desenvolvimento de Website", "valor": 3000.00, "quantidade": 1},
            {"produto": "Hospedagem Anual", "valor": 600.00, "quantidade": 1}
        ],
        "imposto": 0.18  # 18% de imposto
    }
]
```

### Modelo de Solução
```python
# Solução do Exercício 3

# Dados de entrada
notas_fiscais = [
    {
        "numero": "NF-001",
        "data": "2025-01-15",
        "cliente": "Empresa A",
        "itens": [
            {"produto": "Serviço de Consultoria", "valor": 1500.00, "quantidade": 10},
            {"produto": "Licença de Software", "valor": 800.00, "quantidade": 5}
        ],
        "imposto": 0.15  # 15% de imposto
    },
    {
        "numero": "NF-002",
        "data": "2025-01-20",
        "cliente": "Empresa B",
        "itens": [
            {"produto": "Manutenção de Equipamentos", "valor": 350.00, "quantidade": 3},
            {"produto": "Peças de Reposição", "valor": 120.00, "quantidade": 12}
        ],
        "imposto": 0.12  # 12% de imposto
    },
    {
        "numero": "NF-003",
        "data": "2025-01-25",
        "cliente": "Empresa C",
        "itens": [
            {"produto": "Desenvolvimento de Website", "valor": 3000.00, "quantidade": 1},
            {"produto": "Hospedagem Anual", "valor": 600.00, "quantidade": 1}
        ],
        "imposto": 0.18  # 18% de imposto
    }
]

# Função para calcular o subtotal de uma nota fiscal
def calcular_subtotal(nota):
    subtotal = 0
    for item in nota["itens"]:
        subtotal += item["valor"] * item["quantidade"]
    return subtotal

# Função para calcular o valor do imposto
def calcular_imposto(nota):
    subtotal = calcular_subtotal(nota)
    return subtotal * nota["imposto"]

# Função para calcular o total da nota
def calcular_total(nota):
    subtotal = calcular_subtotal(nota)
    imposto = calcular_imposto(nota)
    return subtotal + imposto

# Função para verificar inconsistências
def verificar_inconsistencias(nota):
    inconsistencias = []
    
    # Verificar se há itens na nota
    if not nota["itens"]:
        inconsistencias.append(f"Nota {nota['numero']}: Não possui itens")
    
    # Verificar se há valores negativos
    for item in nota["itens"]:
        if item["valor"] < 0:
            inconsistencias.append(f"Nota {nota['numero']}: Item '{item['produto']}' com valor negativo")
        if item["quantidade"] <= 0:
            inconsistencias.append(f"Nota {nota['numero']}: Item '{item['produto']}' com quantidade inválida")
    
    # Verificar taxa de imposto
    if nota["imposto"] < 0 or nota["imposto"] > 0.5:  # Imposto entre 0% e 50%
        inconsistencias.append(f"Nota {nota['numero']}: Taxa de imposto suspeita ({nota['imposto']*100}%)")
    
    return inconsistencias

# Função para gerar resumo da nota
def gerar_resumo_nota(nota):
    subtotal = calcular_subtotal(nota)
    imposto = calcular_imposto(nota)
    total = calcular_total(nota)
    
    resumo = {
        "numero": nota["numero"],
        "data": nota["data"],
        "cliente": nota["cliente"],
        "qtd_itens": len(nota["itens"]),
        "subtotal": subtotal,
        "imposto": imposto,
        "total": total
    }
    
    return resumo

# Função para processar todas as notas
def processar_notas(notas):
    resumos = []
    todas_inconsistencias = []
    
    for nota in notas:
        # Verificar inconsistências
        inconsistencias = verificar_inconsistencias(nota)
        if inconsistencias:
            todas_inconsistencias.extend(inconsistencias)
        
        # Gerar resumo
        resumo = gerar_resumo_nota(nota)
        resumos.append(resumo)
    
    return resumos, todas_inconsistencias

# Função para exibir relatório
def exibir_relatorio(resumos, inconsistencias):
    print("RELATÓRIO DE PROCESSAMENTO DE NOTAS FISCAIS")
    print("=" * 50)
    
    # Exibir resumos
    print("\nResumo das Notas Processadas:")
    total_geral = 0
    
    for resumo in resumos:
        print(f"\nNota: {resumo['numero']} - Data: {resumo['data']}")
        print(f"Cliente: {resumo['cliente']}")
        print(f"Itens: {resumo['qtd_itens']}")
        print(f"Subtotal: R$ {resumo['subtotal']:.2f}")
        print(f"Imposto: R$ {resumo['imposto']:.2f} ({resumo['imposto']/resumo['subtotal']*100:.1f}%)")
        print(f"Total: R$ {resumo['total']:.2f}")
        
        total_geral += resumo['total']
    
    print("\n" + "-" * 50)
    print(f"Total Geral: R$ {total_geral:.2f}")
    
    # Exibir inconsistências
    if inconsistencias:
        print("\nInconsistências Encontradas:")
        for inconsistencia in inconsistencias:
            print(f"- {inconsistencia}")
    else:
        print("\nNenhuma inconsistência encontrada.")

# Executar o processamento
resumos, inconsistencias = processar_notas(notas_fiscais)
exibir_relatorio(resumos, inconsistencias)

# Adicionar uma nota com inconsistências para teste
nota_inconsistente = {
    "numero": "NF-004",
    "data": "2025-01-30",
    "cliente": "Empresa D",
    "itens": [
        {"produto": "Produto com valor negativo", "valor": -100.00, "quantidade": 1},
        {"produto": "Produto com quantidade zero", "valor": 200.00, "quantidade": 0}
    ],
    "imposto": 0.75  # 75% de imposto (suspeito)
}

print("\n\nTestando com nota inconsistente:")
notas_teste = [nota_inconsistente]
resumos_teste, inconsistencias_teste = processar_notas(notas_teste)
exibir_relatorio(resumos_teste, inconsistencias_teste)
```

## Exercício 4: Trabalhando com APIs e JSON

### Objetivo
Praticar a interação com APIs web, processamento de dados JSON e manipulação de estruturas de dados complexas.

### Enunciado
Você precisa criar um sistema que consulta uma API de previsão do tempo e gera relatórios personalizados. Sua tarefa é:
1. Fazer requisições para uma API de previsão do tempo
2. Processar os dados JSON retornados
3. Extrair informações relevantes e organizá-las
4. Gerar um relatório de previsão do tempo para os próximos dias

### Dados de Entrada
Para este exercício, usaremos uma simulação de API em vez de uma API real:

```python
# Simulação de resposta de API de previsão do tempo
def simular_api_previsao(cidade):
    import random
    from datetime import datetime, timedelta
    
    # Dados simulados
    previsoes = []
    data_atual = datetime.now()
    
    # Condições possíveis
    condicoes = ["Ensolarado", "Parcialmente nublado", "Nublado", "Chuvoso", "Tempestade"]
    
    # Gerar previsões para 5 dias
    for i in range(5):
        data = data_atual + timedelta(days=i)
        data_str = data.strftime("%Y-%m-%d")
        
        # Gerar dados aleatórios
        temp_min = random.randint(15, 25)
        temp_max = temp_min + random.randint(3, 10)
        condicao = random.choice(condicoes)
        probabilidade_chuva = random.randint(0, 100) if condicao in ["Nublado", "Chuvoso", "Tempestade"] else 0
        velocidade_vento = random.randint(5, 30)
        
        # Criar previsão para o dia
        previsao = {
            "data": data_str,
            "temperatura": {
                "minima": temp_min,
                "maxima": temp_max
            },
            "condicao": condicao,
            "probabilidade_chuva": probabilidade_chuva,
            "vento": {
                "velocidade": velocidade_vento,
                "direcao": random.choice(["Norte", "Sul", "Leste", "Oeste"])
            },
            "umidade": random.randint(30, 90)
        }
        
        previsoes.append(previsao)
    
    # Criar resposta completa
    resposta = {
        "cidade": cidade,
        "pais": "Brasil",
        "latitude": -23.5505,
        "longitude": -46.6333,
        "previsoes": previsoes
    }
    
    return resposta
```

### Modelo de Solução
```python
# Solução do Exercício 4

import json
from datetime import datetime

# Simulação de resposta de API de previsão do tempo
def simular_api_previsao(cidade):
    import random
    from datetime import datetime, timedelta
    
    # Dados simulados
    previsoes = []
    data_atual = datetime.now()
    
    # Condições possíveis
    condicoes = ["Ensolarado", "Parcialmente nublado", "Nublado", "Chuvoso", "Tempestade"]
    
    # Gerar previsões para 5 dias
    for i in range(5):
        data = data_atual + timedelta(days=i)
        data_str = data.strftime("%Y-%m-%d")
        
        # Gerar dados aleatórios
        temp_min = random.randint(15, 25)
        temp_max = temp_min + random.randint(3, 10)
        condicao = random.choice(condicoes)
        
(Content truncated due to size limit. Use line ranges to read in chunks)