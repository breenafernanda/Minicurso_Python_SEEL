# Lê o número de casos de teste
N = int(input())

# Itera sobre cada caso de teste
for _ in range(N):
    # Lê o valor de X
    X = int(input())
    
    # Inicializa a soma dos divisores
    soma_divisores = 0
    
    # Encontra os divisores próprios de X e calcula a soma
    for i in range(1, X // 2 + 1):
        if X % i == 0:
            soma_divisores += i
    
    # Verifica se a soma dos divisores é igual a X
    if soma_divisores == X:
        print(f"{X} eh perfeito")
    else:
        print(f"{X} nao eh perfeito")
