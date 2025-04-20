# Inicializa o contador de soma e lista de resultados
soma = 0
resultados = []

# Converte piscadas para valores binários
def piscada_para_valor(piscada):
    return int(piscada.replace('*', '1').replace('-', '0'), 2)

try:
    while True:
        entrada = input().strip()

        if entrada == "caw caw":  # Grito do corvo
            resultados.append(soma)
            soma = 0
            if len(resultados) == 3:  # Três resultados calculados
                break
        else:  # Piscada
            soma += piscada_para_valor(entrada)

# Exibe os resultados
except EOFError:
    pass

for resultado in resultados:
    print(resultado)
