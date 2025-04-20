def estatisticas_voleibol():
    n = int(input())  # Número de jogadores
    total_saque, total_bloqueio, total_ataque = 0, 0, 0
    sucesso_saque, sucesso_bloqueio, sucesso_ataque = 0, 0, 0

    for _ in range(n):
        input()  # Nome do jogador (não utilizado)
        s, b, a = map(int, input().split())  # Tentativas de saque, bloqueio e ataque
        s1, b1, a1 = map(int, input().split())  # Sucessos de saque, bloqueio e ataque

        # Soma os totais e sucessos
        total_saque += s
        total_bloqueio += b
        total_ataque += a
        sucesso_saque += s1
        sucesso_bloqueio += b1
        sucesso_ataque += a1

    # Calcula os percentuais de sucesso
    perc_saque = (sucesso_saque / total_saque * 100) if total_saque > 0 else 0
    perc_bloqueio = (sucesso_bloqueio / total_bloqueio * 100) if total_bloqueio > 0 else 0
    perc_ataque = (sucesso_ataque / total_ataque * 100) if total_ataque > 0 else 0

    # Exibe os resultados
    print(f"Pontos de Saque: {perc_saque:.2f} %.")
    print(f"Pontos de Bloqueio: {perc_bloqueio:.2f} %.")
    print(f"Pontos de Ataque: {perc_ataque:.2f} %.")

estatisticas_voleibol()
