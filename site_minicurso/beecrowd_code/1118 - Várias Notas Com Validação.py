while True:
    notas_validas = []
    
    # Continua solicitando notas até que duas válidas sejam inseridas
    while len(notas_validas) < 2:
        nota = float(input())
        if 0 <= nota <= 10:
            notas_validas.append(nota)
        else:
            print("nota invalida")
    
    # Calcula e imprime a média das notas válidas
    media = sum(notas_validas) / 2
    print(f"media = {media:.2f}")
    
    # Solicita a decisão para um novo cálculo
    while True:
        print("novo calculo (1-sim 2-nao)")
        decisao = int(input())
        if decisao == 1:
            break
        elif decisao == 2:
            exit()
