def calc(n, source, target, auxiliary):
    if n == 1:
        print(f"{source} -> {target}")
        return

    calc(n - 1, source, auxiliary, target)

    print(f"{source} -> {target}")

    calc(n - 1, auxiliary, target, source)

n = int(input())
calc(n, 'A', 'C', 'B')

