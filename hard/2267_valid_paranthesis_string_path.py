"""
https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/description/?envType=daily-question&envId=2026-09-29
2267. Check if There Is a Valid Parentheses String Path

A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:
    It is ().
    It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
    It can be written as (A), where A is a valid parentheses string.
You are given an m x n matrix of parentheses grid. A valid parentheses string path in the grid is a path satisfying all of the following conditions:
    The path starts from the upper left cell (0, 0).
    The path ends at the bottom-right cell (m - 1, n - 1).
    The path only ever moves down or right.
    The resulting parentheses string formed by the path is valid.
Return true if there exists a valid parentheses string path in the grid. Otherwise, return false.

Example 1:
Input: grid = [["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]
Output: true
Explanation: The above diagram shows two possible paths that form valid parentheses strings.
The first path shown results in the valid parentheses string "()(())".
The second path shown results in the valid parentheses string "((()))".
Note that there may be other valid parentheses string paths.

Example 2:
Input: grid = [[")",")"],["(","("]]
Output: false
Explanation: The two possible paths form the parentheses strings "))(" and ")((". Since neither of them are valid parentheses strings, we return false.

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 100
    grid[i][j] is either '(' or ')'.
"""

import unittest


class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        # A valid path has length m + n - 1, which must be even.
        if (m + n - 1) % 2 == 1:
            return False
        # Must start with '(' and end with ')'.
        if grid[0][0] == ")" or grid[m - 1][n - 1] == "(":
            return False

        # A balance can never exceed half the path length (otherwise it
        # cannot return to 0), so cap it to keep the bitmask small.
        max_bal = (m + n - 1) // 2
        limit_mask = (1 << (max_bal + 1)) - 1

        # dp[j] is a bitmask: bit b set => balance b is reachable at (i, j).
        dp = [0] * n
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    incoming = 1  # balance 0 before consuming the first cell
                else:
                    incoming = dp[j] if i > 0 else 0  # from above (previous row)
                    if j > 0:
                        incoming |= dp[j - 1]  # from the left (current row)

                if grid[i][j] == "(":
                    cur = (incoming << 1) & limit_mask
                else:
                    cur = incoming >> 1  # drops balance 0 -> -1 automatically
                dp[j] = cur

        return bool(dp[n - 1] & 1)  # balance 0 reachable at the end


class TestHasValidPath(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        grid = [["(", "(", "("], [")", "(", ")"], ["(", "(", ")"], ["(", "(", ")"]]
        output = True
        self.assertEqual(self.sol.hasValidPath(grid), output)

    def test_example_2(self):
        grid = [[")", ")"], ["(", "("]]
        output = False
        self.assertEqual(self.sol.hasValidPath(grid), output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
