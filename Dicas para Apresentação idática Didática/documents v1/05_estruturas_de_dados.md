# Estruturas de Dados em Python

As estruturas de dados são formas de organizar e armazenar dados para que possam ser acessados e modificados de maneira eficiente. Python oferece várias estruturas de dados embutidas que são fundamentais para resolver problemas de programação. Neste capítulo, vamos explorar as principais estruturas de dados em Python: listas, tuplas, dicionários e conjuntos.

## Listas

As listas são uma das estruturas de dados mais versáteis e frequentemente utilizadas em Python. Elas permitem armazenar coleções ordenadas de itens, que podem ser de diferentes tipos.

### Criando Listas

```python
# Lista vazia
lista_vazia = []

# Lista com elementos
numeros = [1, 2, 3, 4, 5]
frutas = ["maçã", "banana", "laranja"]

# Lista com diferentes tipos de dados
misturada = [1, "Python", True, 3.14]

# Lista de listas (matriz)
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

### Acessando Elementos

Os elementos de uma lista são acessados por seus índices, que começam em 0:

```python
frutas = ["maçã", "banana", "laranja", "uva", "pera"]

# Acessando pelo índice
primeira_fruta = frutas[0]  # "maçã"
segunda_fruta = frutas[1]   # "banana"

# Índices negativos (contam a partir do final)
ultima_fruta = frutas[-1]   # "pera"
penultima_fruta = frutas[-2]  # "uva"

# Fatiamento (slicing)
duas_primeiras = frutas[0:2]  # ["maçã", "banana"]
do_meio_ao_fim = frutas[2:]   # ["laranja", "uva", "pera"]
do_inicio_ao_meio = frutas[:3]  # ["maçã", "banana", "laranja"]

# Saltando elementos
de_dois_em_dois = frutas[::2]  # ["maçã", "laranja", "pera"]

# Invertendo a lista
invertida = frutas[::-1]  # ["pera", "uva", "laranja", "banana", "maçã"]
```

### Modificando Listas

As listas são mutáveis, o que significa que podem ser modificadas após a criação:

```python
numeros = [1, 2, 3, 4, 5]

# Alterando um elemento
numeros[0] = 10  # numeros agora é [10, 2, 3, 4, 5]

# Adicionando elementos
numeros.append(6)  # Adiciona ao final: [10, 2, 3, 4, 5, 6]
numeros.insert(1, 15)  # Insere na posição 1: [10, 15, 2, 3, 4, 5, 6]

# Estendendo a lista
mais_numeros = [7, 8, 9]
numeros.extend(mais_numeros)  # [10, 15, 2, 3, 4, 5, 6, 7, 8, 9]

# Removendo elementos
numeros.remove(15)  # Remove o valor 15: [10, 2, 3, 4, 5, 6, 7, 8, 9]
ultimo = numeros.pop()  # Remove e retorna o último elemento (9)
elemento_indice_2 = numeros.pop(2)  # Remove e retorna o elemento no índice 2 (3)

# Limpando a lista
numeros.clear()  # numeros agora é []
```

### Operações com Listas

```python
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

# Concatenação
lista_combinada = lista1 + lista2  # [1, 2, 3, 4, 5, 6]

# Repetição
lista_repetida = lista1 * 3  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Verificando se um elemento está na lista
esta_na_lista = 2 in lista1  # True
nao_esta_na_lista = 7 in lista1  # False

# Comprimento da lista
tamanho = len(lista1)  # 3

# Mínimo e máximo
minimo = min(lista1)  # 1
maximo = max(lista1)  # 3

# Soma dos elementos
soma = sum(lista1)  # 6
```

### Métodos Úteis para Listas

```python
numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# Ordenação
numeros.sort()  # Ordena a lista original: [1, 1, 2, 3, 4, 5, 5, 6, 9]
numeros.sort(reverse=True)  # Ordena em ordem decrescente: [9, 6, 5, 5, 4, 3, 2, 1, 1]

# Criando uma nova lista ordenada (sem modificar a original)
numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5]
ordenada = sorted(numeros)  # [1, 1, 2, 3, 4, 5, 5, 6, 9]
ordenada_decrescente = sorted(numeros, reverse=True)  # [9, 6, 5, 5, 4, 3, 2, 1, 1]

# Invertendo a ordem
numeros.reverse()  # Inverte a lista original

# Contando ocorrências
contagem_de_5 = numeros.count(5)  # Conta quantas vezes o número 5 aparece

