def paridade():
    mensagem = input().strip()  # Lê a mensagem S
    bit_1_count = mensagem.count('1')  # Conta o número de bits '1'
    bit_paridade = '0' if bit_1_count % 2 == 0 else '1'  # Determina o bit de paridade
    print(mensagem + bit_paridade)  # Adiciona o bit de paridade à mensagem e exibe

paridade()
