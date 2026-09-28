"""
https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/?envType=daily-question&envId=2026-09-28
1614. Maximum Nesting Depth of the Parentheses

Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.

Example 1:
Input: s = "(1+(2*3)+((8)/4))+1"
Output: 3
Explanation:
Digit 8 is inside of 3 nested parentheses in the string.

Example 2:
Input: s = "(1)+((2))+(((3)))"
Output: 3
Explanation:
Digit 3 is inside of 3 nested parentheses in the string.

Example 3:
Input: s = "()(())((()()))"
Output: 3

Constraints:
    1 <= s.length <= 100
    s consists of digits 0-9 and characters '+', '-', '*', '/', '(', and ')'.
    It is guaranteed that parentheses expression s is a VPS.
"""

import unittest


class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        max_depth = 0
        stack: list[str] = []
        max_val = lambda x, y: x if x >= y else y
        for c in s:
            if c == "(":
                stack.append(c)
                depth += 1
                max_depth = max_val(depth, max_depth)
            elif c == ")":
                stack.pop()
                depth -= 1
        return max_depth


class TestMaxDepth(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        s = "(1+(2*3)+((8)/4))+1"
        output = 3
        self.assertEqual(self.sol.maxDepth(s), output)

    def test_example_2(self):
        s = "(1)+((2))+(((3)))"
        output = 3
        self.assertEqual(self.sol.maxDepth(s), output)

    def test_example_3(self):
        s = "()(())((()()))"
        output = 3
        self.assertEqual(self.sol.maxDepth(s), output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
