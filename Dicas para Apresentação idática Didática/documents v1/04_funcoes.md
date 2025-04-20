# Funções em Python

As funções são blocos de código reutilizáveis que realizam uma tarefa específica. Elas são fundamentais para organizar seu código, evitar repetição e tornar seus programas mais legíveis e fáceis de manter. Neste capítulo, vamos aprender como criar e usar funções em Python.

## Por que usar funções?

Antes de mergulharmos nos detalhes técnicos, vamos entender por que as funções são tão importantes:

1. **Reutilização de código**: Escreva o código uma vez e use-o várias vezes.
2. **Organização**: Divida seu programa em blocos lógicos e gerenciáveis.
3. **Abstração**: Esconda detalhes complexos atrás de interfaces simples.
4. **Manutenção**: Facilite a correção de erros e a atualização do código.

Pense nas funções como "mini-programas" dentro do seu programa principal. Cada função deve ter uma responsabilidade clara e bem definida.

## Definindo uma Função

Em Python, usamos a palavra-chave `def` para definir uma função:

```python
def nome_da_funcao():
    # Bloco de código
    # Indentado com 4 espaços
    print("Esta é uma função simples")
```

Elementos de uma função:
- A palavra-chave `def`
- O nome da função (seguindo as mesmas regras de nomeação de variáveis)
- Parênteses `()` (que podem conter parâmetros)
- Dois pontos `:`
- Um bloco de código indentado

## Chamando uma Função

Depois de definir uma função, você pode "chamá-la" (executá-la) usando seu nome seguido de parênteses:

```python
# Definindo a função
def saudacao():
    print("Olá! Bem-vindo ao Python!")

# Chamando a função
saudacao()  # Exibe: Olá! Bem-vindo ao Python!

# Você pode chamar a mesma função várias vezes
saudacao()  # Exibe novamente: Olá! Bem-vindo ao Python!
saudacao()  # E mais uma vez: Olá! Bem-vindo ao Python!
```

## Parâmetros e Argumentos

As funções se tornam muito mais poderosas quando podem receber informações para processar. Essas informações são chamadas de **parâmetros** (na definição da função) e **argumentos** (quando você chama a função).

### Parâmetros Simples

```python
# Função com um parâmetro
def saudacao_personalizada(nome):
    print(f"Olá, {nome}! Bem-vindo ao Python!")

# Chamando a função com um argumento
saudacao_personalizada("Maria")  # Exibe: Olá, Maria! Bem-vindo ao Python!
saudacao_personalizada("João")   # Exibe: Olá, João! Bem-vindo ao Python!
```

### Múltiplos Parâmetros

```python
# Função com múltiplos parâmetros
def exibir_informacoes(nome, idade, cidade):
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Cidade: {cidade}")

# Chamando a função com múltiplos argumentos
exibir_informacoes("Ana", 25, "São Paulo")
```

### Parâmetros com Valores Padrão

Você pode definir valores padrão para parâmetros, que serão usados caso o argumento correspondente não seja fornecido:

```python
# Função com parâmetros padrão
def saudacao_com_idioma(nome, idioma="português"):
    if idioma == "português":
        print(f"Olá, {nome}!")
    elif idioma == "inglês":
        print(f"Hello, {nome}!")
    elif idioma == "espanhol":
        print(f"¡Hola, {nome}!")
    else:
        print(f"Olá, {nome}!")

# Chamando a função com e sem o segundo argumento
saudacao_com_idioma("Carlos")             # Usa o valor padrão "português"
saudacao_com_idioma("Carlos", "inglês")   # Usa o valor fornecido "inglês"
saudacao_com_idioma("Carlos", "espanhol") # Usa o valor fornecido "espanhol"
```

### Argumentos Nomeados

Você pode especificar os argumentos pelo nome ao chamar uma função, o que torna o código mais legível e permite fornecer os argumentos em qualquer ordem:

```python
# Usando argumentos nomeados
exibir_informacoes(nome="Pedro", cidade="Rio de Janeiro", idade=30)

# Misturando argumentos posicionais e nomeados
# Os argumentos posicionais devem vir antes dos nomeados
exibir_informacoes("Pedro", cidade="Rio de Janeiro", idade=30)
```