# Encontrando o índice
indice_do_4 = numeros.index(4)  # Retorna o índice da primeira ocorrência do 4
```

### Compreensão de Listas

A compreensão de listas é uma forma concisa e elegante de criar novas listas a partir de sequências existentes:

```python
# Criando uma lista com os quadrados dos números de 1 a 10
quadrados = [x**2 for x in range(1, 11)]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Compreensão de lista com condição
pares = [x for x in range(1, 11) if x % 2 == 0]
# [2, 4, 6, 8, 10]

# Compreensão de lista com transformação e condição
nomes = ["Ana", "Pedro", "Maria", "João", "Beatriz"]
nomes_com_a = [nome.upper() for nome in nomes if 'a' in nome.lower()]
# ["ANA", "MARIA", "JOÃO", "BEATRIZ"]
```

## Tuplas

As tuplas são semelhantes às listas, mas são imutáveis, ou seja, não podem ser modificadas após a criação. Elas são usadas para armazenar coleções de itens que não devem ser alterados.

### Criando Tuplas

```python
# Tupla vazia
tupla_vazia = ()

# Tupla com elementos
coordenadas = (10, 20)
cores = ("vermelho", "verde", "azul")

# Tupla com um único elemento (precisa da vírgula)
singleton = (42,)  # Sem a vírgula seria interpretado como um número entre parênteses

# Tupla sem parênteses (empacotamento de tupla)
pessoa = "João", 25, "Engenheiro"  # Equivalente a ("João", 25, "Engenheiro")

# Convertendo uma lista em tupla
lista = [1, 2, 3]
tupla = tuple(lista)  # (1, 2, 3)
```

### Acessando Elementos

O acesso aos elementos de uma tupla é semelhante ao das listas:

```python
coordenadas = (10, 20, 30, 40, 50)

# Acessando pelo índice
x = coordenadas[0]  # 10
y = coordenadas[1]  # 20

# Índices negativos
ultimo = coordenadas[-1]  # 50

# Fatiamento
tres_primeiros = coordenadas[:3]  # (10, 20, 30)
```

### Desempacotamento de Tuplas

Uma característica útil das tuplas é a possibilidade de desempacotar seus valores em variáveis separadas:

```python
# Desempacotamento básico
coordenadas = (10, 20, 30)
x, y, z = coordenadas  # x=10, y=20, z=30

# Desempacotamento com *
primeiro, *meio, ultimo = (1, 2, 3, 4, 5)
# primeiro=1, meio=[2, 3, 4], ultimo=5

# Troca de valores usando tuplas
a, b = 5, 10
a, b = b, a  # Agora a=10 e b=5
```

### Operações com Tuplas

```python
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

# Concatenação
tupla_combinada = tupla1 + tupla2  # (1, 2, 3, 4, 5, 6)

# Repetição
tupla_repetida = tupla1 * 3  # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Verificando se um elemento está na tupla
esta_na_tupla = 2 in tupla1  # True

# Comprimento da tupla
tamanho = len(tupla1)  # 3

# Mínimo e máximo
minimo = min(tupla1)  # 1
maximo = max(tupla1)  # 3

# Contando ocorrências
numeros = (1, 2, 2, 3, 4, 2)
contagem_de_2 = numeros.count(2)  # 3

# Encontrando o índice
indice_do_3 = numeros.index(3)  # 3
```

### Quando Usar Tuplas em Vez de Listas

- Use tuplas para coleções de itens que não devem mudar (como dias da semana, coordenadas geográficas)
- Tuplas podem ser usadas como chaves em dicionários, enquanto listas não podem
- Tuplas geralmente são mais eficientes em termos de memória e desempenho
- Tuplas indicam ao leitor do código que os dados não devem ser modificados

## Dicionários

Os dicionários são estruturas de dados que armazenam pares de chave-valor, permitindo acesso rápido aos valores através de suas chaves. As chaves devem ser imutáveis (como strings, números ou tuplas).

### Criando Dicionários

```python
# Dicionário vazio
dicionario_vazio = {}
outro_vazio = dict()

# Dicionário com elementos
pessoa = {
    "nome": "Maria",
    "idade": 30,
    "profissao": "Engenheira"
}

# Usando a função dict()
pessoa = dict(nome="Maria", idade=30, profissao="Engenheira")

# Dicionário com diferentes tipos de chaves
misturado = {
    "string": "valor",
    10: "número como chave",
    (1, 2): "tupla como chave"
}
```

### Acessando e Modificando Valores

```python
pessoa = {
    "nome": "Maria",
    "idade": 30,
    "profissao": "Engenheira"
}

# Acessando valores
nome = pessoa["nome"]  # "Maria"

