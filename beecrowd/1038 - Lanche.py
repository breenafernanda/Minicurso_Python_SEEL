# Tabela de preços de acordo com o enunciado:
# Código: 1 => R$ 4.00
# Código: 2 => R$ 4.50
# Código: 3 => R$ 5.00
# Código: 4 => R$ 2.00
# Código: 5 => R$ 1.50

# Lê o código do item e a quantidade desejada
codigo, quantidade = map(int, input().split())

# Dicionário que mapeia 'código -> preço'
precos = {
    1: 4.00,
    2: 4.50,
    3: 5.00,
    4: 2.00,
    5: 1.50
}

# Calcula o total a pagar
total = precos[codigo] * quantidade

# Exibe o resultado com 2 casas decimais
print(f"Total: R$ {total:.2f}")
