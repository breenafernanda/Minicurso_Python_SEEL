# Importação das bibliotecas
import sys

# O sys.stdin permite ler várias linhas até o EOF (fim de arquivo).
for linha in sys.stdin:
    # Removemos possíveis espaços no início/fim com strip()
    linha = linha.strip()
    
    # Verificamos se a linha está vazia (pode acontecer no final do arquivo).
    if not linha:
        continue
    
    # Separamos a linha em duas partes (a e b),
    # pois cada linha de entrada possui dois inteiros separados por espaço.
    a_str, b_str = linha.split()
    
    # Convertendo cada parte para inteiro sem sinal (no Python, int já suporta valores longos).
    a = int(a_str)
    b = int(b_str)

    # Chamamos a função que faz a soma "Mofiz" (XOR).
    resultado = a ^ b
    
    # Imprimimos o resultado.
    print(resultado)
