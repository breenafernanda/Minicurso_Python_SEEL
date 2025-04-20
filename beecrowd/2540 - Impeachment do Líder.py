import sys

def main():
    input = sys.stdin.read
    data = input().strip().split("\n")
    
    idx = 0
    results = []
    
    while idx < len(data):
        N = int(data[idx])
        idx += 1
        votes = list(map(int, data[idx].split()))
        idx += 1
        
        # Count votes in favor of impeachment
        favorable_votes = sum(votes)
        
        # Check if favorable votes are at least 2/3 of the total
        if favorable_votes >= (2 * N) / 3:
            results.append("impeachment")
        else:
            results.append("acusacao arquivada")
    
    # Print results
    print("\n".join(results))

if __name__ == "__main__":
    main()