### Número Variável de Argumentos

Python permite que você crie funções que aceitam um número variável de argumentos:

#### *args (Argumentos Posicionais Variáveis)

O parâmetro `*args` permite que a função receba qualquer número de argumentos posicionais, que serão armazenados em uma tupla:

```python
# Função com número variável de argumentos posicionais
def soma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    return resultado

# Chamando a função com diferentes números de argumentos
print(soma(1, 2))           # 3
print(soma(1, 2, 3))        # 6
print(soma(1, 2, 3, 4, 5))  # 15
```

#### **kwargs (Argumentos Nomeados Variáveis)

O parâmetro `**kwargs` permite que a função receba qualquer número de argumentos nomeados, que serão armazenados em um dicionário:

```python
# Função com número variável de argumentos nomeados
def exibir_pessoa(**dados):
    print("Dados da pessoa:")
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

# Chamando a função com diferentes argumentos nomeados
exibir_pessoa(nome="Ana", idade=25)
exibir_pessoa(nome="Carlos", idade=30, cidade="São Paulo", profissao="Engenheiro")
```

## Retornando Valores

Até agora, nossas funções apenas executavam ações (como exibir mensagens), mas não retornavam valores. Para que uma função retorne um valor, usamos a palavra-chave `return`:

```python
# Função que retorna um valor
def dobro(numero):
    return numero * 2

# Usando o valor retornado
resultado = dobro(5)
print(resultado)  # 10

# Você também pode usar o valor retornado diretamente
print(dobro(8))  # 16
```

Uma função pode retornar qualquer tipo de dado em Python, incluindo números, strings, listas, dicionários e até mesmo outras funções.

### Retornando Múltiplos Valores

Em Python, você pode retornar múltiplos valores de uma função usando uma tupla:

```python
# Função que retorna múltiplos valores
def calcular_estatisticas(numeros):
    soma = sum(numeros)
    media = soma / len(numeros)
    minimo = min(numeros)
    maximo = max(numeros)
    return soma, media, minimo, maximo

# Recebendo múltiplos valores retornados
lista = [10, 20, 30, 40, 50]
soma, media, minimo, maximo = calcular_estatisticas(lista)

print(f"Soma: {soma}")
print(f"Média: {media}")
print(f"Mínimo: {minimo}")
print(f"Máximo: {maximo}")
```

### Retorno Antecipado

A instrução `return` também pode ser usada para sair de uma função antes do final do seu bloco de código:

```python
# Função com retorno antecipado
def verificar_idade(idade):
    if idade < 0:
        print("Idade inválida!")
        return  # Sai da função sem retornar um valor específico
    
    if idade < 18:
        return "Menor de idade"
    else:
        return "Maior de idade"

# Testando a função
print(verificar_idade(-5))  # Exibe "Idade inválida!" e retorna None
print(verificar_idade(15))  # "Menor de idade"
print(verificar_idade(25))  # "Maior de idade"
```

## Escopo de Variáveis

O escopo de uma variável determina onde ela pode ser acessada no código. Em Python, temos principalmente dois tipos de escopo:

### Escopo Local

Variáveis definidas dentro de uma função têm escopo local e só podem ser acessadas dentro dessa função:

```python
def minha_funcao():
    # x é uma variável local
    x = 10
    print(f"Dentro da função: x = {x}")

minha_funcao()  # Exibe: Dentro da função: x = 10

# Tentar acessar x fora da função causaria um erro
# print(x)  # NameError: name 'x' is not defined
```

### Escopo Global

Variáveis definidas fora de qualquer função têm escopo global e podem ser acessadas de qualquer lugar do código:

```python
# y é uma variável global
y = 20

def minha_funcao():
    # Podemos acessar variáveis globais dentro de funções
    print(f"Dentro da função: y = {y}")

minha_funcao()  # Exibe: Dentro da função: y = 20
print(f"Fora da função: y = {y}")  # Exibe: Fora da função: y = 20
```

### Modificando Variáveis Globais

Se você quiser modificar uma variável global dentro de uma função, precisa usar a palavra-chave `global`:

