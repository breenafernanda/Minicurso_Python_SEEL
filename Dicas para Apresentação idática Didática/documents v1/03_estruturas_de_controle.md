# Estruturas de Controle em Python

As estruturas de controle são fundamentais em qualquer linguagem de programação, pois permitem que você controle o fluxo de execução do seu código. Em Python, as principais estruturas de controle são as estruturas condicionais (if, elif, else) e as estruturas de repetição (for, while).

## Estruturas Condicionais

As estruturas condicionais permitem que seu programa tome decisões com base em condições. Elas executam diferentes blocos de código dependendo se uma condição é verdadeira ou falsa.

### A Estrutura if

A estrutura `if` é a mais básica das estruturas condicionais. Ela executa um bloco de código apenas se a condição especificada for verdadeira (True).

```python
# Sintaxe básica do if
if condição:
    # Código a ser executado se a condição for verdadeira
    # Este bloco deve estar indentado
```

Exemplo prático:

```python
idade = 18

if idade >= 18:
    print("Você é maior de idade.")
    print("Pode entrar na festa.")
```

### A Estrutura if-else

A estrutura `if-else` permite executar um bloco de código se a condição for verdadeira e outro bloco se a condição for falsa.

```python
# Sintaxe do if-else
if condição:
    # Código a ser executado se a condição for verdadeira
else:
    # Código a ser executado se a condição for falsa
```

Exemplo prático:

```python
idade = 16

if idade >= 18:
    print("Você é maior de idade.")
    print("Pode entrar na festa.")
else:
    print("Você é menor de idade.")
    print("Não pode entrar na festa.")
```

### A Estrutura if-elif-else

A estrutura `if-elif-else` permite verificar múltiplas condições em sequência. O Python verifica cada condição na ordem e executa o bloco de código da primeira condição verdadeira. Se nenhuma condição for verdadeira, o bloco `else` é executado (se existir).

```python
# Sintaxe do if-elif-else
if condição1:
    # Código a ser executado se condição1 for verdadeira
elif condição2:
    # Código a ser executado se condição1 for falsa e condição2 for verdadeira
elif condição3:
    # Código a ser executado se condição1 e condição2 forem falsas e condição3 for verdadeira
else:
    # Código a ser executado se todas as condições anteriores forem falsas
```

Exemplo prático:

```python
nota = 85

if nota >= 90:
    print("Conceito A")
elif nota >= 80:
    print("Conceito B")
elif nota >= 70:
    print("Conceito C")
elif nota >= 60:
    print("Conceito D")
else:
    print("Conceito F")
```

Neste exemplo, como a nota é 85, a saída será "Conceito B". O Python verifica cada condição na ordem e para na primeira que for verdadeira.

### Condições Aninhadas

Você também pode aninhar estruturas condicionais, ou seja, colocar uma estrutura condicional dentro de outra:

```python
idade = 18
tem_carteira = True

if idade >= 18:
    if tem_carteira:
        print("Pode dirigir.")
    else:
        print("Não pode dirigir. Precisa tirar a carteira.")
else:
    print("Não pode dirigir. É menor de idade.")
```

### Operadores Lógicos em Condições

Os operadores lógicos `and`, `or` e `not` são muito úteis para combinar ou negar condições:

```python
idade = 25
tem_carteira = True

# Usando AND: ambas as condições devem ser verdadeiras
if idade >= 18 and tem_carteira:
    print("Pode dirigir.")
else:
    print("Não pode dirigir.")

# Usando OR: pelo menos uma condição deve ser verdadeira
tem_passaporte = False
tem_rg = True

if tem_passaporte or tem_rg:
    print("Pode fazer a identificação.")
else:
    print("Não tem documento válido.")

# Usando NOT: inverte o valor da condição
esta_chovendo = False

if not esta_chovendo:
    print("Não precisa de guarda-chuva.")
else:
    print("Leve um guarda-chuva.")
```

## Estruturas de Repetição

