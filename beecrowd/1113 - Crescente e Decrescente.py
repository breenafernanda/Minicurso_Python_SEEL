while True:
    # Lê os dois valores X e Y
    X, Y = map(int, input().split())
    
    # Verifica se os valores são iguais, encerra o loop
    if X == Y:
        break
    
    # Verifica a ordem e imprime o resultado
    if X < Y:
        print("Crescente")
    else:
        print("Decrescente")
