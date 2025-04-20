# Lê o valor inteiro (tempo em dias)
N = int(input().strip())

# Calcula anos, meses e dias
anos = N // 365          
resto = N % 365
meses = resto // 30      
dias = resto % 30

print(f"{anos} ano(s)\n{meses} mes(es)\n{dias} dia(s)")
