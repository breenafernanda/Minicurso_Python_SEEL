# from colorama import Fore, Style
import sys

# def imprimir(texto, valor):
#     print(f'{Fore.LIGHTBLUE_EX}{texto}: {Fore.YELLOW}{valor}{Style.RESET_ALL}')
#     # Exemplo de uso
#     # imprimir(texto="Altura", valor="2.96")

""" calculos: área e altura
A área da base do cilindro é calculada com  A = pi*R²  //  R = D/2
A altura do cilindro é calculada com h = Voluma/Área
"""
def calcular_A_h(V, D):
    # Calcular Area [A]
    R = D/2
    A = 3.14 * R**2
    # imprimir("Raio", R)
    # imprimir("Área", A)

    # Calcular Altura [h]
    h = V/A 
    # imprimir("Altura", h)
    return A, h

# Inicializar Script
if __name__ == "__main__":
    while True:
        try:
            V = float(input())
        except: break
        D = float(input())
        # imprimir("Volume", V)
        # imprimir("Diametro", D)
        A, h = calcular_A_h(V, D)
        print(f'ALTURA = {h:.2f}')
        print(f'AREA = {A:.2f}')