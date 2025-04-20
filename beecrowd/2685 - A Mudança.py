def principal():
    import sys
    entrada = sys.stdin.read
    dados = entrada().strip().split("\n")
    
    resultados = []
    for linha in dados:
        M = int(linha)
        if 0 <= M < 90 or M == 360:
            resultados.append("Bom Dia!!")
        elif 90 <= M < 180:
            resultados.append("Boa Tarde!!")
        elif 180 <= M < 270:
            resultados.append("Boa Noite!!")
        elif 270 <= M < 360:
            resultados.append("De Madrugada!!")
    
    # Imprimir os resultados
    print("\n".join(resultados))

if __name__ == "__main__":
    principal()
