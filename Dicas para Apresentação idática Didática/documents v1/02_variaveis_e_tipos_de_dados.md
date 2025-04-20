# Variáveis e Tipos de Dados em Python

## O que são Variáveis?

Em programação, uma variável é como uma caixa que guarda um valor. Esse valor pode ser um número, um texto, uma lista de itens ou qualquer outro tipo de dado. As variáveis nos permitem armazenar e manipular informações em nossos programas.

Em Python, criar uma variável é muito simples. Você só precisa escolher um nome para ela e atribuir um valor usando o operador de atribuição `=`.

```python
# Criando uma variável chamada 'idade' e atribuindo o valor 25
idade = 25

# Criando uma variável chamada 'nome' e atribuindo o texto "Maria"
nome = "Maria"

# Exibindo os valores das variáveis
print(idade)  # Exibe: 25
print(nome)   # Exibe: Maria
```

### Regras para Nomes de Variáveis

Em Python, os nomes de variáveis precisam seguir algumas regras:

1. Podem conter letras, números e o caractere underscore (_)
2. Devem começar com uma letra ou underscore, nunca com um número
3. Não podem ser palavras reservadas do Python (como `if`, `for`, `while`, etc.)
4. São sensíveis a maiúsculas e minúsculas (ou seja, `nome` e `Nome` são variáveis diferentes)

```python
# Exemplos de nomes válidos
idade = 25
nome_completo = "João Silva"
_contador = 0
valor1 = 100

# Exemplos de nomes inválidos
# 1valor = 10  # Não pode começar com número
# if = "teste"  # Não pode ser palavra reservada
```

### Boas Práticas para Nomear Variáveis

Além das regras obrigatórias, existem algumas boas práticas que ajudam a tornar seu código mais legível:

1. Use nomes descritivos que expliquem o propósito da variável
2. Em Python, é comum usar letras minúsculas com palavras separadas por underscore (snake_case)
3. Evite nomes muito curtos ou muito longos

```python
# Bons nomes de variáveis
idade_usuario = 25
total_vendas = 1500.50
esta_ativo = True

# Nomes não recomendados
a = 25  # Muito curto, não explica o propósito
valor_total_das_vendas_realizadas_no_mes = 1500.50  # Muito longo
```

## Tipos de Dados Básicos em Python

Python possui vários tipos de dados embutidos. Vamos conhecer os principais:

### Números Inteiros (int)

Representam números inteiros, positivos ou negativos, sem parte decimal.

```python
idade = 25
temperatura_negativa = -10
populacao_mundial = 7_900_000_000  # Underscores para facilitar a leitura
```

### Números de Ponto Flutuante (float)

Representam números reais, ou seja, números que podem ter parte decimal.

```python
altura = 1.75
temperatura = 36.5
pi = 3.14159
```

### Strings (str)

Representam texto. Em Python, strings podem ser definidas usando aspas simples (`'`) ou aspas duplas (`"`).

```python
nome = "Maria"
mensagem = 'Olá, mundo!'
endereco = "Rua das Flores, 123"

# Strings de múltiplas linhas usam três aspas
descricao = """Este é um texto
que ocupa várias
linhas."""
```

#### Operações com Strings

Strings em Python são muito versáteis e permitem várias operações:

```python
# Concatenação (juntar strings)
primeiro_nome = "João"
sobrenome = "Silva"
nome_completo = primeiro_nome + " " + sobrenome  # "João Silva"

# Repetição
linha = "-" * 20  # "--------------------"

# Acessando caracteres (indexação)
palavra = "Python"
primeira_letra = palavra[0]  # "P"
ultima_letra = palavra[5]    # "n"
# Também funciona com índices negativos (contando do final)
ultima_letra = palavra[-1]   # "n"

# Fatiamento (slicing)
linguagem = "Python"
primeiras_tres = linguagem[0:3]  # "Pyt"
ultimas_tres = linguagem[3:6]    # "hon"
# Formas abreviadas
primeiras_tres = linguagem[:3]   # "Pyt"
ultimas_tres = linguagem[3:]     # "hon"
```

#### Formatação de Strings

Python oferece várias formas de formatar strings, mas a mais moderna e recomendada é usando f-strings:

```python
nome = "Maria"
idade = 30

# Usando f-string (disponível a partir do Python 3.6)
mensagem = f"Olá, meu nome é {nome} e tenho {idade} anos."
print(mensagem)  # "Olá, meu nome é Maria e tenho 30 anos."

# Formatando números
pi = 3.14159
print(f"O valor de pi com duas casas decimais é {pi:.2f}")  # 3.14
```

### Booleanos (bool)

Representam valores de verdadeiro (True) ou falso (False). São fundamentais para expressões lógicas e estruturas de controle.

```python
esta_chovendo = True
tem_aula_hoje = False

# Booleanos também podem resultar de comparações
idade = 18
maior_de_idade = idade >= 18  # True
```

### Tipo None

O tipo `None` representa a ausência de valor ou um valor nulo. É frequentemente usado para inicializar variáveis que serão preenchidas posteriormente.

```python
resultado = None

# Verificando se uma variável é None
if resultado is None:
    print("Nenhum resultado disponível")
```

## Verificando o Tipo de uma Variável

Python oferece a função `type()` para verificar o tipo de uma variável:

