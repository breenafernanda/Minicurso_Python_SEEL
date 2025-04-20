def encontrar_sabre_de_luz():
    n, m = map(int, input().split())  # Lê dimensões do terreno
    terreno = [list(map(int, input().split())) for _ in range(n)]  # Lê os valores do terreno
    
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            # Verifica o padrão 42 cercado por 7 em todas as direções
            if (terreno[i][j] == 42 and
                terreno[i - 1][j - 1] == 7 and terreno[i - 1][j] == 7 and terreno[i - 1][j + 1] == 7 and
                terreno[i][j - 1] == 7 and terreno[i][j + 1] == 7 and
                terreno[i + 1][j - 1] == 7 and terreno[i + 1][j] == 7 and terreno[i + 1][j + 1] == 7):
                print(i + 1, j + 1)  # Saída com coordenadas (1-indexado)
                return
    
    print(0, 0)  # Padrão não encontrado

encontrar_sabre_de_luz()
