# Lê 100 valores e armazena no vetor A
A = [float(input()) for _ in range(100)]

# Itera sobre o vetor e imprime os valores menores ou iguais a 10
for i in range(100):
    if A[i] <= 10:
        print(f"A[{i}] = {A[i]:.1f}")
