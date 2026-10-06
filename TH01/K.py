def solve():
    str = input()

    n = len(str)
    if(n % 3 == 1): str = "00" + str
    elif(n % 3 == 2): str = "0" + str

    for i in range(0, len(str), 3):
        x = 0
        cnt = 0
        for j in range(i + 2, i - 1, -1):
            if(str[j] == '1'):
                x += pow(2, cnt)
            cnt += 1
        print(x, end = "")
    
if __name__ == "__main__":
    T = 1
    # T = int(input())

    for _ in range(T):
        solve()