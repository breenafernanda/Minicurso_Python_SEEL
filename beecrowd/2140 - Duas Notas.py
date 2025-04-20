def is_possible_change():
    notes = [2, 5, 10, 20, 50, 100]
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break
        change = m - n
        possible = False
        for i in range(len(notes)):
            for j in range(i, len(notes)):
                if notes[i] + notes[j] == change:
                    possible = True
                    break
            if possible:
                break
        print("possible" if possible else "impossible")

is_possible_change()
