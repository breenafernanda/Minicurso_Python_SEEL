entrada = input().split()
x = int(entrada[0])
y = int(entrada[1])


tmp = 0
for i in range(1,y+1):
    tmp += 1
    if tmp == x:
        print(i,end='\n')
        tmp = 0
    else:
        print(i,end=' ')
        