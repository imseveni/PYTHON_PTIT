import sys


def solve():
    input_line = sys.stdin.readline
    first_line = input_line()
    if not first_line:
        return

    t = int(first_line.strip())
    out = []

    for _ in range(t):
        n_line = input_line()
        while n_line and not n_line.strip():
            n_line = input_line()
        if not n_line:
            break
        n = int(n_line.strip())

        max1 = max2 = max3 = -(10**18)
        count = 0

        # Đọc cho tới khi đủ n phần tử (đề phòng input chia nhiều dòng)
        while count < n:
            line = input_line()
            if not line:
                break
            for x in map(int, line.split()):
                if x >= max1:
                    max3 = max2
                    max2 = max1
                    max1 = x
                elif x >= max2:
                    max3 = max2
                    max2 = x
                elif x > max3:
                    max3 = x
                count += 1

        out.append(str(max1 + max2 + max3))

    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    solve()