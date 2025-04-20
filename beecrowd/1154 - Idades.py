# Inicializa variáveis para armazenar a soma das idades e a contagem de entradas válidas
soma_idades = 0
contador = 0

while True:
    # Lê a idade do usuário
    idade = int(input())
    
    # Verifica se a idade é negativa; se sim, encerra o loop
    if idade < 0:
        break
    
    # Adiciona a idade à soma total e incrementa o contador
    soma_idades += idade
    contador += 1

# Calcula a média das idades, garantindo que o contador seja maior que zero
if contador > 0:
    media = soma_idades / contador
    # Exibe a média com duas casas decimais
    print(f"{media:.2f}")
