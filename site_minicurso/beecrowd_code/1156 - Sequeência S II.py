# Inicializa a variável S com 0
S = 0.0

# Inicializa o numerador e o denominador
numerador = 1
denominador = 1

# Calcula a soma dos termos até o numerador ser 39
while numerador <= 39:
    S += numerador / denominador
    numerador += 2
    denominador *= 2

# Exibe o resultado com duas casas decimais
print(f"{S:.2f}")
