if __name__ == "__main__":
    # Lê os valores de P e N
    P, N = map(int, input().split())
    
    # Lê as alturas dos canos
    alturas = list(map(int, input().split()))
    
    # Verifica se o sapo consegue passar por todos os canos
    venceu = True
    for i in range(1, N):
        if abs(alturas[i] - alturas[i - 1]) > P:
            venceu = False
            break
    
    # Imprime o resultado
    print("YOU WIN" if venceu else "GAME OVER")
