def calc(n, b):
    if n == 0:
        return

    calc(n // b, b)
    
    r = n % b
    if r < 10:
        print(r, end = "")
    else:
        print(chr(r - 10 + ord('A')), end = "")


T = int(input())
for _ in range(T):
    n, b = map(int, input().split())

    calc(n, b)
    print()
