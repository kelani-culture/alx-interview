#!/usr/bin/python3
"""
A module to determine the winner of the prime game between Maria and Ben.
"""

def is_prime(n):
    """
    check if a number is prime
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def isWinner(x, nums):
    """
    check for the winner
    """
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        remaining = list(range(2, n+1))
        while remaining:
            if len(remaining) == 1:
                ben_wins += 1
                break

            if len(remaining) == 0:
                maria_wins += 1
                break

            if remaining[0] == 1:
                remaining.pop(0)
                continue

            if is_prime(remaining[0]):
                player = "Maria" if len(remaining) % 2 == 1 else "Ben"
                prime = remaining[0]
                for i in range(prime, n+1, prime):
                    if i in remaining:
                        remaining.remove(i)
                if player == "Maria":
                    maria_wins += 1
                else:
                    ben_wins += 1
            else:
                remaining.pop(0)

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

