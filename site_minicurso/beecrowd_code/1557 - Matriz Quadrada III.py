while True:
    # Lê o valor de N
    N = int(input().strip())
    if N == 0:
        break  # Termina quando N é igual a 0

    # Calcula o maior valor da matriz para determinar o tamanho do campo
    max_valor = 2 ** (2 * (N - 1))
    T = len(str(max_valor))  # Tamanho do campo de impressão

    # Gera a matriz e imprime
    for i in range(N):
        linha = []
        for j in range(N):
            linha.append(str(2 ** (i + j)).rjust(T))  # Preenche com potências de 2 e ajusta o campo
        print(" ".join(linha))  # Imprime a linha formatada
    print()  # Linha em branco após cada matriz
