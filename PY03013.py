def count_up_to(n):
    if n <= 0:
        return [0] * 10

    counts = [0] * 10
    factor = 1

    while factor <= n:
        lower = n - (n // factor) * factor
        curr = (n // factor) % 10
        higher = n // (factor * 10)

        for d in range(10):
            counts[d] += higher * factor

        for d in range(curr):
            counts[d] += factor

        counts[curr] += lower + 1

        counts[0] -= factor
        factor *= 10

    return counts

for _ in range(int(input())):
    A, B = map(int, input().split())

    cA = count_up_to(A - 1)
    cB = count_up_to(B)

    for d in range(10):
        print(cB[d] - cA[d], end = ' ')

    print()
    