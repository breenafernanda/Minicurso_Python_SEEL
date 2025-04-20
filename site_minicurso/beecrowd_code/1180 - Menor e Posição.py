# Lê o número de elementos do vetor
N = int(input())

# Lê os elementos do vetor e converte-os para inteiros
X = list(map(int, input().split()))

# Inicializa o menor valor e sua posição
menor_valor = X[0]
posicao = 0

# Percorre o vetor para encontrar o menor valor e sua posição
for i in range(1, N):
    if X[i] < menor_valor:
        menor_valor = X[i]
        posicao = i

# Imprime o menor valor e sua posição
print(f"Menor valor: {menor_valor}")
print(f"Posicao: {posicao}")
