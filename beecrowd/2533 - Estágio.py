def calcular_ira():
    import sys
    input = sys.stdin.read
    data = input().strip().split("\n")
    
    i = 0
    while i < len(data):
        m = int(data[i])  # Número de disciplinas
        i += 1
        soma_notas_pesos = 0
        soma_pesos = 0
        
        for _ in range(m):
            nota, carga = map(int, data[i].split())
            soma_notas_pesos += nota * carga
            soma_pesos += carga
            i += 1
        
        # Certifique-se de que soma_pesos é diferente de zero para evitar divisão por zero
        ira = soma_notas_pesos / soma_pesos if soma_pesos > 0 else 0
        print(f"{ira / 100:.4f}")  # Normaliza o resultado dividindo por 100

calcular_ira()
