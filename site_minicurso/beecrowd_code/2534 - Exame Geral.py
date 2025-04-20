import sys

def main():
    input = sys.stdin.read
    data = input().strip().split("\n")
    
    idx = 0
    while idx < len(data):
        # Read number of inhabitants (N) and number of queries (Q)
        N, Q = map(int, data[idx].split())
        idx += 1

        # Read the scores
        scores = []
        for _ in range(N):
            scores.append(int(data[idx]))
            idx += 1

        # Sort scores in descending order
        scores.sort(reverse=True)

        # Process the queries
        results = []
        for _ in range(Q):
            position = int(data[idx])
            results.append(scores[position - 1])
            idx += 1

        # Print the results for the current case
        print("\n".join(map(str, results)))

if __name__ == "__main__":
    main()
