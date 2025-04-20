# Lê o número de linhas a serem impressas
N = int(input())

# Inicializa o contador inicial
contador = 1

# Loop para imprimir as linhas
for _ in range(N):
    # Imprime três números consecutivos seguidos de "PUM"
    print(f"{contador} {contador + 1} {contador + 2} PUM")
    # Incrementa o contador em 4 para a próxima linha
    contador += 4
