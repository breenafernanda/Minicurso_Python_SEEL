import sys

def principal():
    entrada = sys.stdin.read
    dados = entrada().strip().split("\n")
    
    indice = 0
    resultados = []
    
    while indice < len(dados):
        # Ler o número de treinos
        N = int(dados[indice])
        indice += 1

        maior_velocidade = 0.0
        dias_recorde = []
        
        # Processar cada treino
        for dia in range(1, N + 1):
            duracao, distancia = map(int, dados[indice].split())
            indice += 1
            
            # Calcular a velocidade média
            velocidade_media = distancia / duracao
            
            # Verificar se o recorde foi batido
            if velocidade_media > maior_velocidade:
                maior_velocidade = velocidade_media
                dias_recorde.append(dia)
        
        resultados.extend(map(str, dias_recorde))
    
    # Imprimir resultados
    print("\n".join(resultados))

if __name__ == "__main__":
    principal()
