def minimum_days_to_buy_food(N, S, M):
    # Total food required to survive S days
    total_food_required = S * M

    # Total number of days when shop is open
    total_days_open = S - (S // 7)

    # If daily requirement of food is more than what can be bought in a day, survival is impossible
    if M > N:
        return -1

    # Minimum number of days required to buy the total food
    min_days_needed = (total_food_required + N - 1) // N

    # Check if the number of days required to buy the food is less than or equal to the days shop is open
    if min_days_needed <= total_days_open:
        return min_days_needed
    else:
        return -1

# Example usage:
N = 16
S = 10
M = 2

print(minimum_days_to_buy_food(N, S, M))  # Output: 2