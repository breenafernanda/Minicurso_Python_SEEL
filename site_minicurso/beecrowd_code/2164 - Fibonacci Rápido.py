import math

def fibonacci_rapido():
    n = int(input())  # Lê o valor de n
    phi = (1 + math.sqrt(5)) / 2  # Número áureo
    psi = (1 - math.sqrt(5)) / 2  # Complemento
    fib = (phi**n - psi**n) / math.sqrt(5)  # Fórmula de Binet
    print(f"{fib:.1f}")  # Saída com 1 casa decimal

fibonacci_rapido()
