# Lê as informações da data e hora inicial
dia_inicio = int(input().split()[1])
h_inicio, m_inicio, s_inicio = map(int, input().replace(" ", "").split(":"))

# Lê as informações da data e hora final
dia_fim = int(input().split()[1])
h_fim, m_fim, s_fim = map(int, input().replace(" ", "").split(":"))

# Converte o instante inicial e final para segundos totais
inicio_segundos = (dia_inicio * 24 * 3600) + (h_inicio * 3600) + (m_inicio * 60) + s_inicio
fim_segundos = (dia_fim * 24 * 3600) + (h_fim * 3600) + (m_fim * 60) + s_fim

# Calcula a duração em segundos
duracao = fim_segundos - inicio_segundos

# Converte a duração de segundos em dias, horas, minutos e segundos
dias = duracao // (24 * 3600)
resto = duracao % (24 * 3600)
horas = resto // 3600
resto %= 3600
minutos = resto // 60
segundos = resto % 60

# Imprime o resultado no formato pedido
print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")
