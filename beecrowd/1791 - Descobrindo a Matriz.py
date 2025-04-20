def descobrir_matriz(linha, coluna, valor, tamanho):
    matriz = [[0 for _ in range(tamanho)] for _ in range(tamanho)]
    matriz[linha - 1][coluna - 1] = valor

    for i in range(tamanho):
        for j in range(tamanho):
            matriz[i][j] = valor - abs(i - (linha - 1)) - abs(j - (coluna - 1))

    return matriz


def imprimir_matriz(matriz):
    for linha in matriz:
        print(" ".join(map(str, linha)))

def verificar_transformacao(matriz, n):
    try:
        # Exemplo de regra: todos os valores na matriz devem ser não negativos
        for i in range(n):
            for j in range(n):
                if matriz[i][j] < 0:
                    return "Nao Potencia"
        return "Potencia"
    except Exception as e: return e
try:
    # Captura da primeira entrada
    n = input().strip()
    try:
        n = int(n)  # Verifica se o tamanho da matriz é válido
        
    except ValueError:
        print(f"Erro: Tamanho inválido: '{n}'")
        exit()

    # Captura da segunda entrada
    entrada = input().strip()
    entradas = entrada.split()
    if len(entrada) == 1:
        n = int(entrada)
        # Captura da segunda entrada
        try:
            entrada = input().strip()
            entradas = entrada.split()
        except Exception as e: print(f'Falha ao capturar entradas {entradas}')
    # Se n < 3, assume-se que a entrada é válida com 2 valores de x, y e 1 valor de v
    if len(entradas) != 3:
        n = int(entradas[0])
        # Captura da segunda entrada
        entrada = input().strip()
        entradas = entrada.split()

    # Atribui os valores de x, y, v
    x, y = map(int, entradas[:2])
    v = int(entradas[2]) if n >= 3 else 1

    # Construção e exibição da matriz
    matriz_gerada = descobrir_matriz(x, y, v, n)
    saida = verificar_transformacao(matriz_gerada, n)
    print(saida)

except Exception as e:
    print(f"Erro inesperado: {e}")
