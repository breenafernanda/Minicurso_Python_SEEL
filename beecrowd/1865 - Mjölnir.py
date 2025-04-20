# Leitura do número de casos de teste
C = int(input())

# Processa cada caso de teste
for _ in range(C):
    entrada = input().split()
    nome = entrada[0]  # Nome da pessoa
    N = int(entrada[1])  # Força aplicada

    # Apenas Thor consegue levantar o martelo
    if nome == "Thor":
        print("Y")
    else:
        print("N")
