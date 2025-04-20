import sys

for line in sys.stdin:
    # Lê o tamanho da matriz
    N = int(line.strip())
    
    # Inicializa a matriz com zeros
    matriz = [[0 for _ in range(N)] for _ in range(N)]
    
    # Preenche as diagonais
    for i in range(N):
        matriz[i][i] = 2  # Diagonal principal
        matriz[i][N - i - 1] = 3  # Diagonal secundária

    # Determina a posição e tamanho do quadrado interno
    inicio = N // 3
    fim = N - inicio

    # Preenche o quadrado interno com 1
    for i in range(inicio, fim):
        for j in range(inicio, fim):
            matriz[i][j] = 1

    # Preenche o ponto central com 4
    matriz[N // 2][N // 2] = 4

    # Imprime a matriz
    for linha in matriz:
        print("".join(map(str, linha)))
    print()  # Linha em branco após cada matriz
