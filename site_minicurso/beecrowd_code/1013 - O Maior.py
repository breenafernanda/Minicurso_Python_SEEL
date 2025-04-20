def calcular_maior(x, y):
    return (x + y + abs(x - y)) / 2

# Leitura dos três valores inteiros
a, b, c = map(int, input().split())

# Primeiro, calculamos o maior entre a e b
maior_ab = calcular_maior(a, b)

# Depois, calculamos o maior entre (maior_ab) e c
maior = calcular_maior(maior_ab, c)

# Imprimimos o resultado como inteiro (pois a fórmula retorna float) 
print(f"{int(maior)} eh o maior")