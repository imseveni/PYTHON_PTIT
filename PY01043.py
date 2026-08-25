def solve():
    n = int(input())

    for i in range(2, n, 2):
        x = str(i)

        check = False
        for c in x:
            temp = int(c)
            if(temp % 2 == 1):
                check = True
                break

        if(check):
            continue
        
        x = x + x[::-1]

        if(int(x) >= n): 
            break

        print(x, end = " ")

    print()        

if __name__ == "__main__":
    T = 1
    T = int(input())

    for _ in range(T):
        solve()