from bisect import bisect_left
import sys

def solve():
    nums = [1, 2, 4, 6, 12, 24, 36, 48, 60, 120, 180, 240, 360, 720, 840, 1260, 1680, 2520, 5040, 7560, 10080, 15120, 20160,
        25200, 27720, 45360, 50400, 55440, 83160, 110880, 166320, 221760, 277200, 332640, 498960, 554400, 665280,
        720720, 1081080, 1441440, 2162160, 2882880, 3603600, 4324320, 6486480, 7207200, 8648640, 10810800]

    readline = sys.stdin.readline
    write = sys.stdout.write
    
    first_line = readline()
    t = int(first_line.strip())

    buf = []
    for _ in range(t):
        x = int(readline())
        buf.append(str(nums[bisect_left(nums, x)]))

        if len(buf) >= 50000:
            write('\n'.join(buf) + '\n')
            buf.clear()

    if buf:
        write('\n'.join(buf) + '\n')

if __name__ == '__main__':
    solve()