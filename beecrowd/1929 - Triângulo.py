def pode_formar_triangulo(lados):
    # Verifica se qualquer combinação de 3 lados forma um triângulo
    for i in range(4):
        for j in range(i + 1, 4):
            for k in range(j + 1, 4):
                a, b, c = lados[i], lados[j], lados[k]
                if a + b > c and a + c > b and b + c > a:
                    return True
    return False

if __name__ == "__main__":
    # Lê a entrada e transforma em uma lista de inteiros
    lados = list(map(int, input().split()))
    
    # Verifica se é possível formar um triângulo
    if pode_formar_triangulo(lados):
        print("S")
    else:
        print("N")
