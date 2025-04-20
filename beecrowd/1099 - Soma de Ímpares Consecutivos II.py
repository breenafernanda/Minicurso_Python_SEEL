# Lê a quantidade de casos de teste
N = int(input())

# Loop para processar cada caso de teste
for _ in range(N):
    # Lê os dois valores X e Y
    X, Y = map(int, input().split())
    
    # Determina os limites inferior e superior
    inicio = min(X, Y) + 1
    fim = max(X, Y)
    
    # Calcula a soma dos números ímpares no intervalo
    soma_impares = sum(num for num in range(inicio, fim) if num % 2 != 0)
    
    # Imprime o resultado
    print(soma_impares)
