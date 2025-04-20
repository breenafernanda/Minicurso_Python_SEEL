# Lê o valor inteiro N
N = int(input().strip())

# Percorre de 1 até 10000 (inclusive) e verifica se num % N == 2
for num in range(1, 10001):
    if num % N == 2:
        print(num)
