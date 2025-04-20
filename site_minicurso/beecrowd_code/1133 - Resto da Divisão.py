# Leitura dos valores de entrada
X = int(input())
Y = int(input())

# Determina o menor e o maior valor entre X e Y
menor = min(X, Y)
maior = max(X, Y)

# Itera sobre os valores entre menor e maior, excluindo os próprios X e Y
for numero in range(menor + 1, maior):
    # Verifica se o resto da divisão por 5 é 2 ou 3
    if numero % 5 == 2 or numero % 5 == 3:
        # Imprime o número que satisfaz a condição
        print(numero)
