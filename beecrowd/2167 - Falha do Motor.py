def falha_do_motor():
    n = int(input())  # Lê o número de medidas
    velocidades = list(map(int, input().split()))  # Lê os valores de RPM
    
    for i in range(1, n):
        if velocidades[i] < velocidades[i - 1]:  # Verifica a primeira queda
            print(i + 1)  # Retorna o índice da queda (1-indexado)
            return
    
    print(0)  # Nenhuma queda encontrada

falha_do_motor()
