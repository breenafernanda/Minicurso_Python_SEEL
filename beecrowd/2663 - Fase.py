def principal():
    import sys
    entrada = sys.stdin.read
    dados = entrada().strip().split("\n")
    
    # Número de competidores
    N = int(dados[0])
    # Número mínimo de vagas
    K = int(dados[1])
    # Pontuações dos competidores
    pontuacoes = sorted([int(dados[i]) for i in range(2, 2 + N)], reverse=True)
    
    # Pontuação na posição K
    pontuacao_corte = pontuacoes[K - 1]
    
    # Contar todos os competidores com pontuação >= pontuacao_corte
    classificados = sum(1 for p in pontuacoes if p >= pontuacao_corte)
    
    # Imprimir o número de classificados
    print(classificados)

if __name__ == "__main__":
    principal()
