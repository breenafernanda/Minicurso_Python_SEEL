import sys

def principal():
    entrada = sys.stdin.read
    dados = entrada().strip().split("\n")
    
    indice = 0
    resultados = []
    
    while indice < len(dados):
        # Ler número de pessoas e datas
        N, D = map(int, dados[indice].split())
        indice += 1

        data_encontrada = "Pizza antes de FdI"
        
        for _ in range(D):
            linha = dados[indice].split()
            indice += 1
            
            data = linha[0]
            disponibilidade = list(map(int, linha[1:]))
            
            # Verificar se todos podem comparecer
            if sum(disponibilidade) == N and data_encontrada == "Pizza antes de FdI":
                data_encontrada = data
        
        resultados.append(data_encontrada)
    
    # Imprimir resultados
    print("\n".join(resultados))

if __name__ == "__main__":
    principal()
