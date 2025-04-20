"""sys.stdin ou sys.stdout
sys.stdin -> Permite ler entradas diretamente do fluxo padrão de entrada (como em um terminal)
sys.stdout -> Usado para imprimir no fluxo padrão de saída
"""
import sys 

# Criar Função para calcular atraso
def calcular_atraso(hora, minuto):
    # horário limite é 8:00
    """ 8 hrs * 60 minutos = 480 minutos """
    minutos_ao_acordar = hora*60 + minuto 
    # print(f"Bino acordou com {minutos_ao_acordar} minutos")
    """ Tempo máximo que Bino """
    minutos_chegada = minutos_ao_acordar + 60
    # print(f"Bino chegará na feira em até {minutos_chegada}")

    ## forma mais simples
    # atraso = minutos_chegada - 480
    # if atraso < 0: atraso = 0
    """max -> garante que o atraso nunca seja negativo:
            - Se minutos_chegada - 480 for menor que 0, o atraso será definido como 0.
            - Caso contrário, retorna o valor positivo de minutos_chegada - 480.
    """
    atraso = max(0, minutos_chegada - 480)

    return atraso

# Função para inicializar script
if __name__ == "__main__":
    for linha in sys.stdin:
        # ler hora e minuto 
        hora, minuto = map(int, linha.strip().split(":"))
        """strip -> remove espaços em branco no início e no final da string
           split -> divide a string em uma lista usando o caractere ":" como separador """
        atraso = calcular_atraso(hora, minuto)
        print(f'Atraso maximo: {atraso}')
