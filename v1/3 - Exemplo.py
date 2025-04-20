def verificar_maioridade(idade):
    if idade >= 18:
        return "Você é maior de idade."
    else:
        return "Você é menor de idade."

# Definindo variáveis
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

# Resultado
print(f"Olá, {nome}!")
print(verificar_maioridade(idade))

