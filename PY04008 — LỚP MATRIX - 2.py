import sys


class Matrix:

    def __init__(self, n, m, data):
        self.n = n
        self.m = m
        self.data = data

    def trans(self):
        # Tạo ma trận chuyển vị kích thước m x n
        t_data = [
            [self.data[i][j] for i in range(self.n)] for j in range(self.m)
        ]
        return Matrix(self.m, self.n, t_data)

    def mul(self, other):
        # Nhân ma trận self (n x m) với other (m x p)
        res = [[0] * other.m for _ in range(self.n)]
        for i in range(self.n):
            for j in range(other.m):
                s = 0
                for k in range(self.m):
                    s += self.data[i][k] * other.data[k][j]
                res[i][j] = s
        return Matrix(self.n, other.m, res)

    def __str__(self):
        return "\n".join(" ".join(map(str, row)) for row in self.data)


def solve():
    tokens = sys.stdin.read().split()
    if not tokens:
        return

    t = int(tokens[0])
    idx = 1
    out = []

    for _ in range(t):
        n = int(tokens[idx])
        m = int(tokens[idx + 1])
        idx += 2

        data = []
        for _ in range(n):
            row = [int(x) for x in tokens[idx : idx + m]]
            data.append(row)
            idx += m

        mat = Matrix(n, m, data)
        res = mat.mul(mat.trans())
        out.append(str(res))

    print("\n".join(out))


if __name__ == "__main__":
    solve()