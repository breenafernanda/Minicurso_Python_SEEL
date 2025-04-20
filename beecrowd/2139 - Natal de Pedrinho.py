def main():
    import sys

    # Mapeia os dias acumulados até o início de cada mês
    dias_no_mes = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 25]
    dias_acumulados = [sum(dias_no_mes[:i]) for i in range(len(dias_no_mes))]

    natal_dia_do_ano = sum(dias_no_mes)

    for linha in sys.stdin:
        mes, dia = map(int, linha.strip().split())
        dia_do_ano = sum(dias_no_mes[:mes - 1]) + dia

        if dia_do_ano == natal_dia_do_ano:
            print("E natal!")
        elif dia_do_ano == natal_dia_do_ano - 1:
            print("E vespera de natal!")
        elif dia_do_ano > natal_dia_do_ano:
            print("Ja passou!")
        else:
            faltam = natal_dia_do_ano - dia_do_ano
            print(f"Faltam {faltam} dias para o natal!")

if __name__ == "__main__":
    main()
