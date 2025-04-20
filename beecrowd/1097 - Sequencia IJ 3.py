# Loop para os valores de I de 1 a 9 com incremento de 2
for I in range(1, 10, 2):
    # Calcula o valor inicial de J para cada I
    J_inicial = I + 6
    # Loop para os valores de J, decrementando 1, total de 3 iterações
    for J in range(J_inicial, J_inicial - 3, -1):
        # Imprime os valores atuais de I e J
        print(f"I={I} J={J}")
