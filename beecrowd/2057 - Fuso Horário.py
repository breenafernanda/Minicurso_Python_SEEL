def main():
    # Lê os valores de entrada
    S, T, F = map(int, input().split())

    # Calcula a hora de chegada
    chegada = (S + T + F) % 24

    # Ajusta o horário para o formato correto
    if chegada < 0:
        chegada += 24

    # Imprime a hora de chegada
    print(chegada)

if __name__ == "__main__":
    main()
