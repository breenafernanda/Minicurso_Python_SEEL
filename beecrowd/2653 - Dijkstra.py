def principal():
    import sys
    entrada = sys.stdin.read
    dados = entrada().strip().split("\n")
    
    # Usar um conjunto para armazenar jóias únicas
    joias = set(dados)
    
    # Imprimir o número de jóias distintas
    print(len(joias))

if __name__ == "__main__":
    principal()
