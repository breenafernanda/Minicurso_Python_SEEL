def main():
    # Lê o número de alunos
    n = int(input())
    
    # Inicializa variáveis para rastrear o melhor aluno
    melhor_matricula = None
    melhor_nota = -1.0

    # Lê os dados de cada aluno
    for _ in range(n):
        matricula, nota = input().split()
        matricula = int(matricula)
        nota = float(nota)

        # Atualiza o melhor aluno, se necessário
        if nota > melhor_nota:
            melhor_matricula = matricula
            melhor_nota = nota

    # Verifica se a melhor nota atende o critério mínimo
    if melhor_nota >= 8.0:
        print(melhor_matricula)
    else:
        print("Minimum note not reached")

if __name__ == "__main__":
    main()
