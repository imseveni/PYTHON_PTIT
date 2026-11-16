import math

a, b = map(int, input().split())

c = math.sqrt(a**2 + b**2)

r = (a + b - c) / 2

L = max(a, b)

cosA = L / c

s = math.sqrt((1 - cosA) / 2)

q = (1 - s) / (1 + s)

S_circle = math.pi * r * r / (1 - q * q)

S_triangle = a * b / 2

ans = S_circle / S_triangle

print(f"{ans:.4f}")