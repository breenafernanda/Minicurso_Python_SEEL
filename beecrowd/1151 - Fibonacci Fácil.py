entrada = int(input())
contador = 0
tmp1 = 0
tmp2 = 1
while contador < entrada:
    if contador == 0:
        print(tmp1, end=' ')
        
    elif contador == 1:
        print(tmp2, end=' ')
    elif contador+1 == entrada:
        print(f'{tmp1+tmp2}')

    else:
        print(f'{tmp1+tmp2}', end=' ')
        tmp = tmp1 + tmp2
        tmp1 = tmp2
        tmp2 = tmp
    contador += 1

        

