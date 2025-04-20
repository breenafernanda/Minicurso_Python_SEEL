# Lê o número de casos de teste
T = int(input())

# Processa cada caso de teste
for _ in range(T):
    # Lê os valores de entrada para o caso
    PA, PB, G1, G2 = map(float, input().split())
    PA = int(PA)
    PB = int(PB)
    
    anos = 0
    
    # Simula o crescimento populacional
    while PA <= PB:
        # Incrementa a população considerando o crescimento anual
        PA += int(PA * (G1 / 100))
        PB += int(PB * (G2 / 100))
        anos += 1
        
        # Interrompe se passar de 100 anos
        if anos > 100:
            print("Mais de 1 seculo.")
            break
    else:
        # Se saiu do loop antes de 100 anos, imprime o resultado
        print(f"{anos} anos.")
