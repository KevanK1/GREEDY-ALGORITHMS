def min_diff_chocolates(A, N, M):
    if M == 0 or N == 0:
        return 0
    if N < M:
        return -1
    
    A.sort()
    min_diff = float('inf')

    for i in range(N - M + 1):
        diff = A[i + M - 1] - A[i]
        if diff < min_diff:
            min_diff = diff
    
    return min_diff

A = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50]
N = len(A)
M = 7

print(min_diff_chocolates(A, N, M))  # Output: 10