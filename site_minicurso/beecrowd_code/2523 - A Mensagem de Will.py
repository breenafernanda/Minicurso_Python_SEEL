def mensagem_de_will():
    import sys
    input = sys.stdin.read
    data = input().strip().split("\n")
    
    i = 0
    while i < len(data):
        alfabeto = data[i].strip()  # Sequência do alfabeto
        i += 1
        if i >= len(data):  # Verifica se a entrada está incompleta
            break
        n = int(data[i].strip())  # Número de lâmpadas piscadas
        i += 1
        if i >= len(data):  # Verifica se a entrada está incompleta
            break
        indices = list(map(int, data[i].strip().split()))  # Índices das lâmpadas piscadas
        i += 1
        
        # Constrói a mensagem
        mensagem = "".join(alfabeto[idx - 1] for idx in indices)
        print(mensagem)

mensagem_de_will()
