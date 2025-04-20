# Lê o número que representa o mês
mes = int(input().strip())

# Lista dos meses em inglês, indexada a partir de 0 (por isso o -1 ao acessar)
nomes = ["January", "February", "March", "April", "May", "June",
         "July", "August", "September", "October", "November", "December"]

# Imprime o nome correspondente
print(nomes[mes - 1])
