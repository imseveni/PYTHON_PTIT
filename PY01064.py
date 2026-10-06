f = [0] * 26
f[1] = 1
for i in range(2, 26):
    f[i] = f[i - 1] * 2

def calc(n, k):
    # print(n, k)
    if(n == 1):
        return 'A'
    
    if(k == f[n]):
        return chr(ord('A') + n - 1)

    elif(k < f[n]):
        return calc(n - 1, k)
    else:
        return calc(n - 1, k - f[n])


T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    print(calc(n, k))
