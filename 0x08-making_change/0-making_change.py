#!/usr/bin/python3
"""
make change task
"""
def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total.

    :param coins: List of integers representing the coin denominations
    :param total: Integer representing the total amount to be achieved
    :return: Minimum number of coins needed to make the total or -1 if not possible
    """
    if total <= 0:
        return 0

    # Initialize the DP array with a large number (infinity)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: No coins needed to make amount 0

    # Update the DP array
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # Return the result
    return dp[total] if dp[total] != float('inf') else -1