```python
idade = 25
nome = "Maria"
altura = 1.75
ativo = True

print(type(idade))   # <class 'int'>
print(type(nome))    # <class 'str'>
print(type(altura))  # <class 'float'>
print(type(ativo))   # <class 'bool'>
```

## Conversão entre Tipos (Type Casting)

Muitas vezes precisamos converter um tipo de dado em outro. Python oferece funções para isso:

```python
# Convertendo para inteiro
texto_numero = "25"
numero = int(texto_numero)  # 25 (como inteiro)

preco = 19.99
preco_inteiro = int(preco)  # 19 (parte decimal é truncada)

# Convertendo para float
idade = 30
idade_float = float(idade)  # 30.0

texto_decimal = "3.14"
pi = float(texto_decimal)   # 3.14

# Convertendo para string
idade = 25
idade_texto = str(idade)    # "25"

# Convertendo para booleano
# Obs: Zero, strings vazias e None são considerados False, o resto é True
print(bool(0))       # False
print(bool(1))       # True
print(bool(""))      # False
print(bool("Olá"))   # True
print(bool(None))    # False
```

## Operadores em Python

### Operadores Aritméticos

```python
a = 10
b = 3

soma = a + b          # 13
subtracao = a - b     # 7
multiplicacao = a * b # 30
divisao = a / b       # 3.3333... (sempre retorna float)
divisao_inteira = a // b  # 3 (descarta a parte decimal)
resto = a % b         # 1 (resto da divisão)
potencia = a ** b     # 1000 (10 elevado a 3)
```

### Operadores de Atribuição

```python
x = 10        # Atribuição simples

# Atribuições combinadas
x += 5        # Equivalente a: x = x + 5
x -= 3        # Equivalente a: x = x - 3
x *= 2        # Equivalente a: x = x * 2
x /= 4        # Equivalente a: x = x / 4
x //= 2       # Equivalente a: x = x // 2
x %= 3        # Equivalente a: x = x % 3
x **= 2       # Equivalente a: x = x ** 2
```

### Operadores de Comparação

Retornam valores booleanos (True ou False):

```python
a = 10
b = 5

igual = a == b          # False
diferente = a != b      # True
maior = a > b           # True
menor = a < b           # False
maior_ou_igual = a >= b # True
menor_ou_igual = a <= b # False
```

### Operadores Lógicos

```python
x = 5
y = 10

# and: Verdadeiro se ambas as condições forem verdadeiras
resultado = x > 0 and y > 0  # True

# or: Verdadeiro se pelo menos uma condição for verdadeira
resultado = x > 10 or y > 0  # True

# not: Inverte o valor booleano
resultado = not (x > 10)     # True
```

## Entrada e Saída de Dados

### Saída de Dados com print()

A função `print()` é usada para exibir informações na tela:

```python
# Exibindo texto simples
print("Olá, mundo!")

# Exibindo valores de variáveis
nome = "Maria"
idade = 30
print("Nome:", nome)
print("Idade:", idade)

# Combinando texto e variáveis
print("Olá, meu nome é", nome, "e tenho", idade, "anos.")

# Usando f-strings (mais elegante)
print(f"Olá, meu nome é {nome} e tenho {idade} anos.")

# Controlando o separador
print("Python", "é", "incrível", sep="-")  # Python-é-incrível

# Controlando o final da linha
print("Isso não quebra linha", end=" ")
print("e continua aqui.")
```

### Entrada de Dados com input()

A função `input()` permite que o usuário digite informações:

```python
# Lendo uma string
nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")

# Lendo e convertendo para número
idade_texto = input("Digite sua idade: ")
idade = int(idade_texto)  # Converte para inteiro
print(f"Daqui a 10 anos você terá {idade + 10} anos.")

# Forma mais concisa
altura = float(input("Digite sua altura em metros: "))
print(f"Sua altura é {altura} metros.")
```

## Exemplo Prático: Calculadora Simples

Vamos criar uma calculadora simples que pede dois números ao usuário e realiza as quatro operações básicas:

```python
# Calculadora simples

# Entrada de dados
print("=== Calculadora Simples ===")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Processamento
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2

# Tratando a divisão por zero
if num2 != 0:
    divisao = num1 / num2
else:
    divisao = "Erro: divisão por zero"

# Saída de resultados
print("\nResultados:")
print(f"{num1} + {num2} = {soma}")
print(f"{num1} - {num2} = {subtracao}")
print(f"{num1} * {num2} = {multiplicacao}")
print(f"{num1} / {num2} = {divisao}")
```

## Exercícios Práticos

1. Crie um programa que peça o nome e a idade do usuário, e depois exiba uma mensagem personalizada.

2. Faça um programa que converta uma temperatura de Celsius para Fahrenheit. A fórmula é: F = C * 9/5 + 32.

3. Crie um programa que calcule a área e o perímetro de um retângulo, pedindo a base e a altura ao usuário.

4. Desenvolva um programa que calcule o IMC (Índice de Massa Corporal) de uma pessoa. A fórmula é: IMC = peso / (altura * altura).

## Conclusão

Neste capítulo, você aprendeu sobre variáveis e os tipos de dados básicos em Python, como criar e manipular variáveis, realizar operações com diferentes tipos de dados e interagir com o usuário através de entrada e saída de dados.

Esses conceitos são fundamentais para qualquer programa em Python e serão a base para os tópicos mais avançados que veremos nos próximos capítulos. Pratique bastante esses conceitos, pois eles serão usados constantemente em seus projetos de automação RPA.
