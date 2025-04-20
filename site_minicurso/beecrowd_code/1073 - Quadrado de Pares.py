# Lê o valor inteiro N
N = int(input().strip())

# Percorre de 1 até N, verificando os pares
for i in range(1, N + 1):
    if i % 2 == 0:
        print(f"{i}^2 = {i * i}")
