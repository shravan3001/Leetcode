"""
https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/description/?envType=daily-question&envId=2026-10-26
3619. Count Islands With Total Value Divisible by K

You are given an m x n matrix grid and a positive integer k. An island is a group of positive integers (representing land) that are 4-directionally connected (horizontally or vertically).
The total value of an island is the sum of the values of all cells in the island.
Return the number of islands with a total value divisible by k.

Example 1:
Input: grid = [[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]], k = 5
Output: 2
Explanation:
The grid contains four islands. The islands highlighted in blue have a total value that is divisible by 5, while the islands highlighted in red do not.

Example 2:
Input: grid = [[3,0,3,0], [0,3,0,3], [3,0,3,0]], k = 3
Output: 6
Explanation:
The grid contains six islands, each with a total value that is divisible by 3.

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 1000
    1 <= m * n <= 1e5
    0 <= grid[i][j] <= 1e6
    1 <= k <= 1e6
"""

import unittest
from collections import deque

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]


class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        vis: list[list[bool]] = [[False] * m for _ in range(n)]

        def bfs(i: int, j: int) -> int:
            q = deque([(i, j)])
            vis[i][j] = True
            ans = grid[i][j]

            while q:
                ci, cj = q.popleft()
                for di, dj in dirs:
                    ni = ci + di
                    nj = cj + dj
                    if (
                        ni < 0
                        or ni == n
                        or nj < 0
                        or nj == m
                        or grid[ni][nj] == 0
                        or vis[ni][nj]
                    ):
                        continue
                    vis[ni][nj] = True
                    ans += grid[ni][nj]
                    q.append((ni, nj))
            return ans

        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0 and not vis[i][j]:
                    s = bfs(i, j)
                    if s % k == 0:
                        count += 1
        return count


class TestCountIslands(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        grid = [
            [0, 2, 1, 0, 0],
            [0, 5, 0, 0, 5],
            [0, 0, 1, 0, 0],
            [0, 1, 4, 7, 0],
            [0, 2, 0, 0, 8],
        ]
        k = 5
        output = 2
        self.assertEqual(self.sol.countIslands(grid, k), output)

    def test_example_2(self):
        grid = [[3, 0, 3, 0], [0, 3, 0, 3], [3, 0, 3, 0]]
        k = 3
        output = 6
        self.assertEqual(self.sol.countIslands(grid, k), output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
