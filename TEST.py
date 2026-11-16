import sys

class Process:
    def __init__(self, pid, at, bt):
        self.pid = pid
        self.at = at
        self.bt = bt
        self.remaining = bt

    def copy(self):
        return Process(self.pid, self.at, self.bt)


def merge_gantt(raw_gantt):
    """Gộp các đoạn biểu đồ Gantt liên tiếp có cùng PID/IDLE."""
    if not raw_gantt:
        return ""
    merged = [list(raw_gantt[0])]
    for seg in raw_gantt[1:]:
        if seg[2] == merged[-1][2] and seg[0] == merged[-1][1]:
            merged[-1][1] = seg[1]
        else:
            merged.append(list(seg))
    return " | ".join(f"[{s},{e}) {pid}" for s, e, pid in merged)


def run_round_robin(original_procs, q):
    """Mô phỏng thuật toán Round Robin (RR)."""
    n = len(original_procs)
    procs = [p.copy() for p in original_procs]
    
    current_time = 0
    completed = 0
    in_queue = [False] * n
    ready_queue = []
    gantt = []

    init_arrived = [i for i in range(n) if procs[i].at == 0]
    init_arrived.sort()
    for idx in init_arrived:
        ready_queue.append(idx)
        in_queue[idx] = True

    while completed < n:
        if not ready_queue:
            next_at = min(p.at for p in procs if p.remaining > 0 and not in_queue[p.pid - 1])
            gantt.append((current_time, next_at, "IDLE"))
            current_time = next_at

            arrived = [i for i in range(n) if procs[i].at == current_time and not in_queue[i] and procs[i].remaining > 0]
            arrived.sort()
            for idx in arrived:
                ready_queue.append(idx)
                in_queue[idx] = True

        u = ready_queue.pop(0)

        exec_time = min(q, procs[u].remaining)
        gantt.append((current_time, current_time + exec_time, f"P{procs[u].pid}"))

        start_time = current_time
        current_time += exec_time
        procs[u].remaining -= exec_time

        newly_arrived = []
        for i in range(n):
            if not in_queue[i] and procs[i].remaining > 0 and start_time < procs[i].at <= current_time:
                newly_arrived.append((procs[i].at, i))

        newly_arrived.sort(key=lambda x: (x[0], x[1]))
        for _, idx in newly_arrived:
            ready_queue.append(idx)
            in_queue[idx] = True

        if procs[u].remaining > 0:
            ready_queue.append(u)
        else:
            completed += 1

    print("Gantt RR:")
    print(merge_gantt(gantt))


def run_srtf(original_procs):
    """Mô phỏng thuật toán Shortest Remaining Time First (SRTF)."""
    n = len(original_procs)
    procs = [p.copy() for p in original_procs]
    
    current_time = 0
    completed = 0
    gantt = []

    while completed < n:
        best_idx = -1
        min_remaining = float('inf')

        for i in range(n):
            if procs[i].at <= current_time and procs[i].remaining > 0:
                if procs[i].remaining < min_remaining:
                    min_remaining = procs[i].remaining
                    best_idx = i
                elif procs[i].remaining == min_remaining:
                    if procs[i].at < procs[best_idx].at:
                        best_idx = i
                    elif procs[i].at == procs[best_idx].at and i < best_idx:
                        best_idx = i

        if best_idx == -1:
            next_at = min(p.at for p in procs if p.remaining > 0)
            gantt.append((current_time, next_at, "IDLE"))
            current_time = next_at
        else:
            gantt.append((current_time, current_time + 1, f"P{procs[best_idx].pid}"))
            procs[best_idx].remaining -= 1
            current_time += 1

            if procs[best_idx].remaining == 0:
                completed += 1

    print("Gantt SRTF:")
    print(merge_gantt(gantt))


def main():
    try:
        input_data = sys.stdin.read().split()
        if not input_data:
            return
        
        n = int(input_data[0])
        q = int(input_data[1])

        # Ràng buộc dữ liệu đầu vào
        if n < 1 or n > 100 or q <= 0:
            print("Loi: Du lieu dau vao khong hop le!")
            return

        procs = []
        idx = 2
        for i in range(1, n + 1):
            at = int(input_data[idx])
            bt = int(input_data[idx + 1])
            idx += 2
            
            if at < 0 or bt <= 0:
                print("Loi: Du lieu dau vao khong hop le!")
                return
            
            procs.append(Process(i, at, bt))

        run_round_robin(procs, q)
        run_srtf(procs)

    except Exception:
        print("Loi: Du lieu dau vao khong hop le!")


if __name__ == "__main__":
    main()