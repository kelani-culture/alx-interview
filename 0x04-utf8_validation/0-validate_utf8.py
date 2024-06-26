#!/usr/bin/env python3
""" Implement a function to validate utf-8"""


def validUTF8(data):
    """Utf-8 validate function implemented"""
    num_bytes = 0

    # Masks to check the most significant bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    # Iterate over each integer (byte) in the data
    for num in data:
        mask = 1 << 7
        if num_bytes == 0:
            # Determine how many bytes the current UTF-8 character has
            while mask & num:
                num_bytes += 1
                mask = mask >> 1

            # 1 byte character (0xxxxxxx) or invalid scenario
            if num_bytes == 0:
                continue

            # If num_bytes is more than 4 or 1 (invalid scenarios)
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # If this byte is not a valid continuation byte
            if not (num & mask1 and not (num & mask2)):
                return False

        # Decrement the number of bytes to process
        num_bytes -= 1

    # If we processed all characters successfully
    return num_bytes == 0
