import sys

def principal():
    entrada = sys.stdin.read
    dados = entrada().strip().split("\n")
    
    indice = 0
    resultados = []
    
    while indice < len(dados):
        # Ler número de visitantes, altura mínima e altura máxima
        N, altura_minima, altura_maxima = map(int, dados[indice].split())
        indice += 1

        contador_aptos = 0
        
        # Contar visitantes aptos
        for _ in range(N):
            altura_visitante = int(dados[indice])
            indice += 1
            if altura_minima <= altura_visitante <= altura_maxima:
                contador_aptos += 1
        
        resultados.append(str(contador_aptos))
    
    # Imprimir resultados
    print("\n".join(resultados))

if __name__ == "__main__":
    principal()