As estruturas de repetição, também conhecidas como loops, permitem executar um bloco de código várias vezes. Python oferece duas estruturas principais: `for` e `while`.

### O Loop for

O loop `for` é usado para iterar sobre uma sequência (como uma lista, tupla, dicionário, conjunto ou string) ou outros objetos iteráveis. É especialmente útil quando você sabe antecipadamente o número de iterações.

```python
# Sintaxe básica do for
for variável in sequência:
    # Código a ser executado em cada iteração
```

Exemplos práticos:

```python
# Iterando sobre uma string
for letra in "Python":
    print(letra)
# Saída:
# P
# y
# t
# h
# o
# n

# Iterando sobre uma lista
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(f"Eu gosto de {fruta}")
# Saída:
# Eu gosto de maçã
# Eu gosto de banana
# Eu gosto de laranja

# Usando a função range() para gerar uma sequência de números
for i in range(5):  # range(5) gera os números de 0 a 4
    print(i)
# Saída:
# 0
# 1
# 2
# 3
# 4

# range() com início e fim
for i in range(2, 6):  # Números de 2 a 5
    print(i)
# Saída:
# 2
# 3
# 4
# 5

# range() com início, fim e passo
for i in range(1, 10, 2):  # Números ímpares de 1 a 9
    print(i)
# Saída:
# 1
# 3
# 5
# 7
# 9
```

### O Loop while

O loop `while` executa um bloco de código enquanto uma condição for verdadeira. É útil quando você não sabe antecipadamente quantas iterações serão necessárias.

```python
# Sintaxe básica do while
while condição:
    # Código a ser executado enquanto a condição for verdadeira
```

Exemplos práticos:

```python
# Contagem regressiva
contagem = 5
while contagem > 0:
    print(contagem)
    contagem -= 1  # Equivalente a: contagem = contagem - 1
print("Lançamento!")
# Saída:
# 5
# 4
# 3
# 2
# 1
# Lançamento!

# Loop com entrada do usuário
resposta = ""
while resposta.lower() != "sim":
    resposta = input("Você quer sair? (sim/não): ")
print("Programa encerrado.")
```

**Atenção**: É importante garantir que a condição do `while` eventualmente se torne falsa, caso contrário, você terá um "loop infinito" que nunca termina (a menos que seja interrompido manualmente).

### Controlando Loops com break, continue e else

Python oferece comandos especiais para controlar o fluxo dentro de loops:

#### break

O comando `break` interrompe o loop completamente, mesmo que a condição ainda seja verdadeira:

```python
# Usando break para sair de um loop
for i in range(1, 11):
    if i == 5:
        print("Encontrei o 5! Saindo do loop...")
        break
    print(i)
# Saída:
# 1
# 2
# 3
# 4
# Encontrei o 5! Saindo do loop...
```

#### continue

O comando `continue` pula a iteração atual e passa para a próxima:

```python
# Usando continue para pular uma iteração
for i in range(1, 6):
    if i == 3:
        print("Pulando o número 3...")
        continue
    print(i)
# Saída:
# 1
# 2
# Pulando o número 3...
# 4
# 5
```

#### else em loops

Tanto o `for` quanto o `while` podem ter uma cláusula `else` que é executada quando o loop termina normalmente (sem ser interrompido por um `break`):

```python
# Usando else com for
for i in range(1, 6):
    print(i)
else:
    print("Loop concluído com sucesso!")
# Saída:
# 1
# 2
# 3
# 4
# 5
# Loop concluído com sucesso!

# Usando else com for e break
for i in range(1, 6):
    if i == 3:
        break
    print(i)
else:
    print("Este texto não será exibido porque o loop foi interrompido pelo break")
# Saída:
# 1
# 2
```

## A Importância da Indentação em Python

Em Python, a indentação (os espaços no início de cada linha) não é apenas uma questão de estilo, mas define a estrutura do código. Blocos de código são definidos pela indentação, não por chaves ou palavras-chave como em outras linguagens.

