import sys
data = sys.stdin.read().split()

it = iter(data)
T = int(next(it))

for _ in range(T):
    n = int(next(it))
    k = int(next(it))

    points = []
    for _ in range(n):
        x = int(next(it))
        y = int(next(it))
        points.append((x, y))

    found = False
    for i in range(n):
        if found:
            break
        for j in range(i + 1, n):
            if found:
                break
            for m in range(j + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                x3, y3 = points[m]

                det = 2 * (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)
                if det == 0:
                    continue

                sq1 = x1 * x1 + y1 * y1
                sq2 = x2 * x2 + y2 * y2
                sq3 = x3 * x3 + y3 * y3

                p1 = sq2 - sq1
                p2 = sq3 - sq1

                x0 = ((y3 - y1) * p1 - (y2 - y1) * p2) / det
                y0 = ((x2 - x1) * p2 - (x3 - x1) * p1) / det

                r2 = (x1 - x0) ** 2 + (y1 - y0) ** 2

                count = 0
                eps = 1e-7
                for p in range(n):
                    if p == i or p == j or p == m:
                        continue
                    xp, yp = points[p]
                    dist2 = (xp - x0) ** 2 + (yp - y0) ** 2
                    if dist2 < r2 - eps:
                        count += 1
                        if count > k:
                            break

                if count == k:
                    found = True
                    break

    