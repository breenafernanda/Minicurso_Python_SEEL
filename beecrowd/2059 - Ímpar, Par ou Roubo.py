def main():
    # Lê a entrada
    p, j1, j2, r, a = map(int, input().split())

    # Verifica se o jogador 1 roubou e se foi acusado
    if r == 1:
        if a == 1:
            print("Jogador 2 ganha!")
        else:
            print("Jogador 1 ganha!")
    else:
        if a == 1:
            print("Jogador 1 ganha!")
        else:
            # Jogo normal
            soma = j1 + j2
            if (soma % 2 == 0 and p == 1) or (soma % 2 != 0 and p == 0):
                print("Jogador 1 ganha!")
            else:
                print("Jogador 2 ganha!")

if __name__ == "__main__":
    main()
