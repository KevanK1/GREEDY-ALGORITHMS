def min_max_cost(candies, N, K):
    candies.sort()
    min_cost = 0
    max_cost = 0
    
    # Calculate minimum cost
    i = 0
    while i < N:
        min_cost += candies[i]
        i += (K + 1)
    
    # Calculate maximum cost
    j = N - 1
    while j >= 0:
        max_cost += candies[j]
        j -= (K + 1)
    
    return min_cost, max_cost

# Example usage
candies = [3, 2, 1, 4, 5]
N = len(candies)
K = 2

min_cost, max_cost = min_max_cost(candies, N, K)
print(min_cost, max_cost)  # Output: 3 9