```python
# Indentação correta
if idade >= 18:
    print("Maior de idade")
    if tem_carteira:
        print("Pode dirigir")
else:
    print("Menor de idade")
    print("Não pode dirigir")

# Indentação incorreta causaria erros
if idade >= 18:
print("Maior de idade")  # Erro: falta indentação
    if tem_carteira:
        print("Pode dirigir")
else:
    print("Menor de idade")
print("Não pode dirigir")  # Este print não faz parte do bloco else
```

A convenção em Python é usar 4 espaços para cada nível de indentação.

## Exemplos Práticos Combinando Estruturas de Controle

### Exemplo 1: Verificador de Números Primos

```python
# Programa para verificar se um número é primo
numero = int(input("Digite um número inteiro positivo: "))

if numero <= 1:
    print(f"{numero} não é um número primo.")
else:
    eh_primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            eh_primo = False
            break
    
    if eh_primo:
        print(f"{numero} é um número primo.")
    else:
        print(f"{numero} não é um número primo.")
```

### Exemplo 2: Jogo de Adivinhação

```python
import random

# Gera um número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)
tentativas = 0
max_tentativas = 10

print("Bem-vindo ao Jogo de Adivinhação!")
print(f"Você tem {max_tentativas} tentativas para adivinhar um número entre 1 e 100.")

while tentativas < max_tentativas:
    tentativa = int(input("\nDigite sua tentativa: "))
    tentativas += 1
    
    if tentativa < numero_secreto:
        print("Tente um número MAIOR.")
    elif tentativa > numero_secreto:
        print("Tente um número MENOR.")
    else:
        print(f"Parabéns! Você acertou em {tentativas} tentativas!")
        break
    
    print(f"Tentativas restantes: {max_tentativas - tentativas}")
else:
    print(f"\nSuas tentativas acabaram! O número secreto era {numero_secreto}.")
```

### Exemplo 3: Calculadora com Menu

```python
# Calculadora simples com menu de opções

while True:
    print("\n=== Calculadora ===")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")
    
    opcao = input("\nEscolha uma opção (1-5): ")
    
    if opcao == '5':
        print("Obrigado por usar a calculadora. Até logo!")
        break
    
    if opcao in ('1', '2', '3', '4'):
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        if opcao == '1':
            print(f"{num1} + {num2} = {num1 + num2}")
        elif opcao == '2':
            print(f"{num1} - {num2} = {num1 - num2}")
        elif opcao == '3':
            print(f"{num1} * {num2} = {num1 * num2}")
        elif opcao == '4':
            if num2 == 0:
                print("Erro: Divisão por zero!")
            else:
                print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Opção inválida! Por favor, escolha uma opção de 1 a 5.")
```

## Exercícios Práticos

1. Crie um programa que peça a idade do usuário e informe se ele pode votar (idade >= 16) e se o voto é obrigatório (idade entre 18 e 70) ou facultativo.

2. Faça um programa que calcule a soma de todos os números de 1 até um número informado pelo usuário.

3. Crie um programa que exiba a tabuada de um número informado pelo usuário.

4. Desenvolva um programa que peça ao usuário para digitar uma senha. O programa deve continuar pedindo a senha até que o usuário digite a senha correta "python123".

5. Faça um programa que leia 5 números e informe o maior, o menor e a média deles.

## Conclusão

As estruturas de controle são essenciais para criar programas dinâmicos e interativos. Com as estruturas condicionais (if, elif, else), você pode fazer seu programa tomar decisões com base em diferentes condições. Com as estruturas de repetição (for, while), você pode executar blocos de código repetidamente, economizando tempo e tornando seu código mais eficiente.

Dominar essas estruturas é fundamental para avançar na programação Python e, especialmente, para desenvolver soluções de RPA (Robotic Process Automation), onde frequentemente precisamos tomar decisões baseadas em condições e repetir ações várias vezes.

No próximo capítulo, vamos explorar as funções em Python, que nos permitirão organizar melhor nosso código e reutilizar blocos de código em diferentes partes do programa.
