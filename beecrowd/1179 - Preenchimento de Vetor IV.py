# Inicializa os vetores para pares e ímpares
par = []
impar = []

# Lê os 15 valores inteiros
for _ in range(15):
    valor = int(input())
    
    # Verifica se o valor é par ou ímpar e adiciona ao vetor correspondente
    if valor % 2 == 0:
        par.append(valor)
        # Se o vetor par atingir 5 elementos, imprime e reinicia
        if len(par) == 5:
            for i in range(5):
                print(f"par[{i}] = {par[i]}")
            par.clear()
    else:
        impar.append(valor)
        # Se o vetor ímpar atingir 5 elementos, imprime e reinicia
        if len(impar) == 5:
            for i in range(5):
                print(f"impar[{i}] = {impar[i]}")
            impar.clear()

# Imprime os valores restantes no vetor ímpar
for i in range(len(impar)):
    print(f"impar[{i}] = {impar[i]}")

# Imprime os valores restantes no vetor par
for i in range(len(par)):
    print(f"par[{i}] = {par[i]}")
