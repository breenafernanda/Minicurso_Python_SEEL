def tuitando():
    texto = input()  # Lê o texto
    print("TWEET" if len(texto) <= 140 else "MUTE")  # Verifica o limite de caracteres

tuitando()
