# Leitura das temperaturas dos 3 dias
try:
    while True:
        A, B, C = map(int, input().split())

        # Condições para determinar o humor do povo de Westeros
        if A > B and B <= C:
            print(":)")  # Desceu do 1º para o 2º e subiu ou permaneceu constante do 2º para o 3º
        elif A < B and B >= C:
            print(":(")  # Subiu do 1º para o 2º e desceu ou permaneceu constante do 2º para o 3º
        elif A < B and B < C:
            if (C - B) >= (B - A):
                print(":)")  # Subiu do 1º para o 2º e do 2º para o 3º com maior ou igual intensidade
            else:
                print(":(")  # Subiu do 1º para o 2º e do 2º para o 3º com menor intensidade
        elif A > B and B > C:
            if (B - C) < (A - B):
                print(":)")  # Desceu do 1º para o 2º e do 2º para o 3º com menor intensidade
            else:
                print(":(")  # Desceu do 1º para o 2º e do 2º para o 3º com maior ou igual intensidade
        elif A == B:
            if B < C:
                print(":)")  # Temperatura constante do 1º para o 2º e subiu do 2º para o 3º
            else:
                print(":(")  # Temperatura constante do 1º para o 2º e desceu ou permaneceu constante do 2º para o 3º
except EOFError:
    pass
