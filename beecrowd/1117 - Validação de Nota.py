# Inicializa a lista para armazenar as notas válidas
notas_validas = []

# Continua solicitando notas até que duas válidas sejam inseridas
while len(notas_validas) < 2:
    # Lê uma nota do usuário
    nota = float(input())
    
    # Verifica se a nota está no intervalo válido
    if 0 <= nota <= 10:
        # Adiciona a nota à lista de notas válidas
        notas_validas.append(nota)
    else:
        # Informa que a nota é inválida
        print("nota invalida")

# Calcula a média das notas válidas
media = sum(notas_validas) / len(notas_validas)

# Exibe a média com duas casas decimais
print(f"media = {media:.2f}")
