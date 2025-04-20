# Lê a operação a ser realizada ('S' para soma, 'M' para média)
operacao = input().strip()

# Inicializa a matriz 12x12
matriz = []
for _ in range(12):
    linha = [float(input().strip()) for _ in range(12)]
    matriz.append(linha)

# Soma os elementos abaixo da diagonal principal
soma = 0
contador = 0
for i in range(12):
    for j in range(i):  # Apenas elementos abaixo da diagonal principal
        soma += matriz[i][j]
        contador += 1

# Calcula o resultado (soma ou média) e exibe
if operacao == 'S':
    print(f"{soma:.1f}")
elif operacao == 'M':
    media = soma / contador
    print(f"{media:.1f}")
