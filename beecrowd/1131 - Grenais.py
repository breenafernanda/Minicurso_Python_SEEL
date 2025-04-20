# Inicializa contadores
grenais = 0
vitorias_inter = 0
vitorias_gremio = 0
empates = 0

while True:
    # Lê os gols marcados pelo Inter e Grêmio
    gols_inter, gols_gremio = map(int, input().split())
    
    # Atualiza estatísticas
    grenais += 1
    if gols_inter > gols_gremio:
        vitorias_inter += 1
    elif gols_inter < gols_gremio:
        vitorias_gremio += 1
    else:
        empates += 1
    
    # Pergunta se deseja realizar um novo GRENAL
    print("Novo grenal (1-sim 2-nao)")
    decisao = int(input())
    if decisao == 2:
        break

# Imprime estatísticas finais
print(f"{grenais} grenais")
print(f"Inter:{vitorias_inter}")
print(f"Gremio:{vitorias_gremio}")
print(f"Empates:{empates}")

# Determina o vencedor final
if vitorias_inter > vitorias_gremio:
    print("Inter venceu mais")
elif vitorias_gremio > vitorias_inter:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")
