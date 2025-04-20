# Lê os dois valores inteiros
x = int(input().strip())
y = int(input().strip())

# Garante que x seja o menor e y o maior
if x > y:
    x, y = y, x

soma_impares = 0
# Percorre entre x+1 e y-1, somando somente os ímpares
for num in range(x + 1, y):
    if num % 2 != 0:
        soma_impares += num

print(soma_impares)
