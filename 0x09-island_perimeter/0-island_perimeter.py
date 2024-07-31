#!/usr/bin/python3
"""
This module defines the function island_perimeter
which calculates the perimeter of the island in a grid.
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the grid.

    Args:
        grid (list of list of int): The grid representing the map,
                                    where 0 represents water and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    if not grid or not grid[0]:
        return 0

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Each land cell has 4 possible sides to contribute to the perimeter
                perimeter += 4

                # Check above
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2

                # Check left
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2

    return perimeter

