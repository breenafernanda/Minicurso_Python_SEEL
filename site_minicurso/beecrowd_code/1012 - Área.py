A, B, C = map(float, input().split())

# a) área do triângulo retângulo que tem A por base e C por altura
triangulo = (A * C) / 2

# b) área do círculo de raio C (pi = 3.14159)
circulo = 3.14159 * (C ** 2)

# c) área do trapézio que tem A e B por bases e C por altura
trapezio = ((A + B) / 2) * C

# d) área do quadrado que tem lado B
quadrado = B ** 2

# e) área do retângulo que tem lados A e B
retangulo = A * B

# Exibe os resultados com 3 casas decimais, seguindo o padrão do enunciado
print(f"TRIANGULO: {triangulo:.3f}")
print(f"CIRCULO: {circulo:.3f}")
print(f"TRAPEZIO: {trapezio:.3f}")
print(f"QUADRADO: {quadrado:.3f}")
print(f"RETANGULO: {retangulo:.3f}")