```python
z = 30

def modificar_global():
    # Declaramos que queremos usar a variável global z
    global z
    z = 50
    print(f"Dentro da função: z = {z}")

print(f"Antes da função: z = {z}")  # Exibe: Antes da função: z = 30
modificar_global()  # Exibe: Dentro da função: z = 50
print(f"Depois da função: z = {z}")  # Exibe: Depois da função: z = 50
```

## Funções como Objetos de Primeira Classe

Em Python, funções são "objetos de primeira classe", o que significa que elas podem ser:

1. Atribuídas a variáveis
2. Passadas como argumentos para outras funções
3. Retornadas por outras funções
4. Armazenadas em estruturas de dados como listas e dicionários

Isso torna Python uma linguagem muito flexível e poderosa:

```python
# Atribuindo uma função a uma variável
def saudacao(nome):
    return f"Olá, {nome}!"

minha_funcao = saudacao
print(minha_funcao("Maria"))  # Exibe: Olá, Maria!

# Passando uma função como argumento
def aplicar_funcao(f, valor):
    return f(valor)

def quadrado(x):
    return x ** 2

resultado = aplicar_funcao(quadrado, 5)
print(resultado)  # Exibe: 25
```

## Funções Lambda (Funções Anônimas)

Python permite criar pequenas funções anônimas usando a palavra-chave `lambda`. Essas funções são úteis quando você precisa de uma função simples por um curto período de tempo:

```python
# Função lambda que retorna o dobro de um número
dobro = lambda x: x * 2
print(dobro(5))  # Exibe: 10

# Função lambda com múltiplos parâmetros
soma = lambda x, y: x + y
print(soma(3, 4))  # Exibe: 7

# Usando lambda com a função sorted()
alunos = [
    {"nome": "Ana", "nota": 8.5},
    {"nome": "Pedro", "nota": 7.0},
    {"nome": "Maria", "nota": 9.5}
]

# Ordenando a lista de alunos pela nota
alunos_ordenados = sorted(alunos, key=lambda aluno: aluno["nota"], reverse=True)
for aluno in alunos_ordenados:
    print(f"{aluno['nome']}: {aluno['nota']}")
```

## Docstrings: Documentando Funções

É uma boa prática documentar suas funções para que outros (e você mesmo no futuro) possam entender o que elas fazem. Em Python, usamos docstrings (strings de documentação):

```python
def calcular_area_retangulo(base, altura):
    """
    Calcula a área de um retângulo.
    
    Parâmetros:
        base (float): A base do retângulo
        altura (float): A altura do retângulo
    
    Retorna:
        float: A área do retângulo
    """
    return base * altura

# Acessando a documentação
print(calcular_area_retangulo.__doc__)

# Ou usando a função help()
help(calcular_area_retangulo)
```

## Funções Recursivas

Uma função recursiva é aquela que chama a si mesma. Isso pode ser útil para resolver problemas que podem ser divididos em subproblemas menores e similares:

```python
# Função recursiva para calcular o fatorial
def fatorial(n):
    """
    Calcula o fatorial de um número usando recursão.
    
    Parâmetros:
        n (int): O número para calcular o fatorial
    
    Retorna:
        int: O fatorial de n
    """
    # Caso base: fatorial de 0 ou 1 é 1
    if n <= 1:
        return 1
    # Caso recursivo: n! = n * (n-1)!
    else:
        return n * fatorial(n - 1)

# Testando a função
print(fatorial(5))  # 5! = 5 * 4 * 3 * 2 * 1 = 120
```

**Importante**: Funções recursivas sempre devem ter um "caso base" que não envolve recursão, caso contrário, elas entrarão em um loop infinito e causarão um erro de estouro de pilha.

## Exemplos Práticos

### Exemplo 1: Calculadora de IMC

