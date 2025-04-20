def principal():
    import sys
    entrada = sys.stdin.read
    dados = entrada().strip().split("\n")
    
    resultados = []
    for linha in dados:
        jogadas = linha.split()
        dodo, leo, pepper = jogadas
        
        # Verificar condições de vitória
        if dodo == leo == pepper:
            resultados.append("Putz vei, o Leo ta demorando muito pra jogar...")
        elif (dodo == "pedra" and leo == "tesoura" and pepper == "tesoura") or \
             (dodo == "papel" and leo == "pedra" and pepper == "pedra") or \
             (dodo == "tesoura" and leo == "papel" and pepper == "papel"):
            resultados.append("Os atributos dos monstros vao ser inteligencia, sabedoria...")
        elif (leo == "pedra" and dodo == "tesoura" and pepper == "tesoura") or \
             (leo == "papel" and dodo == "pedra" and pepper == "pedra") or \
             (leo == "tesoura" and dodo == "papel" and pepper == "papel"):
            resultados.append("Iron Maiden's gonna get you, no matter how far!")
        elif (pepper == "pedra" and dodo == "tesoura" and leo == "tesoura") or \
             (pepper == "papel" and dodo == "pedra" and leo == "pedra") or \
             (pepper == "tesoura" and dodo == "papel" and leo == "papel"):
            resultados.append("Urano perdeu algo muito precioso...")
        else:
            resultados.append("Putz vei, o Leo ta demorando muito pra jogar...")
    
    # Imprimir resultados
    print("\n".join(resultados))

if __name__ == "__main__":
    principal()
