def main():
    import sys

    case_number = 1

    while True:
        try:
            # Lê os dois números
            n1 = input().strip()
            n2 = input().strip()

            # Procura as subsequências
            count = 0
            last_pos = -1
            start = 0

            while True:
                pos = n2.find(n1, start)
                if pos == -1:
                    break
                count += 1
                last_pos = pos + 1
                start = pos + 1

            # Imprime os resultados
            print(f"Caso #{case_number}:")
            if count > 0:
                print(f"Qtd.Subsequencias: {count}")
                print(f"Pos: {last_pos}")
            else:
                print("Nao existe subsequencia")
            print()

            case_number += 1

        except EOFError:
            break

if __name__ == "__main__":
    main()
