def solve():
    t = int(input())
    
    for i in range(t):
        n = list(map(int, input()))

        for j in range(len(n) - 1, 0, -1):
            if n[j] >= 5:
                n[j - 1] += 1
            n[j] = 0

        print("".join(map(str, n)))

if __name__ == "__main__":
    solve()