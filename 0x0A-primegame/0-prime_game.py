#!/usr/bin/python3
"""
A module to determine the winner of the prime game between Maria and Ben.
"""

def isWinner(x, nums):
    """Determine the winner of the game after x rounds."""
    if x == 0 or not nums:
        return None

    def sieve_of_eratosthenes(n):
        """Generate primes up to n using Sieve of Eratosthenes."""
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if sieve[i]:
                for j in range(i * i, n + 1, i):
                    sieve[j] = False
        return [i for i in range(2, n + 1) if sieve[i]]

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = sieve_of_eratosthenes(n)
        if not primes:
            ben_wins += 1
            continue

        rounds = 0
        while primes:
            prime = primes[0]
            primes = [p for p in primes if p % prime != 0]
            rounds += 1

        if rounds % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

