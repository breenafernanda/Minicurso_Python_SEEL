import sys
import math

def principal():
    entrada = sys.stdin.read
    dados = entrada().strip().split("\n")
    
    resultados = []
    
    for linha in dados:
        # Converter número de ninjas para inteiro
        numero_ninjas = int(linha)
        
        # Calcular o número de vezes que a técnica foi utilizada
        vezes_utilizada = int(math.log2(numero_ninjas))
        resultados.append(str(vezes_utilizada))
    
    # Imprimir resultados
    print("\n".join(resultados))

if __name__ == "__main__":
    principal()
