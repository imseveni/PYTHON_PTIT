import sys

n = int(input())

arr = list(map(int, sys.stdin.read().split()))

even = []
odd = []

for x in arr:
    if x % 2 == 1:
        odd.append(x)
    else:
        even.append(x)

even.sort()
odd.sort(reverse=True)

countEven = countOdd = 0

for x in arr:
    if x % 2 == 1:
        print(odd[countOdd], end = " ")
        countOdd += 1
    else:
        print(even[countEven], end = " ")
        countEven += 1


