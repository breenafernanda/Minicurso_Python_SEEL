import sys

for line in sys.stdin:
    # Lê o número de lesmas (não usado diretamente no cálculo)
    L = int(line.strip())
    
    # Lê as velocidades das lesmas
    velocidades = list(map(int, input().strip().split()))
    
    # Determina a velocidade máxima
    max_velocidade = max(velocidades)
    
    # Classifica o nível baseado na velocidade máxima
    if max_velocidade < 10:
        print(1)
    elif max_velocidade < 20:
        print(2)
    else:
        print(3)
