################################################################################################################
# Estrutura Básica do Python
################################################################################################################
"""Variáveis"""
# Variáveis são usadas para armazenar 
# dados que podemos reutilizar.
nome = "Mario"
idade = 23
print(f"Olá, meu nome é {nome} e eu tenho {idade} anos.")
################################################################################################################
"""Tipo de Dados"""
# Os principais tipos em Python 

numero = 10 # int
pi = 3.14 # float
texto = "Automação" # str
verdadeiro = True # bool
################################################################################################################

"""Controle de Fluxo"""

idade = 23 
if idade >= 18: 
    print("Você é maior de idade!")
else:
    print("Você é menor de idade!")

################################################################################################################

################################################################################################################
# Funções e Boas Práticas
################################################################################################################
""" Definição de funções"""
#Funções são blocos de código reutilizáveis que nos ajudam a organizar nossos programas.
def saudacao(nome):
        texto = (
             f"Olá, {nome}! "
             f"Bem-vindo ao minicurso."
        )
        return texto

nome = "Bob"
texto_de_saudacao = saudacao(nome)
print(texto)

################################################################################################################
"""Boas práticas"""
# - Use nomes de variáveis e funções claros e descritivos.
# - Comente seu código onde necessário.
# - Organize seu código em funções para torná-lo mais legível.
################################################################################################################

"""Execução de um pequeno script simples"""
# Vamos juntar tudo em um exemplo prático.
# Esse script utiliza entrada de dados, controle de fluxo e funções. Agora que dominamos o básico, podemos avançar para aplicações práticas!
### Exemplo:
# Função para verificar maioridade
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

