def typing_time():
    c = int(input())
    for _ in range(c):
        word = input().strip()
        time = len(word) * 0.01
        print(f"{time:.2f}")

typing_time()
