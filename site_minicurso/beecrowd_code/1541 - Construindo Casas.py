import math

while True:
    # Lê os valores A, B e C
    entrada = input().strip()
    if entrada == "0":
        break

    A, B, C = map(int, entrada.split())
    
    # Calcula a área da casa
    area_casa = A * B
    
    # Calcula o lado do terreno
    lado_terreno = math.sqrt(area_casa * 100 / C)
    
    # Exibe o resultado truncado para inteiro
    print(int(lado_terreno))
