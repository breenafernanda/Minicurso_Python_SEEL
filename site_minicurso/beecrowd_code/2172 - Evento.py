def evento_xp():
    while True:
        x, m = map(int, input().split())  # Lê os valores X e M
        if x == 0 and m == 0:  # Condição de parada
            break
        print(x * m)  # Calcula e exibe o novo valor de EXP

evento_xp()
