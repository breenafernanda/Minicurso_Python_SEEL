# Leitura dos dois valores inteiros
X = int(input())
Y = int(input())

# Determina o menor e o maior valor entre X e Y
menor = min(X, Y)
maior = max(X, Y)

# Inicializa a soma dos números não múltiplos de 13
soma = 0

# Itera sobre o intervalo de menor a maior, inclusive
for numero in range(menor, maior + 1):
    # Verifica se o número não é múltiplo de 13
    if numero % 13 != 0:
        # Adiciona o número à soma
        soma += numero

# Exibe o resultado da soma
print(soma)
