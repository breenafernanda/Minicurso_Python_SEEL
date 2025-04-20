# Inicializa a variável S com 0
S = 0.0

# Calcula a soma dos inversos de 1 até 100
for i in range(1, 101):
    S += 1 / i

# Exibe o resultado com duas casas decimais
print(f"{S:.2f}")
