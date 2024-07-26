def max_meetings(start, end, n):
    meetings = sorted(zip(start, end), key=lambda x: x[1])
    last_meeting_end = -1
    count = 0
    
    for s, e in meetings:
        if s > last_meeting_end:
            count += 1
            last_meeting_end = e
    
    return count

# Example usage
start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 6, 7, 9, 9]
n = len(start)

print(max_meetings(start, end, n))  # Output: 4