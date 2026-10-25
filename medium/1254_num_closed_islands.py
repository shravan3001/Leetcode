"""
https://leetcode.com/problems/number-of-closed-islands/description/?envType=daily-question&envId=2026-10-25
1254. Number of Closed Islands

Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.
Return the number of closed islands.

Example 1:
Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation:
Islands in gray are closed because they are completely surrounded by water (group of 1s).

Example 2:
Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1

Example 3:
Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2

Constraints:
    1 <= grid.length, grid[0].length <= 100
    0 <= grid[i][j] <=1
"""

import unittest
from collections import deque

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]


class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        ans = 0
        n = len(grid)
        m = len(grid[0])
        vis: list[list[bool]] = [[False] * m for _ in range(n)]

        def bfs(i: int, j: int) -> int:
            ret = 1
            q: deque[tuple[int, int]] = deque([(i, j)])
            while q:
                ci, cj = q.popleft()
                for di, dj in dirs:
                    ni = ci + di
                    nj = cj + dj
                    if ni < 0 or ni == n or nj < 0 or nj == m:
                        ret = 0
                        continue
                    if not vis[ni][nj] and grid[ni][nj]==0:
                        vis[ni][nj] = True
                        q.append((ni, nj))
            return ret

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0 and not vis[i][j]:
                    vis[i][j] = True
                    ans += bfs(i, j)
        return ans


class TestClosedIsland(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        grid = [
            [1, 1, 1, 1, 1, 1, 1, 0],
            [1, 0, 0, 0, 0, 1, 1, 0],
            [1, 0, 1, 0, 1, 1, 1, 0],
            [1, 0, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 0],
        ]
        output = 2
        self.assertEqual(self.sol.closedIsland(grid), output)

    def test_example_2(self):
        grid = [[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]
        output = 1
        self.assertEqual(self.sol.closedIsland(grid), output)

    def test_example_3(self):
        grid = [
            [1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1],
        ]
        output = 2
        self.assertEqual(self.sol.closedIsland(grid), output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
