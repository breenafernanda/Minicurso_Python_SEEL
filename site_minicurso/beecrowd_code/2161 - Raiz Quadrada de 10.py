def sqrt_of_10():
    n = int(input())
    result = 0
    for _ in range(n):
        result = 1 / (6 + result)
    result += 3
    print(f"{result:.10f}")

sqrt_of_10()
