def ultimo_analogimon():
    import sys
    input = sys.stdin.read
    data = input().strip().split("\n")
    
    i = 0
    while i < len(data):
        n, m = map(int, data[i].split())
        i += 1
        cidade = []
        pos1 = pos2 = None
        
        for r in range(n):
            linha = list(map(int, data[i].split()))
            cidade.append(linha)
            if 1 in linha:
                pos1 = (r, linha.index(1))
            if 2 in linha:
                pos2 = (r, linha.index(2))
            i += 1
        
        # Calcula a distância de Manhattan
        distancia = abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
        print(distancia)

ultimo_analogimon()
