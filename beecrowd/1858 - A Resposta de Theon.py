# Lê a quantidade de pessoas
n = int(input())

# Lê a lista de vezes que cada pessoa atinge Theon
t = list(map(int, input().split()))

# Encontra o índice da pessoa que bate menos vezes (menor valor de T)
menor_atingido = min(t)
resposta = t.index(menor_atingido) + 1  # Soma 1 para ajustar ao índice 1-based

# Exibe o resultado
print(resposta)
