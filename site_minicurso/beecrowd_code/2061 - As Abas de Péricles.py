# Lendo os números iniciais de abas e ações de Péricles
N, M = map(int, input().split())

# Loop para processar cada ação de Péricles
for _ in range(M):
    acao = input().strip()

    # Atualizando o número de abas com base na ação
    if acao == "fechou":
        N += 1  # Fechar uma aba, adiciona uma nova
    elif acao == "clicou":
        N -= 1  # Clicar em uma propaganda, fecha uma aba

# Imprimindo o número final de abas
print(N)
