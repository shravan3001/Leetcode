"""
https://leetcode.com/problems/create-grid-with-exactly-one-path/description/?envType=daily-question&envId=2026-10-27
3963. Create Grid With Exactly One Path

You are given two integers m and n, representing the number of rows and columns of a grid.
Construct any m x n grid consisting only of the characters '.' and '#', where:
    '.' represents a free cell.
    '#' represents an obstacle cell.
A valid path is a sequence of free cells that:
    Starts at the top-left cell (0, 0).
    Ends at the bottom-right cell (m - 1, n - 1).
    Moves only:
        Right, from (i, j) to (i, j + 1), or
        Down, from (i, j) to (i + 1, j).
Return any grid such that there is exactly one valid path from the top-left cell to the bottom-right cell.

Example 1:
Input: m = 2, n = 3
Output: ["..#","#.."]
Explanation:
The only valid path is: (0,0) → (0,1) → (1,1) → (1,2)

Example 2:
Input: m = 3, n = 3
Output: ["..#","#..","##."]
Explanation:
The only valid path is: (0,0) → (0,1) → (1,1) → (1,2) → (2,2)

Example 3:
Input: m = 1, n = 4
Output: ["...."]
Explanation:
The only valid path is: (0,0) → (0,1) → (0,2) → (0,3)

Constraints:
    1 <= m, n <= 25
"""

import unittest


class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        ans: list[str] = []
        ans.append("." * n)
        for i in range(1, m):
            ans.append("#" * (n - 1) + ".")
        return ans


class TestCreateGrid(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        m, n = 2, 3
        output = ["..#", "#.."]
        self.assertEqual(self.sol.createGrid(m, n), output)

    def test_example_2(self):
        m, n = 3, 3
        output = ["..#", "#..", "##."]
        self.assertEqual(self.sol.createGrid(m, n), output)

    def test_example_3(self):
        m, n = 1, 4
        output = ["...."]
        self.assertEqual(self.sol.createGrid(m, n), output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