# Modificando valores
pessoa["idade"] = 31  # Atualiza a idade

# Adicionando novos pares chave-valor
pessoa["cidade"] = "São Paulo"  # Adiciona uma nova chave

# Removendo pares chave-valor
del pessoa["profissao"]  # Remove a chave "profissao" e seu valor

# Acessando com get() (evita erros se a chave não existir)
cidade = pessoa.get("cidade", "Não informada")  # Retorna "São Paulo"
pais = pessoa.get("pais", "Não informado")  # Retorna "Não informado" (chave não existe)

# Verificando se uma chave existe
tem_nome = "nome" in pessoa  # True
tem_pais = "pais" in pessoa  # False
```

### Métodos Úteis para Dicionários

```python
pessoa = {
    "nome": "Maria",
    "idade": 30,
    "profissao": "Engenheira",
    "cidade": "São Paulo"
}

# Obtendo todas as chaves
chaves = pessoa.keys()  # dict_keys(['nome', 'idade', 'profissao', 'cidade'])

# Obtendo todos os valores
valores = pessoa.values()  # dict_values(['Maria', 30, 'Engenheira', 'São Paulo'])

# Obtendo todos os pares chave-valor
itens = pessoa.items()  # dict_items([('nome', 'Maria'), ('idade', 30), ...])

# Atualizando com outro dicionário
atualizacoes = {"idade": 31, "estado_civil": "casada"}
pessoa.update(atualizacoes)  # Atualiza idade e adiciona estado_civil

# Removendo e retornando um item
profissao = pessoa.pop("profissao")  # Remove e retorna "Engenheira"

# Removendo e retornando o último item inserido (Python 3.7+)
ultimo_item = pessoa.popitem()  # Remove e retorna o último par adicionado

# Limpando o dicionário
pessoa.clear()  # Remove todos os itens
```

### Dicionários Aninhados

Os dicionários podem conter outros dicionários como valores, permitindo representar estruturas de dados mais complexas:

```python
alunos = {
    "João": {
        "idade": 20,
        "curso": "Engenharia",
        "notas": [8.5, 7.0, 9.0]
    },
    "Maria": {
        "idade": 22,
        "curso": "Medicina",
        "notas": [9.5, 9.0, 8.5]
    }
}

