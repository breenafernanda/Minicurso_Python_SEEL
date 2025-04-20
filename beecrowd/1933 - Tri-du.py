if __name__ == "__main__":
    # Lê os valores das duas cartas
    A, B = map(int, input().split())
    
    # Determina o valor da terceira carta que maximiza as chances
    melhor_carta = A if A == B else max(A, B)
    
    # Imprime o resultado
    print(melhor_carta)
