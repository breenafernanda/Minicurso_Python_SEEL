# Lê as quatro notas com uma casa decimal
N1, N2, N3, N4 = map(float, input().split())

# Calcula a média ponderada das quatro notas
# Pesos: N1 (2), N2 (3), N3 (4), N4 (1)
media = (N1 * 2 + N2 * 3 + N3 * 4 + N4 * 1) / 10

print(f"Media: {media:.1f}")

# Verifica a condição de aprovação
if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    # Caso a média esteja entre 5.0 e 6.9 (inclusive), vai para exame
    print("Aluno em exame.")
    exame = float(input().strip())
    print(f"Nota do exame: {exame:.1f}")
    
    media_final = (media + exame) / 2
    
    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    
    print(f"Media final: {media_final:.1f}")
