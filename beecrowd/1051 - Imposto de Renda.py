# Lê o valor do salário
salario = float(input().strip())

# Variável para acumular o imposto total
imposto = 0.0

# Se salário até 2000, é isento
if salario <= 2000:
    print("Isento")
else:
    # Calcula imposto sobre faixa 2000.01 até 3000 (8%)
    if salario > 2000:
        faixa = min(salario, 3000) - 2000
        imposto += faixa * 0.08
    
    # Calcula imposto sobre faixa 3000.01 até 4500 (18%)
    if salario > 3000:
        faixa = min(salario, 4500) - 3000
        imposto += faixa * 0.18
    
    # Calcula imposto sobre acima de 4500 (28%)
    if salario > 4500:
        faixa = salario - 4500
        imposto += faixa * 0.28
    
    print(f"R$ {imposto:.2f}")
