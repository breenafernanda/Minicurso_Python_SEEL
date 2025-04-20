# Lê o valor de X
X = int(input())

# Lê o valor de Z até que seja maior que X
while True:
    Z = int(input())
    if Z > X:
        break

# Inicializa a soma e o contador
soma = 0
contador = 0
valor = X

# Soma os números consecutivos até ultrapassar Z
while soma <= Z:
    soma += valor
    contador += 1
    valor += 1

# Imprime o número de valores somados
print(contador)
