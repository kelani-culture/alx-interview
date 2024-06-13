#!/usr/bin/python3
"""
text file, there is a single character H.
Your text editor can execute only two operations in this file
"""

def minOperations(n):
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
