def principal():
    import sys
    entrada = sys.stdin.read
    dados = entrada().strip().split("\n")
    
    N = int(dados[0])  # Número de casos de teste
    respostas = ["I am Toorg!"] * N  # Resposta para cada pergunta
    
    # Imprimir respostas
    print("\n".join(respostas))

if __name__ == "__main__":
    principal()
