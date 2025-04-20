def main():
    # Cardápio com preços dos produtos
    precos = {
        1001: 1.50,
        1002: 2.50,
        1003: 3.50,
        1004: 4.50,
        1005: 5.50
    }

    # Lê a quantidade de produtos comprados
    p = int(input())

    # Calcula o valor total da compra
    total = 0.0
    for _ in range(p):
        codigo, quantidade = map(int, input().split())
        total += precos[codigo] * quantidade

    # Imprime o valor total com duas casas decimais
    print(f"{total:.2f}")

if __name__ == "__main__":
    main()
