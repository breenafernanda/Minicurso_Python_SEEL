while True:
    # Lê a senha fornecida pelo usuário
    senha = int(input())
    
    # Verifica se a senha está correta
    if senha == 2002:
        print("Acesso Permitido")
        break  # Encerra o loop se a senha estiver correta
    else:
        print("Senha Invalida")  # Informa que a senha está incorreta
