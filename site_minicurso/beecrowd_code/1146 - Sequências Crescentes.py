while True:
    # Lê um número inteiro X
    X = int(input())
    
    # Verifica se X é zero; se sim, encerra o loop
    if X == 0:
        break
    
    # Gera a sequência de 1 até X e converte cada número para string
    sequencia = [str(i) for i in range(1, X + 1)]
    
    # Junta a sequência em uma única string separada por espaços e imprime
    print(" ".join(sequencia))
