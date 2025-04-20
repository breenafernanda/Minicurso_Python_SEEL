# Lê o valor inteiro (tempo em segundos)
N = int(input().strip())

# Calcula horas, minutos e segundos
horas = N // 3600          # cada hora tem 3600 segundos
resto = N % 3600
minutos = resto // 60      # cada minuto tem 60 segundos
segundos = resto % 60

# Imprime no formato horas:minutos:segundos
print(f"{horas}:{minutos}:{segundos}")
