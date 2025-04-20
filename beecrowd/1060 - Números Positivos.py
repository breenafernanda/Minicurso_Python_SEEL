count_pos = 0
for _ in range(6):
    valor = float(input().strip())
    if valor > 0:
        count_pos += 1

print(f"{count_pos} valores positivos")
