def solve():
    T = int(input())

    for _ in range(T):
        str = input()

        count = 1
        for i in range(len(str) - 1):
            if(str[i] == str[i + 1]):
                count += 1
            else:
                print(count, str[i], sep = "", end = "")
                count = 1

        print(count, str[-1], sep = "")

if __name__ == "__main__":
    solve()