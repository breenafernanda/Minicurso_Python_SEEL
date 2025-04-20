# Inicializa I com 0
I = 0.0

# Enquanto I <= 2, com incrementos de 0.2
while I <= 2.0:
    # Gera os valores de J adicionando 1, 2 e 3
    for J in range(1, 4):
        valor_J = I + J  # Calcula o valor atual de J
        
        # Formata I para evitar valores com múltiplas casas decimais desnecessárias
        if I == int(I):
            I_str = f"{int(I)}"
        else:
            I_str = f"{I:.1f}"
        
        # Formata J para evitar valores com múltiplas casas decimais desnecessárias
        if valor_J == int(valor_J):
            J_str = f"{int(valor_J)}"
        else:
            J_str = f"{valor_J:.1f}"
        
        # Imprime no formato correto
        print(f"I={I_str} J={J_str}")
    
    # Incrementa I em 0.2
    I = round(I + 0.2, 1)  # Arredonda para evitar imprecisões
