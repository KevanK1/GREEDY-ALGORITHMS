def min_intervals_to_remove(intervals):
    intervals.sort(key=lambda x: x[1])
    end = float('-inf')
    remove_count = 0
    
    for start, finish in intervals:
        if start < end:
            remove_count += 1
        else:
            end = finish
    
    return remove_count

# Example usage
intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
print(min_intervals_to_remove(intervals))  # Output: 1