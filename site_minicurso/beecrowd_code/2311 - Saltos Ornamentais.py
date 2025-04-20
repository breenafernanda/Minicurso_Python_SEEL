def saltos_ornamentais():
    n = int(input())  # Número de competidores
    for _ in range(n):
        nome = input().strip()  # Nome do competidor
        grau_dificuldade = float(input())  # Grau de dificuldade
        notas = list(map(float, input().split()))  # Notas dos juízes

        # Remove a maior e a menor nota
        notas.remove(max(notas))
        notas.remove(min(notas))

        # Calcula o resultado
        resultado = sum(notas) * grau_dificuldade

        # Exibe o resultado do competidor
        print(f"{nome} {resultado:.2f}")

saltos_ornamentais()
