count_par = 0
count_impar = 0
count_pos = 0
count_neg = 0

for _ in range(5):
    valor = int(input().strip())
    
    # Par ou ímpar
    if valor % 2 == 0:
        count_par += 1
    else:
        count_impar += 1
    
    # Positivo ou negativo (não conte 0 como positivo ou negativo)
    if valor > 0:
        count_pos += 1
    elif valor < 0:
        count_neg += 1

print(f"{count_par} valor(es) par(es)")
print(f"{count_impar} valor(es) impar(es)")
print(f"{count_pos} valor(es) positivo(s)")
print(f"{count_neg} valor(es) negativo(s)")
