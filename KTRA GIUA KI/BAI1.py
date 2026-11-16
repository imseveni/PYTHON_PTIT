def calc(n, b):
    if n == 0:
        return

    r = n % b
    calc(n // b, b)

    if r < 10: 
        print(r, end = "")
    else:
        print(chr(ord('A') + (r - 10)), end = "")


for _ in range(int(input())):
    n, b = map(int, input().split())
    calc(n, b)
    print()
