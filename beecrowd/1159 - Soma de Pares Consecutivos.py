while True:
    # Lê o valor de X
    X = int(input())
    
    # Verifica se X é zero; se sim, encerra o loop
    if X == 0:
        break
    
    # Inicializa a soma dos pares consecutivos
    soma = 0
    
    # Ajusta X para o próximo par, se necessário
    if X % 2 != 0:
        X += 1
    
    # Soma os 5 pares consecutivos a partir de X
    for _ in range(5):
        soma += X
        X += 2
    
    # Imprime o resultado para o caso de teste atual
    print(soma)
