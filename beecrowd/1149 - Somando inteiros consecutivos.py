# Leitura dos valores de entrada
valores = list(map(int, input().split()))

# O primeiro valor é A
A = valores[0]

# Encontrar o primeiro N positivo
N = next(n for n in valores[1:] if n > 0)

# Calcular a soma de A até A + (N - 1)
soma = sum(A + i for i in range(N))

# Exibir o resultado
print(soma)
