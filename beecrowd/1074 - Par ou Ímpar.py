# Lê a quantidade de valores
N = int(input().strip())

for _ in range(N):
    X = int(input().strip())
    
    # Se for zero, imprime apenas NULL
    if X == 0:
        print("NULL")
    else:
        # Define se é par ou ímpar
        if X % 2 == 0:
            texto_paridade = "EVEN"
        else:
            texto_paridade = "ODD"
        
        # Define se é positivo ou negativo
        if X > 0:
            texto_sinal = "POSITIVE"
        else:
            texto_sinal = "NEGATIVE"
        
        # Imprime o resultado
        print(f"{texto_paridade} {texto_sinal}")
