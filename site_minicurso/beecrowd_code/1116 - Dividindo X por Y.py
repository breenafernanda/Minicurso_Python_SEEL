# Lê o número de casos de teste
N = int(input())

# Processa cada caso de teste
for _ in range(N):
    # Lê os valores de X e Y
    X, Y = map(int, input().split())
    
    # Verifica se a divisão é possível
    if Y == 0:
        print("divisao impossivel")
    else:
        # Calcula o resultado da divisão
        resultado = X / Y
        # Imprime o resultado com uma casa decimal
        print(f"{resultado:.1f}")
