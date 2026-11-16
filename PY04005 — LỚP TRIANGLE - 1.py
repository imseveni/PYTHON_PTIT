import sys
from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return sqrt(
            (self.x - other.x) ** 2 +
            (self.y - other.y) ** 2
        )


data = sys.stdin.buffer.read().split()

T = int(data[0])
pos = 1

for _ in range(T):
    x1 = float(data[pos])
    y1 = float(data[pos + 1])
    x2 = float(data[pos + 2])
    y2 = float(data[pos + 3])
    x3 = float(data[pos + 4])
    y3 = float(data[pos + 5])

    pos += 6

    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    p3 = Point(x3, y3)

    area = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)

    if abs(area) < 1e-9:
        print("INVALID")
    else:
        chu_vi = (
            p1.distance(p2)
            + p2.distance(p3)
            + p3.distance(p1)
        )

        print(f"{chu_vi:.3f}")