def fractional_knapsack(values, weights, capacity):
    n = len(values)
    items = [(values[i] / weights[i], values[i], weights[i]) for i in range(n)]
    items.sort(reverse=True)
    
    total_value = 0.0
    
    for value_per_weight, value, weight in items:
        if capacity >= weight:
            capacity -= weight
            total_value += value
        else:
            total_value += value_per_weight * capacity
            break
    
    return total_value

values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

print(fractional_knapsack(values, weights, capacity))  # Output: 240.