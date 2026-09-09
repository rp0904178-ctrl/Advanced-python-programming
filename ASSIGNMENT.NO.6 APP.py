# Experiment No. 6
# 0/1 Knapsack using Bottom-Up and Top-Down DP


# -------------------------------------------------
# Bottom-Up Dynamic Programming
# -------------------------------------------------

def knapsack_bottom_up(weights, values, capacity):
    n = len(weights)

    # Create DP table
    dp = [[0 for _ in range(capacity + 1)]
          for _ in range(n + 1)]

    # Build the table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):

            if weights[i - 1] <= w:

                include = (
                    values[i - 1]
                    + dp[i - 1][w - weights[i - 1]]
                )

                exclude = dp[i - 1][w]

                dp[i][w] = max(include, exclude)

            else:
                dp[i][w] = dp[i - 1][w]

    # Find selected items
    selected_items = []
    w = capacity

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i)
            w -= weights[i - 1]

    selected_items.reverse()

    return dp[n][capacity], selected_items


# -------------------------------------------------
# Top-Down Dynamic Programming with Memoization
# -------------------------------------------------

def knapsack_top_down(weights, values, n, capacity, memo):

    # Base case
    if n == 0 or capacity == 0:
        return 0

    # Check if already calculated
    if memo[n][capacity] != -1:
        return memo[n][capacity]

    # If item is too heavy, exclude it
    if weights[n - 1] > capacity:
        memo[n][capacity] = knapsack_top_down(
            weights,
            values,
            n - 1,
            capacity,
            memo
        )

    else:
        # Include current item
        include = (
            values[n - 1]
            + knapsack_top_down(
                weights,
                values,
                n - 1,
                capacity - weights[n - 1],
                memo
            )
        )

        # Exclude current item
        exclude = knapsack_top_down(
            weights,
            values,
            n - 1,
            capacity,
            memo
        )

        memo[n][capacity] = max(include, exclude)

    return memo[n][capacity]


def find_selected_items(weights, values, n, capacity, memo):
    selected_items = []

    i = n
    w = capacity

    while i > 0 and w > 0:

        if weights[i - 1] <= w:

            include = (
                values[i - 1]
                + (memo[i - 1][w - weights[i - 1]]
                   if memo[i - 1][w - weights[i - 1]] != -1
                   else 0)
            )

            if memo[i][w] == include:
                selected_items.append(i)
                w -= weights[i - 1]

        i -= 1

    selected_items.reverse()
    return selected_items


# -------------------------------------------------
# Main Program
# -------------------------------------------------

print("===== 0/1 Knapsack Problem =====")

n = int(input("Enter number of items: "))

weights = []
values = []

for i in range(n):
    print(f"\nItem {i + 1}")
    weight = int(input("Enter weight: "))
    value = int(input("Enter value: "))

    weights.append(weight)
    values.append(value)

capacity = int(input("\nEnter knapsack capacity: "))


# Bottom-Up
bottom_value, bottom_items = knapsack_bottom_up(
    weights,
    values,
    capacity
)


# Top-Down
memo = [
    [-1 for _ in range(capacity + 1)]
    for _ in range(n + 1)
]

# Base cases
for i in range(n + 1):
    memo[i][0] = 0

for w in range(capacity + 1):
    memo[0][w] = 0

top_value = knapsack_top_down(
    weights,
    values,
    n,
    capacity,
    memo
)

top_items = find_selected_items(
    weights,
    values,
    n,
    capacity,
    memo
)


# Display results
print("\n===== Results =====")

print("\n--- Bottom-Up Approach ---")
print("Maximum Value:", bottom_value)
print("Selected Items:", bottom_items)

print("\n--- Top-Down Approach ---")
print("Maximum Value:", top_value)
print("Selected Items:", top_items)