def input_data():
    print("Enter the number of processes and resources:")
    np = int(input())
    nr = int(input())
    need = [[0]*nr for _ in range(np)]
    max = [[0]*nr for _ in range(np)]
    allocate = [[0]*nr for _ in range(np)]
    avail = [0]*nr

    print("Enter the allocation matrix:")
    for i in range(np):
        for j in range(nr):
            allocate[i][j] = int(input())

    print("Enter the max matrix:")
    for i in range(np):
        for j in range(nr):
            max[i][j] = int(input())

    print("Enter the available matrix:")
    for j in range(nr):
        avail[j] = int(input())

    return np, nr, need, max, allocate, avail

def calc_need(np, nr, need, max, allocate):
    for i in range(np):
        for j in range(nr):
            need[i][j] = max[i][j] - allocate[i][j]
    return need

def check(i, nr, need, avail):
    for j in range(nr):
        if avail[j] < need[i][j]:
            return False
    return True

def is_safe():
    np, nr, need, max, allocate, avail = input_data()
    need = calc_need(np, nr, need, max, allocate)
    done = [False] * np
    j = 0

    while j < np:
        allocated = False
        for i in range(np):
            if not done[i] and check(i, nr, need, avail):
                for k in range(nr):
                    avail[k] = avail[k] - need[i][k] + max[i][k]
                print(f"Allocated process: {i}")
                allocated = done[i] = True
                j += 1

        if not allocated:
            break

    if j == np:
        print("Safely allocated")
    else:
        print("All processes cannot allocate safely")

if __name__ == "__main__":
    is_safe()
