# Lê a quantidade de casos de teste
N = int(input().strip())

for _ in range(N):
    # Lê 3 valores de ponto flutuante com uma casa decimal
    v1, v2, v3 = map(float, input().split())
    
    # Calcula a média ponderada: pesos 2, 3 e 5
    media = (v1 * 2 + v2 * 3 + v3 * 5) / 10
    
    # Exibe o resultado
    print(f"{media:.1f}")
