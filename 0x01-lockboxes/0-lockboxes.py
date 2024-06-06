#!/usr/bin/python3
"""
This module provides a function to determine if all boxes can be unlocked.

The function `canUnlockAll` accepts a list of lists where each sublist contains
keys to other boxes. The goal is to check if all boxes can be unlocked starting
from the first box.
"""

from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    Determine if all boxes can be unlocked.

    Args:
        boxes (List[List[int]]): A list of lists, where each sublist contains
                                 keys to other boxes.

    Returns:
        bool: True if all boxes can be unlocked, otherwise False.
    """
    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    keys = [0]

    while keys:
        current_key = keys.pop(0)
        for key in boxes[current_key]:
            if key < n and not opened[key]:
                opened[key] = True
                keys.append(key)

    return all(opened)