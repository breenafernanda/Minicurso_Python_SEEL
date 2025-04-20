# Lê a coluna que será considerada
C = int(input())

# Lê o tipo de operação (S para soma, M para média)
T = input().strip()

# Inicializa a matriz 12x12
matriz = []

# Lê os valores da matriz
for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)

# Calcula a soma dos elementos da coluna C
soma = sum(matriz[i][C] for i in range(12))

# Realiza a operação escolhida
if T == 'S':
    resultado = soma
elif T == 'M':
    resultado = soma / 12

# Exibe o resultado com uma casa decimal
print(f"{resultado:.1f}")
