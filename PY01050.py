n = int(input())

def backtrack(current_str, cnt_a, cnt_b, cnt_c, target_len):
    if len(current_str) == target_len:
        if cnt_a >= 1 and cnt_b >= cnt_a and cnt_c >= cnt_b:
            print(current_str)
        return

    rem = target_len - len(current_str)
    if cnt_a == 0 and rem < 1:
        return
    if cnt_b == 0 and rem < 1:
        return
    if cnt_c == 0 and rem < 1:
        return

    backtrack(current_str + 'A', cnt_a + 1, cnt_b, cnt_c, target_len)
    backtrack(current_str + 'B', cnt_a, cnt_b + 1, cnt_c, target_len)
    backtrack(current_str + 'C', cnt_a, cnt_b, cnt_c + 1, target_len)

for length in range(3, n + 1):
    backtrack("", 0, 0, 0, length)