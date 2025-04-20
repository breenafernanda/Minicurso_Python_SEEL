def cachorros_quentes():
    h, p = map(int, input().split())  # Lê o número de cachorros-quentes e participantes
    media = h / p  # Calcula a média de cachorros-quentes consumidos
    print(f"{media:.2f}")  # Exibe a média com 2 casas decimais

cachorros_quentes()