# Acessando dados aninhados
curso_joao = alunos["João"]["curso"]  # "Engenharia"
primeira_nota_maria = alunos["Maria"]["notas"][0]  # 9.5
```

### Compreensão de Dicionários

Assim como as listas, os dicionários também suportam compreensões:

```python
# Criando um dicionário de quadrados
quadrados = {x: x**2 for x in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Compreensão de dicionário com condição
pares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
# {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# Invertendo um dicionário (chaves viram valores e vice-versa)
original = {"a": 1, "b": 2, "c": 3}
invertido = {valor: chave for chave, valor in original.items()}
# {1: "a", 2: "b", 3: "c"}
```

## Conjuntos (Sets)

Os conjuntos são coleções não ordenadas de elementos únicos. Eles são úteis para operações como união, interseção e diferença, além de eliminar duplicatas de uma sequência.

### Criando Conjuntos

```python
# Conjunto vazio
conjunto_vazio = set()  # Não podemos usar {} pois isso cria um dicionário vazio

# Conjunto com elementos
frutas = {"maçã", "banana", "laranja"}

# Convertendo uma lista em conjunto (remove duplicatas)
numeros = [1, 2, 2, 3, 4, 4, 5]
conjunto_numeros = set(numeros)  # {1, 2, 3, 4, 5}
```

### Operações com Conjuntos

```python
# Adicionando elementos
frutas = {"maçã", "banana", "laranja"}
frutas.add("uva")  # {"maçã", "banana", "laranja", "uva"}

# Removendo elementos
frutas.remove("banana")  # Gera erro se o elemento não existir
frutas.discard("pera")   # Não gera erro se o elemento não existir

# Verificando se um elemento está no conjunto
tem_maca = "maçã" in frutas  # True

# Tamanho do conjunto
tamanho = len(frutas)  # 3
```

### Operações Matemáticas com Conjuntos

```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# União (elementos que estão em A OU em B)
uniao = A | B  # ou A.union(B)
# {1, 2, 3, 4, 5, 6, 7, 8}

# Interseção (elementos que estão em A E em B)
intersecao = A & B  # ou A.intersection(B)
# {4, 5}

# Diferença (elementos que estão em A mas não em B)
diferenca = A - B  # ou A.difference(B)
# {1, 2, 3}

# Diferença simétrica (elementos que estão em A ou em B, mas não em ambos)
dif_simetrica = A ^ B  # ou A.symmetric_difference(B)
# {1, 2, 3, 6, 7, 8}

# Verificando se um conjunto é subconjunto de outro
C = {1, 2}
eh_subconjunto = C <= A  # True (todos os elementos de C estão em A)

# Verificando se um conjunto é superconjunto de outro
eh_superconjunto = A >= C  # True (A contém todos os elementos de C)

# Verificando se dois conjuntos são disjuntos (não têm elementos em comum)
sao_disjuntos = A.isdisjoint({9, 10})  # True
```

### Compreensão de Conjuntos

```python
# Criando um conjunto com os quadrados dos números de 1 a 5
quadrados = {x**2 for x in range(1, 6)}
# {1, 4, 9, 16, 25}

# Compreensão de conjunto com condição
pares = {x for x in range(1, 11) if x % 2 == 0}
# {2, 4, 6, 8, 10}
```

## Exemplos Práticos

### Exemplo 1: Contagem de Palavras

```python
def contar_palavras(texto):
    """
    Conta a frequência de cada palavra em um texto.
    
    Parâmetros:
        texto (str): O texto a ser analisado
    
    Retorna:
        dict: Um dicionário com as palavras como chaves e suas contagens como valores
    """
    # Removendo pontuação e convertendo para minúsculas
    for pontuacao in ",.!?;:\"'()[]{}":
        texto = texto.replace(pontuacao, "")
    
    texto = texto.lower()
    
    # Dividindo o texto em palavras
    palavras = texto.split()
    
    # Contando as palavras
    contagem = {}
    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    
    return contagem

# Exemplo de uso
texto_exemplo = """
Python é uma linguagem de programação de alto nível, interpretada, 
de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. 
Python é uma linguagem muito popular e versátil.
"""

resultado = contar_palavras(texto_exemplo)

# Exibindo as palavras mais frequentes
palavras_ordenadas = sorted(resultado.items(), key=lambda x: x[1], reverse=True)
print("Palavras mais frequentes:")
for palavra, contagem in palavras_ordenadas[:5]:
    print(f"{palavra}: {contagem}")
```

### Exemplo 2: Gerenciamento de Contatos

```python
def exibir_menu():
    """Exibe o menu de opções."""
    print("\n=== Gerenciador de Contatos ===")
    print("1. Adicionar contato")
    print("2. Buscar contato")
    print("3. Listar todos os contatos")
    print("4. Atualizar contato")
    print("5. Remover contato")
    print("6. Sair")
    return input("Escolha uma opção (1-6): ")

def adicionar_contato(contatos):
    """Adiciona um novo contato ao dicionário."""
    nome = input("Nome: ")
    if nome in contatos:
        print(f"Contato '{nome}' já existe!")
        return
    
    telefone = input("Telefone: ")
    email = input("Email: ")
    
    contatos[nome] = {
        "telefone": telefone,
        "email": email
    }
    print(f"Contato '{nome}' adicionado com sucesso!")

def buscar_contato(contatos):
    """Busca um contato pelo nome."""
    nome = input("Digite o nome do contato: ")
    if nome in contatos:
        print(f"\nInformações de '{nome}':")
        print(f"Telefone: {contatos[nome]['telefone']}")
        print(f"Email: {contatos[nome]['email']}")
    else:
        print(f"Contato '{nome}' não encontrado!")

def listar_contatos(contatos):
    """Lista todos os contatos."""
    if not contatos:
        print("Nenhum contato cadastrado!")
        return
    
    print("\n=== Lista de Contatos ===")
    for nome, info in sorted(contatos.items()):
        print(f"Nome: {nome}")
        print(f"Telefone: {info['telefone']}")
        print(f"Email: {info['email']}")
        print("-" * 20)

def atualizar_contato(contatos):
    """Atualiza as informações de um contato existente."""
    nome = input("Digite o nome do contato a ser atualizado: ")
    if nome not in contatos:
        print(f"Contato '{nome}' não encontrado!")
        return
    
    print("Deixe em branco para manter o valor atual.")
    
    telefone = input(f"Novo telefone ({contatos[nome]['telefone']}): ")
    if telefone:
        contatos[nome]['telefone'] = telefone
    
    email = input(f"Novo email ({contatos[nome]['email']}): ")
    if email:
        contatos[nome]['email'] = email
    
    print(f"Contato '{nome}' atualizado com sucesso!")

def remover_contato(contatos):
    """Remove um contato do dicionário."
(Content truncated due to size limit. Use line ranges to read in chunks)