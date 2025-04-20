def principal():
    import sys
    entrada = sys.stdin.read
    dados = entrada().strip().split("\n")
    
    # Quantidade de refeições disponíveis
    Ca, Ba, Pa = map(int, dados[0].split())
    # Quantidade de refeições requisitadas
    Cr, Br, Pr = map(int, dados[1].split())
    
    # Calcular a diferença entre o requisitado e o disponível, considerando apenas os que faltam
    falta_frango = max(0, Cr - Ca)
    falta_bife = max(0, Br - Ba)
    falta_massa = max(0, Pr - Pa)
    
    # Soma total de refeições que faltam
    resultado = falta_frango + falta_bife + falta_massa
    
    # Imprimir o resultado
    print(resultado)

if __name__ == "__main__":
    principal()
