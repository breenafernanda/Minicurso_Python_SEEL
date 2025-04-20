# Lê a quantidade de valores
N = int(input().strip())

count_in = 0
count_out = 0

# Para cada valor, verifica se está no intervalo [10,20]
for _ in range(N):
    X = int(input().strip())
    if 10 <= X <= 20:
        count_in += 1
    else:
        count_out += 1

# Exibe o resultado
print(f"{count_in} in")
print(f"{count_out} out")
