def average_waiting_time(bt):
    n = len(bt)
    bt.sort()
    waiting_time = 0
    total_waiting_time = 0

    for i in range(n):
        total_waiting_time += waiting_time
        waiting_time += bt[i]

    avg_waiting_time = total_waiting_time // n
    return avg_waiting_time

bt = [6, 8, 7, 3]
print(average_waiting_time(bt))  # Output: 6