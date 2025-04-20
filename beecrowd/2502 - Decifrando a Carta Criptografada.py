def decifrar_carta():
    import sys
    input = sys.stdin.read
    data = input().split("\n")

    i = 0
    resultado = []
    
    while i < len(data):
        if not data[i].strip():
            i += 1
            continue
        
        c, n = map(int, data[i].split())
        i += 1
        cifra1 = data[i]
        i += 1
        cifra2 = data[i]
        i += 1

        # Cria dicionários de mapeamento
        mapa = {}
        for a, b in zip(cifra1, cifra2):
            mapa[a] = b
            mapa[a.lower()] = b.lower()
            mapa[b] = a
            mapa[b.lower()] = a.lower()

        for _ in range(n):
            if i < len(data) and data[i].strip():
                linha = data[i]
                decifrada = ''.join(mapa.get(char, char) for char in linha)
                resultado.append(decifrada)
                i += 1
            else:
                break

        resultado.append("")  # Adiciona linha em branco entre casos de teste

    print("\n".join(resultado))

decifrar_carta()
