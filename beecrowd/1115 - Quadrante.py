while True:
    # Lê as coordenadas X e Y
    X, Y = map(int, input().split())
    
    # Verifica se alguma das coordenadas é zero; se sim, encerra o loop
    if X == 0 or Y == 0:
        break
    
    # Determina e imprime o quadrante correspondente
    if X > 0 and Y > 0:
        print("primeiro")
    elif X < 0 and Y > 0:
        print("segundo")
    elif X < 0 and Y < 0:
        print("terceiro")
    elif X > 0 and Y < 0:
        print("quarto")
