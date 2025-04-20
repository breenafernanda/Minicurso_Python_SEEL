def principal():
    import sys
    entrada = sys.stdin.read
    dados = list(map(int, entrada().strip().split("\n")))
    
    A1, A2, A3 = dados

    # Calcular o tempo total para posicionar a máquina em cada andar
    tempo_andar_1 = 2 * A2 + 4 * A3
    tempo_andar_2 = 2 * A1 + 2 * A3
    tempo_andar_3 = 4 * A1 + 2 * A2

    # Encontrar o mínimo tempo total
    menor_tempo = min(tempo_andar_1, tempo_andar_2, tempo_andar_3)

    # Imprimir o resultado
    print(menor_tempo)

if __name__ == "__main__":
    principal()
