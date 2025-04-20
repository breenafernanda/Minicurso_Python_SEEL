def principal():
    import sys
    entrada = sys.stdin.read
    dados = entrada().strip().split("\n")
    
    C = int(dados[0])  # Número de casos de teste
    musicas = [
        "PROXYCITY", "P.Y.N.G.", "DNSUEY!", "SERVERS", "HOST!",
        "CRIPTONIZE", "OFFLINE DAY", "SALT", "ANSWER!", "RAR?", "WIFI ANTENNAS"
    ]
    
    resultados = []
    for i in range(1, C + 1):
        X, Y = map(int, dados[i].split())
        resultados.append(musicas[X + Y])
    
    # Imprimir apenas as respostas do problema atual
    print("\n".join(resultados))

if __name__ == "__main__":
    principal()
