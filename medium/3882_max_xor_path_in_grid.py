"""
https://leetcode.com/problems/minimum-xor-path-in-a-grid/description/?envType=daily-question&envId=2026-10-28
3882. Minimum XOR Path in a Grid

You are given a 2D integer array grid of size m * n.
You start at the top-left cell (0, 0) and want to reach the bottom-right cell (m - 1, n - 1).
At each step, you may move either right or down.
The cost of a path is defined as the bitwise XOR of all the values in the cells along that path, including the start and end cells.
Return the minimum possible XOR value among all valid paths from (0, 0) to (m - 1, n - 1).

Example 1:
Input: grid = [[1,2],[3,4]]
Output: 6
Explanation:
There are two valid paths:
    (0, 0) → (0, 1) → (1, 1) with XOR: 1 XOR 2 XOR 4 = 7
    (0, 0) → (1, 0) → (1, 1) with XOR: 1 XOR 3 XOR 4 = 6
The minimum XOR value among all valid paths is 6.

Example 2:
Input: grid = [[6,7],[5,8]]
Output: 9
Explanation:
There are two valid paths:
    (0, 0) → (0, 1) → (1, 1) with XOR: 6 XOR 7 XOR 8 = 9
    (0, 0) → (1, 0) → (1, 1) with XOR: 6 XOR 5 XOR 8 = 11
The minimum XOR value among all valid paths is 9.

Example 3:
Input: grid = [[2,7,5]]
Output: 0
Explanation:
There is only one valid path:
    (0, 0) → (0, 1) → (0, 2) with XOR: 2 XOR 7 XOR 5 = 0
The XOR value of this path is 0, which is the minimum possible.

Constraints:
    1 <= m == grid.length <= 1000
    1 <= n == grid[i].length <= 1000
    m * n <= 1000
    0 <= grid[i][j] <= 1023
"""

import unittest


class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp: list[list[set[int]]] = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(grid[0][0])
        for i in range(1, n):
            dp[0][i] = set(grid[0][i] ^ x for x in dp[0][i - 1])
        for i in range(1, m):
            dp[i][0] = set(grid[i][0] ^ x for x in dp[i - 1][0])
        for i in range(1, m):
            for j in range(1, n):
                for x in dp[i - 1][j]:
                    dp[i][j].add(grid[i][j] ^ x)
                for x in dp[i][j - 1]:
                    dp[i][j].add(grid[i][j] ^ x)
        return min(dp[m - 1][n - 1])


class TestMinCost(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        grid = [[1, 2], [3, 4]]
        output = 6
        self.assertEqual(self.sol.minCost(grid), output)

    def test_example_2(self):
        grid = [[6, 7], [5, 8]]
        output = 9
        self.assertEqual(self.sol.minCost(grid), output)

    def test_example_3(self):
        grid = [[2, 7, 5]]
        output = 0
        self.assertEqual(self.sol.minCost(grid), output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
