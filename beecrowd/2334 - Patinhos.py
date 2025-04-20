def patinhos():
    while True:
        p = int(input())  # Lê o número total de patos
        if p == -1:  # Condição de parada
            break
        print(max(0, p - 1))  # Calcula e exibe os patinhos que voltaram

patinhos()
