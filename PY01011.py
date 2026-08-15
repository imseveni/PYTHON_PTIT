def check(s):
    for c in s:
        if c not in "02468":
            return False
    return True

def solve():
    T = int(input())

    for _ in range(T):
        N = int(input())

        k = 2
        while True:
            strK = str(k)
            if(check(strK)):
                ans = strK + strK[::-1]
                num = int(ans)

                if num >= N:
                    break
                else:
                    print(num, end = " ")

            k += 1

        print()

if __name__ == "__main__":
    solve()