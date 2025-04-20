# Função para calcular o n-ésimo termo da sequência de Fibonacci
def fibonacci(n):
    # Inicializa os dois primeiros termos da sequência
    a, b = 0, 1
    # Calcula os termos até o n-ésimo
    for _ in range(n):
        a, b = b, a + b
    return a

# Lê o número de casos de teste
T = int(input())

# Itera sobre cada caso de teste
for _ in range(T):
    # Lê o valor de N
    N = int(input())
    # Calcula o N-ésimo termo da sequência de Fibonacci
    result = fibonacci(N)
    # Exibe o resultado no formato solicitado
    print(f"Fib({N}) = {result}")
