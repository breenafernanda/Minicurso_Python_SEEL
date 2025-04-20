# Dicionário que define os vencedores
regras = {
    "tesoura": ["papel", "lagarto"],
    "papel": ["pedra", "Spock"],
    "pedra": ["lagarto", "tesoura"],
    "lagarto": ["Spock", "papel"],
    "Spock": ["tesoura", "pedra"]
}

# Lê o número de casos de teste
T = int(input().strip())

for t in range(1, T + 1):
    # Lê as escolhas de Sheldon e Raj
    sheldon, raj = input().strip().split()
    
    # Determina o resultado
    if sheldon == raj:
        resultado = "De novo!"
    elif raj in regras[sheldon]:
        resultado = "Bazinga!"
    else:
        resultado = "Raj trapaceou!"
    
    # Imprime o resultado do caso
    print(f"Caso #{t}: {resultado}")
