while True:
    # Lê o tamanho da matriz
    N = int(input().strip())
    if N == 0:
        break  # Encerra quando o tamanho é 0

    # Inicializa e preenche a matriz
    matriz = []
    for i in range(N):
        linha = []
        for j in range(N):
            linha.append(abs(i - j) + 1)  # Calcula o valor da célula
        matriz.append(linha)

    # Imprime a matriz formatada
    for linha in matriz:
        print(" ".join(f"{num:3}" for num in linha))
    print()  # Linha em branco após cada matriz
