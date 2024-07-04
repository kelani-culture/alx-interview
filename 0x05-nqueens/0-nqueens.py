#!/usr/bin/python3
import sys

"""Nqueens alogrinthm solved"""


class NQueens:
    """N queens object solved"""

    def __init__(self, n):
        self.n = n
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        self.solutions = []

    def is_safe(self, row, col):
        """check is safe method"""
        # Check this row on the left side
        for i in range(col):
            if self.board[row][i] == 1:
                return False

        # Check upper diagonal on the left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        # Check lower diagonal on the left side
        for i, j in zip(range(row, self.n, 1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        return True

    def solve_nqueens_util(self, col):
        """solve nqueens utils"""
        if col >= self.n:
            self.solutions.append([list(row) for row in self.board])
            return True

        res = False
        for i in range(self.n):
            if self.is_safe(i, col):
                self.board[i][col] = 1
                res = self.solve_nqueens_util(col + 1) or res
                self.board[i][col] = 0

        return res

    def solve(self):
        """solve nqueens method"""
        self.solve_nqueens_util(0)
        return self.solutions

    def print_solutions(self):
        """print nqueens solutions"""
        for solution in self.solutions:
            result = []
            for i in range(self.n):
                for j in range(self.n):
                    if solution[i][j] == 1:
                        result.append([i, j])
            print(result)


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens = NQueens(n)
    nqueens.solve()
    nqueens.print_solutions()


if __name__ == "__main__":
    main()
