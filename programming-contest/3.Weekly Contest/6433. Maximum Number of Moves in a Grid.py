"""
https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/

6433. Maximum Number of Moves in a Grid

You are given a 0-indexed m x n matrix grid consisting of positive integers.

You can start at any cell in the first column of the matrix, and traverse the grid in the following way:

From a cell (row, col), you can move to any of the cells: (row - 1, col + 1), (row, col + 1) and (row + 1, col + 1) such that the value of the cell you move to, should be strictly bigger than the value of the current cell.
Return the maximum number of moves that you can perform.



Example 1:
Input: grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
Output: 3
Explanation: We can start at the cell (0, 0) and make the following moves:
- (0, 0) -> (0, 1).
- (0, 1) -> (1, 2).
- (1, 2) -> (2, 3).
It can be shown that it is the maximum number of moves that can be made.


Example 2:
Input: grid = [[3,2,4],[2,1,9],[1,1,7]]
Output: 0
Explanation: Starting from any cell in the first column we cannot perform any moves.



Constraints:
m == grid.length
n == grid[i].length
2 <= m, n <= 1000
4 <= m * n <= 100000
1 <= grid[i][j] <= 1000000


"""
from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        row_len, col_len = len(grid), len(grid[0])

        dp = [[0] * col_len for _ in range(row_len)]

        for col in range(col_len - 2, -1, -1):
            for row in range(row_len):
                for direct in [-1, 0, 1]:
                    nxt_row = direct + row
                    if 0 <= direct + row < row_len and grid[row][col] < grid[nxt_row][col + 1]:
                        dp[row][col] = max(dp[row][col], 1 + dp[nxt_row][col + 1])

        return max(dp[row][0] for row in range(row_len))


print(Solution().maxMoves(grid=[[2, 4, 3, 5], [5, 4, 9, 3], [3, 4, 2, 11], [10, 9, 13, 15]]))
