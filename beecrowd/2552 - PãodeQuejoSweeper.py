import sys

def principal():
    entrada = sys.stdin.read
    dados = entrada().strip().split("\n")
    
    indice = 0
    resultados = []
    
    while indice < len(dados):
        # Ler dimensões da matriz
        N, M = map(int, dados[indice].split())
        indice += 1

        # Ler o tabuleiro inicial
        tabuleiro = []
        for _ in range(N):
            tabuleiro.append(list(map(int, dados[indice].split())))
            indice += 1
        
        # Gerar o tabuleiro de saída
        tabuleiro_saida = [[0] * M for _ in range(N)]
        
        for i in range(N):
            for j in range(M):
                if tabuleiro[i][j] == 1:
                    tabuleiro_saida[i][j] = 9
                else:
                    # Contar pães de queijo adjacentes
                    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < N and 0 <= nj < M and tabuleiro[ni][nj] == 1:
                            tabuleiro_saida[i][j] += 1
        
        # Adicionar o resultado formatado
        for linha in tabuleiro_saida:
            resultados.append("".join(map(str, linha)))
    
    # Imprimir resultados
    print("\n".join(resultados))

if __name__ == "__main__":
    principal()
