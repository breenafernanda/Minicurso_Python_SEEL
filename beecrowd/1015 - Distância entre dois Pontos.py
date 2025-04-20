import math

# 1ª linha de entrada: x1 e y1
x1, y1 = map(float, input().split())
# 2ª linha de entrada: x2 e y2
x2, y2 = map(float, input().split())

# Fórmula da distância no plano 2D:
# distancia = sqrt((x2 - x1)^2 + (y2 - y1)^2)
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Exibição do resultado com 4 casas decimais
print(f"{distancia:.4f}")
