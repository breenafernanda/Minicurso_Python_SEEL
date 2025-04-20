def vitamina_c():
    tabela_vitamina_c = {
        "suco de laranja": 120,
        "morango fresco": 85,
        "mamao": 85,
        "goiaba vermelha": 70,
        "manga": 56,
        "laranja": 50,
        "brocolis": 34
    }
    
    while True:
        t = int(input())  # Lê o número de alimentos consumidos
        if t == 0:  # Condição de parada
            break
        
        consumo_total = 0
        for _ in range(t):
            n, alimento = input().split(maxsplit=1)
            consumo_total += int(n) * tabela_vitamina_c[alimento]
        
        if consumo_total < 110:
            print(f"Mais {110 - consumo_total} mg")
        elif consumo_total > 130:
            print(f"Menos {consumo_total - 130} mg")
        else:
            print(f"{consumo_total} mg")

vitamina_c()
