# Lê um valor inteiro V
V = int(input())

# Inicializa o vetor N com 10 posições
N = [0] * 10

# Atribui o valor inicial à primeira posição do vetor
N[0] = V

# Preenche as demais posições com o dobro do valor anterior
for i in range(1, 10):
    N[i] = N[i - 1] * 2

# Exibe o vetor conforme o formato solicitado
for i in range(10):
    print(f"N[{i}] = {N[i]}")
