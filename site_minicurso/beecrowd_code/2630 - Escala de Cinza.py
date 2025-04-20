def principal():
    import sys
    entrada = sys.stdin.read
    dados = entrada().strip().split("\n")
    
    T = int(dados[0])  # Número de casos de teste
    resultados = []
    
    for i in range(1, T + 1):
        conversao = dados[2 * i - 1]
        R, G, B = map(int, dados[2 * i].split())
        
        if conversao == "eye":
            P = int(0.30 * R + 0.59 * G + 0.11 * B)
        elif conversao == "mean":
            P = (R + G + B) // 3
        elif conversao == "max":
            P = max(R, G, B)
        elif conversao == "min":
            P = min(R, G, B)
        
        resultados.append(f"Caso #{i}: {P}")
    
    # Imprimir resultados
    print("\n".join(resultados))

if __name__ == "__main__":
    principal()
