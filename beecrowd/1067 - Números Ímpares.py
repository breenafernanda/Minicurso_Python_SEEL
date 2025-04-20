# Lê o valor inteiro
x = int(input().strip())

# Percorre todos os valores de 1 até X
for i in range(1, x + 1):
    # Verifica se o número é ímpar
    if i % 2 != 0:
        print(i)
