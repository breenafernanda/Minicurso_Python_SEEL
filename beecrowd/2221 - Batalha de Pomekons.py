def batalha_de_pomekons():
    t = int(input())  # Número de instâncias
    for _ in range(t):
        b = int(input())  # Valor do bônus
        
        # Dados de Dabriel
        ad, dd, ld = map(int, input().split())
        golpe_dabriel = (ad + dd) / 2 + (b if ld % 2 == 0 else 0)
        
        # Dados de Guarte
        ag, dg, lg = map(int, input().split())
        golpe_guarte = (ag + dg) / 2 + (b if lg % 2 == 0 else 0)
        
        # Determina o vencedor
        if golpe_dabriel > golpe_guarte:
            print("Dabriel")
        elif golpe_guarte > golpe_dabriel:
            print("Guarte")
        else:
            print("Empate")

batalha_de_pomekons()
