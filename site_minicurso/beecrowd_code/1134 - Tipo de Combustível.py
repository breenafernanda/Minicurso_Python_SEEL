# Inicializa os contadores para cada tipo de combustível
alcool = 0
gasolina = 0
diesel = 0

while True:
    # Lê o código do combustível
    codigo = int(input())
    
    # Verifica o código e atualiza o contador correspondente
    if codigo == 1:
        alcool += 1
    elif codigo == 2:
        gasolina += 1
    elif codigo == 3:
        diesel += 1
    elif codigo == 4:
        break  # Encerra o loop se o código for 4
    # Se o código for inválido (fora do intervalo 1 a 4), ignora e continua o loop

# Imprime os resultados
print("MUITO OBRIGADO")
print(f"Alcool: {alcool}")
print(f"Gasolina: {gasolina}")
print(f"Diesel: {diesel}")
