import bisect
import sys


def get_primes(limit):
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            sieve[i * i : limit + 1 : i] = b"\x00" * (
                (limit - i * i) // i + 1
            )
    return [i for i in range(2, limit + 1) if sieve[i]]


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    t = int(input_data[0])
    queries = []
    max_b = 0
    idx = 1

    for _ in range(t):
        a = int(input_data[idx])
        b = int(input_data[idx + 1])
        idx += 2
        queries.append((a, b))
        if b > max_b:
            max_b = b

    primes = get_primes(max_b)
    MOD = 10**9 + 7
    results = []

    for a, b in queries:
        ans = 1
        a_minus_1 = a - 1
        sqrt_b = int(b**0.5)

        # 1. Xử lý các số nguyên tố p <= sqrt(b) (tối đa 168 số)
        i = 0
        num_primes = len(primes)
        while i < num_primes and primes[i] <= sqrt_b:
            p = primes[i]
            e = 0
            temp_b = b
            temp_a = a_minus_1
            while temp_b >= p:
                temp_b //= p
                e += temp_b
            while temp_a >= p:
                temp_a //= p
                e -= temp_a
            if e > 0:
                ans = (ans * (2 * e + 1)) % MOD
            i += 1

        # 2. Xử lý các số nguyên tố p > sqrt(b): khi đó e = b//p - (a-1)//p
        # Nhóm các p có cùng giá trị (b//p) và ((a-1)//p) để dùng pow()
        limit_idx = bisect.bisect_right(primes, b)
        curr_idx = i
        while curr_idx < limit_idx:
            p = primes[curr_idx]
            q_b = b // p
            q_a = a_minus_1 // p

            # Tìm biên trên lớn nhất của p giữ nguyên cả q_b và q_a
            max_p = b // q_b
            if q_a > 0:
                max_p_a = a_minus_1 // q_a
                if max_p_a < max_p:
                    max_p = max_p_a

            next_idx = bisect.bisect_right(primes, max_p, curr_idx, limit_idx)
            count = next_idx - curr_idx
            e = q_b - q_a
            if e > 0:
                ans = (ans * pow(2 * e + 1, count, MOD)) % MOD
            curr_idx = next_idx

        results.append(str(ans))

    sys.stdout.write("\n".join(results) + "\n")


if __name__ == "__main__":
    solve()