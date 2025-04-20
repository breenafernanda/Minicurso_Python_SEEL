# Lê o código DDD
ddd = int(input().strip())

# Mapeamento de cada DDD para sua respectiva cidade
tabela = {
    61: "Brasilia",
    71: "Salvador",
    11: "Sao Paulo",
    21: "Rio de Janeiro",
    32: "Juiz de Fora",
    19: "Campinas",
    27: "Vitoria",
    31: "Belo Horizonte"
}

# Se existir na tabela, imprime a cidade; senão, imprime "DDD nao cadastrado"
print(tabela.get(ddd, "DDD nao cadastrado"))
