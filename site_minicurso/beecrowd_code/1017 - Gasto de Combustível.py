# Lê o tempo gasto na viagem (em horas) e a velocidade média (em km/h)
tempo = int(input())
velocidade = int(input())

# Distância percorrida (em km) = tempo (horas) * velocidade (km/h)
distancia = tempo * velocidade

# O automóvel faz 12 km/L, então litros usados = distância / 12
litros = distancia / 12

# Exibe o valor com 3 casas decimais
print(f"{litros:.3f}")
