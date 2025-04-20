# Lê os 4 valores inteiros de uma só vez
A, B, C, D = map(int, input().split())

# Testa cada condição, conforme enunciado:
# 1) B > C
# 2) D > A
# 3) (C + D) > (A + B)
# 4) C e D são positivos (C > 0, D > 0)
# 5) A é par (A % 2 == 0)

if (B > C and
    D > A and
    (C + D) > (A + B) and
    C > 0 and
    D > 0 and
    A % 2 == 0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
