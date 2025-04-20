import sys

def principal():
    entrada = sys.stdin.read
    dados = entrada().strip().split("\n")
    
    indice = 0
    resultados = []
    
    while indice < len(dados):
        # Ler número de atributos
        numero_atributos = int(dados[indice])
        indice += 1

        # Ler número de cartas nos baralhos de Marcos e Leonardo
        numero_cartas_marcos, numero_cartas_leonardo = map(int, dados[indice].split())
        indice += 1

        # Ler baralho do Marcos
        baralho_marcos = []
        for _ in range(numero_cartas_marcos):
            baralho_marcos.append(list(map(int, dados[indice].split())))
            indice += 1

        # Ler baralho do Leonardo
        baralho_leonardo = []
        for _ in range(numero_cartas_leonardo):
            baralho_leonardo.append(list(map(int, dados[indice].split())))
            indice += 1

        # Ler cartas escolhidas e atributo sorteado
        carta_marcos, carta_leonardo = map(int, dados[indice].split())
        indice += 1
        atributo_sorteado = int(dados[indice])
        indice += 1

        # Obter os valores do atributo sorteado
        atributo_marcos = baralho_marcos[carta_marcos - 1][atributo_sorteado - 1]
        atributo_leonardo = baralho_leonardo[carta_leonardo - 1][atributo_sorteado - 1]

        # Determinar o resultado
        if atributo_marcos > atributo_leonardo:
            resultados.append("Marcos")
        elif atributo_leonardo > atributo_marcos:
            resultados.append("Leonardo")
        else:
            resultados.append("Empate")
    
    # Imprimir resultados
    print("\n".join(resultados))

if __name__ == "__main__":
    principal()
