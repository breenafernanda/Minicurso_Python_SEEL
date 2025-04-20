maior_valor = 0
posicao = 0

for i in range(1, 101):
    valor = int(input().strip())
    if valor > maior_valor:
        maior_valor = valor
        posicao = i

print(maior_valor)
print(posicao)
