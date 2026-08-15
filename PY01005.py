def solve():
    N = input()

    count = 0
    for i in range(len(N)):
        if N[i] == '4' or N[i] == '7': 
            count += 1

    if count == 4 or count == 7: 
        print("YES")
    else: 
        print("NO")

if __name__ == "__main__":
    solve()