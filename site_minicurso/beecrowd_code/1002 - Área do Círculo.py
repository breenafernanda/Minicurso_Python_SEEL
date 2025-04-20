# A entrada contém um valor de ponto flutuante (dupla precisão), no caso, a variável raio.
raio = float(input())

# A fórmula para calcular a área de uma circunferência é: area = π . raio2. Considerando para este problema que π = 3.14159:
pi = 3.14159
area = pi * raio**2

# presentar a mensagem "A=" seguido pelo valor da variável area
print(f'A={area:.4f}')