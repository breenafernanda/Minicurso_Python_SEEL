# Inicializa uma lista para armazenar os 20 números inteiros
N = []

# Lê 20 números inteiros do usuário e armazena na lista
for i in range(20):
    valor = int(input())
    N.append(valor)

# Troca os elementos: o primeiro com o último, o segundo com o penúltimo, e assim por diante
for i in range(10):
    # Realiza a troca utilizando uma variável temporária
    temp = N[i]
    N[i] = N[19 - i]
    N[19 - i] = temp

# Exibe o vetor modificado
for i in range(20):
    print(f"N[{i}] = {N[i]}")
