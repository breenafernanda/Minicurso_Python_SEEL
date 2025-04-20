def principal():
    import sys
    entrada = sys.stdin.read
    dados = entrada().strip().split("\n")
    
    indice = 0
    resultados = []
    
    while indice < len(dados):
        # Ler número de palavras pesquisadas
        N = int(dados[indice])
        indice += 1

        # Armazenar as palavras pesquisadas
        palavras = []
        for _ in range(N):
            palavras.append(dados[indice])
            indice += 1

        # Ler número de consultas
        Q = int(dados[indice])
        indice += 1

        for _ in range(Q):
            consulta = dados[indice]
            indice += 1

            # Filtrar palavras que começam com a string da consulta
            sugestoes = [palavra for palavra in palavras if palavra.startswith(consulta)]

            if sugestoes:
                quantidade = len(sugestoes)
                maior_tamanho = max(len(palavra) for palavra in sugestoes)
                resultados.append(f"{quantidade} {maior_tamanho}")
            else:
                resultados.append("-1")
    
    # Imprimir resultados
    print("\n".join(resultados))

if __name__ == "__main__":
    principal()
