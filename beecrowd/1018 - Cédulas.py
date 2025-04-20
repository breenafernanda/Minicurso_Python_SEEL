# Lê o valor inteiro N
N = int(input().strip())

# Exibe o valor original
print(N)

# Lista das cédulas disponíveis
cedulas = [100, 50, 20, 10, 5, 2, 1]

# Variável auxiliar para decompor o valor
resto = N

# Para cada tipo de cédula, calcula quantas são necessárias
for cedula in cedulas:
    quantidade = resto // cedula  # Quantas notas 'cedula' cabem?
    resto = resto % cedula        # Atualiza o resto
    print(f"{quantidade} nota(s) de R$ {cedula},00")
