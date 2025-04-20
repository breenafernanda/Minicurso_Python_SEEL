def tipo_triangulo():
    a, b, c = map(int, input().split())  # Lê os três lados do triângulo

    # Verifica se os lados formam um triângulo válido
    if a + b > c and a + c > b and b + c > a:
        # Determina o tipo do triângulo
        if a == b == c:
            print("Valido-Equilatero")
        elif a == b or b == c or a == c:
            print("Valido-Isoceles")
        else:
            print("Valido-Escaleno")

        # Verifica se o triângulo é retângulo
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            print("Retangulo: S")
        else:
            print("Retangulo: N")
    else:
        print("Invalido")

tipo_triangulo()
