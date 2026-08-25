def solve():
    file = input().lower()

    if(len(file) < 3):
        print("no")
        return

    exten = file[-3::]
    if(exten != ".py"):
        print("no")
        return

    for i in range(len(file) - 3):
        if(file[i].isalpha() or file[i] == '.' or file[i] == '_'):
            continue
        else:
            print("no")
            return

    print("yes")

if __name__ == "__main__":
    T = 1
    # T = int(input())

    for _ in range(T):
        solve()