if __name__ == "__main__":
    # Lê os valores antigos e novos do ingresso
    A, B = map(float, input().split())
    
    # Calcula o aumento percentual
    aumento = ((B - A) / A) * 100
    
    # Imprime o resultado formatado com duas casas decimais e o símbolo de porcentagem
    print(f"{aumento:.2f}%")
