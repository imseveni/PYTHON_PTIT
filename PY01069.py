n = int(input())

digits = [2, 3, 5, 7]
results = []
current = []

def Try():
    if 4 <= len(current) <= n:
        if current[-1] != 2 and {2, 3, 5, 7}.issubset(set(current)):
            results.append("".join(map(str, current)))


    if len(current) < n:
        for d in digits:
            current.append(d)
            Try()
            current.pop() 


Try()

results.sort(key=lambda x: (len(x), x))
print("\n".join(results))