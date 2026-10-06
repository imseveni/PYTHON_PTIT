T = int(input())
for _ in range(1, T + 1):
    s1 = input()
    s2 = input()

    n1 = len(s1)
    n2 = len(s2)

    if(n1 != n2):
        print(f"Test {_}: NO")
        continue

    x1 = "".join(sorted(s1))
    x2 = "".join(sorted(s2))

    if(x1 == x2):
        print(f"Test {_}: YES")
    else:
        print(f"Test {_}: NO")