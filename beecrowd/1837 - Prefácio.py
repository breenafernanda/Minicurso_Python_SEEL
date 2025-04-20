# Lê os valores de a e b
a, b = map(int, input().strip().split())

# Calcula o quociente e o resto
if b < 0:
    q = (a // abs(b)) * -1
else:
    q = a // b

r = a - b * q

# Garante que o resto seja no intervalo 0 ≤ r < |b|
if r < 0:
    q -= 1
    r += abs(b)

# Imprime o quociente e o resto
print(q, r)
