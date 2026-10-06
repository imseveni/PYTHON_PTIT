T = int(input())
for _ in range(T):
    s = list(input())
    n = len(s)
    half = n // 2

    left = s[:half]
    right = s[half:n]

    totalLeft = sum(ord(x) for x in left) % 26
    totalRight = sum(ord(x) for x in right) % 26

    for i in range(half):
        left[i] = chr((ord(left[i]) - ord('A') + totalLeft) % 26 + ord('A'))

    for i in range(half):
        right[i] = chr((ord(right[i]) - ord('A') + totalRight) % 26 + ord('A'))

    for i in range(half):
        left[i] = chr((ord(left[i]) - ord('A') + ord(right[i]) - ord('A')) % 26 + ord('A'))

    print("".join(left))
