def main():
    import sys
    input = sys.stdin.read

    # Lê todos os casos de teste de uma só vez
    dados = input().strip().splitlines()
    caso = 1

    for linha in dados:
        # Converte o valor de N
        N = int(linha.strip())

        # Cria a sequência com base em N
        sequencia = [0]
        for i in range(1, N + 1):
            sequencia.extend([i] * i)

        # Calcula o número total de elementos
        total_numeros = len(sequencia)

        # Ajusta o plural de "numero"
        plural = "numero" if total_numeros == 1 else "numeros"

        # Imprime o resultado
        print(f"Caso {caso}: {total_numeros} {plural}")
        print(" ".join(map(str, sequencia)))
        print()  # Linha em branco após cada caso

        caso += 1

if __name__ == "__main__":
    main()
