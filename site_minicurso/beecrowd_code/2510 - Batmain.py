def batmain():
    t = int(input())  # Número de casos de teste
    
    for _ in range(t):
        vilao = input().strip()  # Nome do vilão
        # Sempre imprime "Y" pois no contexto do problema, todos os vilões são capturados
        print("Y")

batmain()