```python
def calcular_imc(peso, altura):
    """
    Calcula o Índice de Massa Corporal (IMC).
    
    Parâmetros:
        peso (float): Peso em quilogramas
        altura (float): Altura em metros
    
    Retorna:
        float: O valor do IMC
    """
    return peso / (altura ** 2)

def interpretar_imc(imc):
    """
    Interpreta o valor do IMC conforme a tabela padrão.
    
    Parâmetros:
        imc (float): O valor do IMC
    
    Retorna:
        str: A interpretação do IMC
    """
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obesidade grau 1"
    elif imc < 40:
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3"

def main():
    """Função principal que interage com o usuário."""
    print("=== Calculadora de IMC ===")
    
    try:
        peso = float(input("Digite seu peso em kg: "))
        altura = float(input("Digite sua altura em metros: "))
        
        if peso <= 0 or altura <= 0:
            print("Erro: Peso e altura devem ser valores positivos.")
            return
        
        imc = calcular_imc(peso, altura)
        categoria = interpretar_imc(imc)
        
        print(f"\nSeu IMC é: {imc:.2f}")
        print(f"Classificação: {categoria}")
    
    except ValueError:
        print("Erro: Por favor, digite valores numéricos válidos.")

# Executando o programa
main()
```

### Exemplo 2: Conversor de Moedas

```python
def converter_moeda(valor, taxa_cambio, moeda_origem, moeda_destino):
    """
    Converte um valor de uma moeda para outra.
    
    Parâmetros:
        valor (float): Valor a ser convertido
        taxa_cambio (float): Taxa de câmbio
        moeda_origem (str): Código da moeda de origem
        moeda_destino (str): Código da moeda de destino
    
    Retorna:
        float: Valor convertido
    """
    valor_convertido = valor * taxa_cambio
    return valor_convertido

def formatar_moeda(valor, codigo_moeda):
    """
    Formata um valor monetário de acordo com o código da moeda.
    
    Parâmetros:
        valor (float): Valor a ser formatado
        codigo_moeda (str): Código da moeda
    
    Retorna:
        str: Valor formatado
    """
    if codigo_moeda == "BRL":
        return f"R$ {valor:.2f}"
    elif codigo_moeda == "USD":
        return f"US$ {valor:.2f}"
    elif codigo_moeda == "EUR":
        return f"€ {valor:.2f}"
    else:
        return f"{valor:.2f} {codigo_moeda}"

def main():
    """Função principal que interage com o usuário."""
    print("=== Conversor de Moedas ===")
    
    try:
        valor = float(input("Digite o valor a ser convertido: "))
        
        print("\nEscolha a moeda de origem:")
        print("1. Real Brasileiro (BRL)")
        print("2. Dólar Americano (USD)")
        print("3. Euro (EUR)")
        
        opcao_origem = input("Opção: ")
        if opcao_origem == "1":
            moeda_origem = "BRL"
        elif opcao_origem == "2":
            moeda_origem = "USD"
        elif opcao_origem == "3":
            moeda_origem = "EUR"
        else:
            print("Opção inválida!")
            return
        
        print("\nEscolha a moeda de destino:")
        print("1. Real Brasileiro (BRL)")
        print("2. Dólar Americano (USD)")
        print("3. Euro (EUR)")
        
        opcao_destino = input("Opção: ")
        if opcao_destino == "1":
            moeda_destino = "BRL"
        elif opcao_destino == "2":
            moeda_destino = "USD"
        elif opcao_destino == "3":
            moeda_destino = "EUR"
        else:
            print("Opção inválida!")
            return
        
        # Taxas de câmbio fictícias (em situações reais, seriam obtidas de uma API)
        taxas = {
            "BRL_USD": 0.2,    # 1 BRL = 0.2 USD
            "BRL_EUR": 0.18,   # 1 BRL = 0.18 EUR
            "USD_BRL": 5.0,    # 1 USD = 5.0 BRL
            "USD_EUR": 0.9,    # 1 USD = 0.9 EUR
            "EUR_BRL": 5.55,   # 1 EUR = 5.55 BRL
            "EUR_USD": 1.11    # 1 EUR = 1.11 USD
        }
        
        # Se origem e destino são iguais, a taxa é 1
        if moeda_origem == moeda_destino:
            taxa = 1
        else:
            chave_taxa = f"{moeda_origem}_{moeda_destino}"
            taxa = taxas.get(chave_taxa)
        
        if taxa is None:
            print("Conversão não suportada!")
            return
        
        valor_convertido = converter_moeda(valor, taxa, moeda_origem, moeda_destino)
        
        valor_formatado_origem = formatar_moeda(valor, moeda_origem)
        valor_formatado_destino = formatar_moed
(Content truncated due to size limit. Use line ranges to read in chunks)