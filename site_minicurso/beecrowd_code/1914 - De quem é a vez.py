def resolver_par_ou_impar(teste):
    somatorio = teste['Jogador 1']['Numero'] + teste['Jogador 2']['Numero']

    if somatorio % 2 == 0: 
        if teste['Jogador 1']['Escolha'] == 'PAR':
            return teste['Jogador 1']['Nome']
        else:
            return teste['Jogador 2']['Nome']
    else:
        if teste['Jogador 1']['Escolha'] == 'IMPAR':
            return teste['Jogador 1']['Nome']
        else:
            return teste['Jogador 2']['Nome']

if __name__ == "__main__":
    try:
        qtd_testes = int(input().strip())
        for _ in range(qtd_testes):
            linha_1 = input().strip().split()
            linha_2 = input().strip().split()

            nome1, escolha1 = linha_1[0], linha_1[1]
            nome2, escolha2 = linha_1[2], linha_1[3]

            N, M = int(linha_2[0]), int(linha_2[1])

            teste = {
                'Jogador 1': {
                    'Nome': nome1,
                    'Escolha': escolha1,
                    'Numero': N
                },
                'Jogador 2': {
                    'Nome': nome2,
                    'Escolha': escolha2,
                    'Numero': M
                }
            }
            proximo = resolver_par_ou_impar(teste)
            print(proximo)
    except EOFError:
        pass
