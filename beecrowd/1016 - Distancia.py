# Lê o valor da distância em km
distancia = int(input().strip())

# A diferença de velocidade entre o carro Y (90 km/h) e o carro X (60 km/h) é 30 km/h.
# Em 1 hora (60 minutos), Y se afasta 30 km a mais que X.
# Isso equivale a 1 km a cada 2 minutos.
# Logo, para se distanciar 'distancia' km, são necessários 'distancia * 2' minutos.

tempo = distancia * 2

# Imprime o resultado no formato exigido
print(f"{tempo} minutos")