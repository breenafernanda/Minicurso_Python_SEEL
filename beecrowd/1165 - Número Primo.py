# Função para verificar se um número é primo
def eh_primo(num):
    if num < 2:
        return False
    # Verifica divisibilidade até a raiz quadrada de num
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Lê o número de casos de teste
N = int(input())

# Itera sobre cada caso de teste
for _ in range(N):
    # Lê o valor de X
    X = int(input())
    
    # Verifica se X é primo e imprime o resultado
    if eh_primo(X):
        print(f"{X} eh primo")
    else:
        print(f"{X} nao eh primo")
