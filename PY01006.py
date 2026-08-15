def solve():
    T = int(input())

    for _ in range(T):
        N = input().strip()

        count = N.count('4') + N.count('7')

        if(count == len(N)): 
            print("YES")
        else:
            print("NO") 


if __name__ == "__main__":
    solve()