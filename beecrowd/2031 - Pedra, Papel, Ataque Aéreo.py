def main():
    # Lê o número de casos de teste
    n = int(input().strip())

    for _ in range(n):
        # Lê as escolhas dos jogadores
        jogador1 = input().strip()
        jogador2 = input().strip()

        # Determina o resultado com base nas regras do jogo
        if jogador1 == "ataque" and jogador2 == "ataque":
            print("Aniquilacao mutua")
        elif jogador1 == "pedra" and jogador2 == "pedra":
            print("Sem ganhador")
        elif jogador1 == "papel" and jogador2 == "papel":
            print("Ambos venceram")
        elif jogador1 == "ataque" or (jogador1 == "pedra" and jogador2 == "papel") or (jogador1 == "ataque" and jogador2 != "ataque"):
            print("Jogador 1 venceu")
        else:
            print("Jogador 2 venceu")

if __name__ == "__main__":
    main()
