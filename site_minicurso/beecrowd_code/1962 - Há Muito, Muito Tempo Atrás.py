if __name__ == "__main__":
    # Lê o número de casos de teste
    N = int(input())
    
    # Processa cada caso de teste
    resultados = []
    for _ in range(N):
        T = int(input())
        ano = 2015 - T
        if ano > 0:
            resultados.append(f"{ano} D.C.")
        else:
            resultados.append(f"{abs(ano) + 1} A.C.")
    
    # Imprime todos os resultados
    print("\n".join(resultados))
