import math

# Lê os 3 valores de ponto flutuante (A, B, C)
A, B, C = map(float, input().split())

# Calcula o discriminante (Delta = B^2 - 4*A*C)
delta = B**2 - 4*A*C

# Verifica se é possível calcular (A != 0 e delta >= 0)
if A == 0 or delta < 0:
    print("Impossivel calcular")
else:
    R1 = (-B + math.sqrt(delta)) / (2 * A)
    R2 = (-B - math.sqrt(delta)) / (2 * A)
    print(f"R1 = {R1:.5f}")
    print(f"R2 = {R2:.5f}")
