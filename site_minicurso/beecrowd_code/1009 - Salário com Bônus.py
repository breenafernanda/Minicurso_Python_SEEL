nome = input()
salario_fixo = float(input())
vendas = float(input())

salario = salario_fixo + 0.15*vendas

print(f"TOTAL = R$ {salario:.2f}")