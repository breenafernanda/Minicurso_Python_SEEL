def raiz_quadrada_de_2():
    n = int(input())  # Lê o número de repetições
    resultado = 0
    for _ in range(n):
        resultado = 1 / (2 + resultado)  # Atualiza o denominador
    resultado += 1  # Soma 1 no final
    print(f"{resultado:.10f}")  # Exibe com 10 casas decimais

raiz_quadrada_de_2()
