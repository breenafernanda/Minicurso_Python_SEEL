C = int(input())
for i in range(0, C):
    n = int(input())
    resultado = 0
    for i in range(1,n+1):
        if i%2==0: 
            resultado -= 1
        else:
            resultado += 1
    print(resultado)

