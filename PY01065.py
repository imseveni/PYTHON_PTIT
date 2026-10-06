def match(val, pattern):
    s = str(val)
    for ch_s, ch_p in zip(s, pattern):
        if ch_p != '?' and ch_s != ch_p:
            return False
    return True

def calc(pA, op, pB, eq, pC):
    if op in ['*', '/']:
        return "WRONG PROBLEM!"

    valid_a = [a for a in range(10, 100) if match(a, pA)]
    valid_b = [b for b in range(10, 100) if match(b, pB)]
    valid_op = ['+', '-'] if op == '?' else [op]

    exist = False
    for o in valid_op:
        for a in valid_a:
            for b in valid_b:
                c = a + b if o == '+' else a - b
                if 10 <= c <= 99 and match(c, pC):
                    return (f"{a} {o} {b} = {c}")

    return "WRONG PROBLEM!"

T = int(input())
for _ in range(T):
    pA, op, pB, eq, pC = input().split()
    print(calc(pA, op, pB, eq, pC))
    


    