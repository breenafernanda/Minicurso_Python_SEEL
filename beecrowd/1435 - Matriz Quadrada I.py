while True:
    # Lê o tamanho da matriz
    N = int(input().strip())
    if N == 0:
        break  # Termina a leitura ao encontrar 0

    # Inicializa a matriz N x N
    matriz = [[0] * N for _ in range(N)]

    # Preenche a matriz em camadas
    for camada in range((N + 1) // 2):
        for i in range(camada, N - camada):
            for j in range(camada, N - camada):
                matriz[i][j] = camada + 1

    # Imprime a matriz formatada
    for linha in matriz:
        print(" ".join(f"{num:3}" for num in linha))
    print()  # Linha em branco após cada matriz
