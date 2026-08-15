def solve():
    T = int(input())

    for _ in range(T):
        N, X, M = map(float, input().split())

        count = 0
        while(N < M):
            N += N * X / 100
            count += 1

        print(count)


if __name__ == "__main__":
    solve()