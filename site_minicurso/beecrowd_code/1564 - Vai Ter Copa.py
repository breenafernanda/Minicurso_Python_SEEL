import sys

for line in sys.stdin:
    # Lê o número de reclamações
    N = int(line.strip())
    
    # Determina a saída com base no número de reclamações
    if N == 0:
        print("vai ter copa!")
    else:
        print("vai ter duas!")
