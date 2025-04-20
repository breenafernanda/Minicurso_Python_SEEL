import math

def tempestade_de_corvos():
    while True:
        try:
            # Lê os valores de entrada
            xf, yf, xi, yi, vi, r1, r2 = map(int, input().split())
            
            # Calcula a distância inicial entre Fiddlesticks e o invasor
            distancia_inicial = math.sqrt((xi - xf) ** 2 + (yi - yf) ** 2)
            
            # Calcula a distância máxima que o invasor pode alcançar em 1.5 segundos
            distancia_fuga = vi * 1.5
            
            # Verifica se a habilidade alcança o invasor
            if distancia_inicial + distancia_fuga <= r1 + r2:
                print('Y')  # É possível atingir o invasor
            else:
                print('N')  # Não é possível atingir o invasor
        except EOFError:
            break

tempestade_de_corvos()
