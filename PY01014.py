def solve():
    a, K, N = map(int, input().split())

    max_b = N - a

    if(K > max_b):
        print(-1)
        return

    pos = K - (a % K)
    for i in range(pos, max_b + 1, K):
        print(i, end = " ")

if __name__ == "__main__":
    solve()