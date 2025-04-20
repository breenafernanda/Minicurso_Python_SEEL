def jogo_do_operador():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    i = 0
    resultados = []
    
    while i < len(data):
        t = int(data[i])  # Número de expressões e jogadores
        i += 1
        
        expressoes = []
        for _ in range(t):
            expressoes.append(data[i].strip())
            i += 1
        
        jogadores = []
        for _ in range(t):
            jogadores.append(data[i].strip())
            i += 1
        
        erraram = []
        for jogador in jogadores:
            nome, e, resposta = jogador.split()
            e = int(e) - 1  # Ajusta o índice para zero-indexado
            x, resto = expressoes[e].split()
            y, z = resto.split('=')
            x, y, z = int(x), int(y), int(z)
            
            # Verifica a resposta do jogador
            if resposta == '+':
                if x + y != z:
                    erraram.append(nome)
            elif resposta == '-':
                if x - y != z:
                    erraram.append(nome)
            elif resposta == '*':
                if x * y != z:
                    erraram.append(nome)
            elif resposta == 'I':
                if x + y == z or x - y == z or x * y == z:
                    erraram.append(nome)
        
        if len(erraram) == 0:
            resultados.append("You Shall All Pass!")
        elif len(erraram) == t:
            resultados.append("None Shall Pass!")
        else:
            resultados.append(" ".join(sorted(erraram)))
    
    print("\n".join(resultados))

jogo_do_operador()
