def solve():
    str = input()

    upperCount = sum(1 for c in str if c.isupper())
    lowerCount = len(str) - upperCount

    if(lowerCount >= upperCount):
        print(str.lower())
    else:
        print(str.upper())

if __name__ == "__main__":
    solve()