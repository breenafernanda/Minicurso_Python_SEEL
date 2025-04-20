def crepusculo_em_portland():
    n = int(input())  # Lê o tamanho da matriz
    matriz = [list(map(int, input().split())) for _ in range(n + 1)]  # Lê a matriz (N+1 x N+1)
    
    for i in range(n):
        linha_resultado = ""
        for j in range(n):
            # Soma as câmeras nas quatro esquinas da quadra
            cameras = (matriz[i][j] + matriz[i][j + 1] +
                       matriz[i + 1][j] + matriz[i + 1][j + 1])
            # Verifica se a quadra é segura
            linha_resultado += "S" if cameras >= 2 else "U"
        print(linha_resultado)

crepusculo_em_portland()
