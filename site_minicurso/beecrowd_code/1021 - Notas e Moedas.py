# Lemos o valor monetário como float
valor = float(input().strip())

# Convertendo tudo para centavos (inteiro) para evitar erros de ponto flutuante
# Exemplo: 576.73 * 100 -> 57673 centavos
total_centavos = int(round(valor * 100))

# Lista de notas em centavos (ex.: 100 Reais = 10000 centavos)
notas = [10000, 5000, 2000, 1000, 500, 200]

# Lista de moedas em centavos (ex.: 1 Real = 100 centavos, 0.50 = 50 centavos, etc.)
moedas = [100, 50, 25, 10, 5, 1]

print("NOTAS:")
for nota in notas:
    # Quantas notas desse tipo cabem?
    qtd_notas = total_centavos // nota
    print(f"{qtd_notas} nota(s) de R$ {nota/100:.2f}")
    # Atualiza o total de centavos que ainda falta decompor
    total_centavos %= nota

print("MOEDAS:")
for moeda in moedas:
    # Quantas moedas desse tipo cabem?
    qtd_moedas = total_centavos // moeda
    print(f"{qtd_moedas} moeda(s) de R$ {moeda/100:.2f}")
    # Atualiza o total de centavos remanescente
    total_centavos %= moeda
