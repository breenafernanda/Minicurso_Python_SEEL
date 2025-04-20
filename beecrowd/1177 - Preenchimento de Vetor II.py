# Lê o valor de T
T = int(input())

# Inicializa o vetor N com 1000 posições
N = [0] * 1000

# Preenche o vetor N com a sequência de 0 até T-1 repetidamente
for i in range(1000):
    N[i] = i % T

# Exibe o vetor conforme o formato solicitado
for i in range(1000):
    print(f"N[{i}] = {N[i]}")
