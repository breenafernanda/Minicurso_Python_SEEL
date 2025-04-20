# Lê o valor inteiro
x = int(input().strip())

# Se X for par, ajusta para o próximo ímpar
if x % 2 == 0:
    x += 1

# Imprime os 6 ímpares consecutivos
for _ in range(6):
    print(x)
    x += 2
