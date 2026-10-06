import sys

arr = list(map(int, sys.stdin.read().split()))

remain = {x % 42 for x in arr}

print(len(remain))