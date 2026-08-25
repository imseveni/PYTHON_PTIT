def solve():
    set1 = set(input().lower().split())
    set2 = set(input().lower().split())

    union_words = sorted(set1 | set2)

    intersection_words = sorted(set1 & set2)

    print(" ".join(union_words))
    print(" ".join(intersection_words))

if __name__ == "__main__":
    T = 1
    # T = int(input())

    for _ in range(T):
        solve()