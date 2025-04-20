# Lê o número de casos de teste
T = int(input().strip())

for _ in range(T):
    # Lê os raios R1 e R2
    R1, R2 = map(int, input().split())
    
    # Calcula o menor raio do conduite
    menor_raio = R1 + R2
    
    # Imprime o resultado
    print(menor_raio)
