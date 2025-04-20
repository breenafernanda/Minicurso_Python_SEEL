if __name__ == "__main__":
    # Lê a entrada e converte para inteiros
    tomadas = list(map(int, input().split()))

    # Calcula o número máximo de aparelhos conectáveis
    max_aparelhos = sum(tomadas) - 3

    # Imprime o resultado
    print(max_aparelhos)
