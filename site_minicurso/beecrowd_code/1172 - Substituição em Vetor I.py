# Inicializa uma lista para armazenar os valores
X = []

# Lê 10 valores inteiros
for i in range(10):
    valor = int(input())
    # Substitui valores nulos ou negativos por 1
    if valor <= 0:
        valor = 1
    X.append(valor)
    # Exibe o valor armazenado na posição i
    print(f"X[{i}] = {valor}")
