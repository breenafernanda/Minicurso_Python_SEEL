count_par = 0
for _ in range(5):
    valor = int(input().strip())
    if valor % 2 == 0:
        count_par += 1

print(f"{count_par} valores pares")
