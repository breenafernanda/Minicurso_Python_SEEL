def door_logs():
    n = int(input())
    for _ in range(n):
        h, m, o = map(int, input().split())
        status = "A porta abriu!" if o == 1 else "A porta fechou!"
        print(f"{h:02}:{m:02} - {status}")

door_logs()
