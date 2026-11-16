n = input()

length = len(n)

if length % 3 == 1:
    n = '00' + n
elif length % 3 == 2:
    n = '0' + n

for i in range(0, length, 3):
    x = 0

    if n[i] == '1':
        x += 4
    if n[i + 1] == '1':
        x += 2
    if n[i + 2] == '1':
        x += 1

    print(x, end = "")