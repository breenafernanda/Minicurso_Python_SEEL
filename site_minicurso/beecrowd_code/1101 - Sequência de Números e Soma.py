while True:
    # Lê os dois valores M e N
    M, N = map(int, input().split())
    
    # Verifica se algum valor é menor ou igual a zero, finaliza o loop
    if M <= 0 or N <= 0:
        break
    
    # Determina o menor e maior valor entre M e N
    menor = min(M, N)
    maior = max(M, N)
    
    # Gera a sequência e calcula a soma
    sequencia = list(range(menor, maior + 1))
    soma = sum(sequencia)
    
    # Formata a sequência e a soma para a saída
    sequencia_str = " ".join(map(str, sequencia))
    print(f"{sequencia_str} Sum={soma}")
