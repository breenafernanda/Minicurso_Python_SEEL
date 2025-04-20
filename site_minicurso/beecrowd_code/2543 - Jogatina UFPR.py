import sys

def principal():
    entrada = sys.stdin.read
    dados = entrada().strip().split("\n")
    
    indice = 0
    resultados = []
    
    while indice < len(dados):
        # Ler número de gameplays e identificador do usuário
        numero_gameplays, identificador_usuario = map(int, dados[indice].split())
        indice += 1

        contador_cs = 0
        
        for _ in range(numero_gameplays):
            identificador_autor, tipo_gameplay = map(int, dados[indice].split())
            indice += 1
            
            # Contar gameplays de Contra-Strike do usuário
            if identificador_autor == identificador_usuario and tipo_gameplay == 0:
                contador_cs += 1
        
        resultados.append(str(contador_cs))
    
    # Imprimir resultados
    print("\n".join(resultados))

if __name__ == "__main__":
    principal()
