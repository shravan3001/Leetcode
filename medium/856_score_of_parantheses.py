"""
https://leetcode.com/problems/score-of-parentheses/description/?envType=daily-question&envId=2026-10-05
856. Score of Parentheses

Given a balanced parentheses string s, return the score of the string.
The score of a balanced parentheses string is based on the following rule:
    "()" has score 1.
    AB has score A + B, where A and B are balanced parentheses strings.
    (A) has score 2 * A, where A is a balanced parentheses string.

Example 1:
Input: s = "()"
Output: 1

Example 2:
Input: s = "(())"
Output: 2

Example 3:
Input: s = "()()"
Output: 2

Constraints:
    2 <= s.length <= 50
    s consists of only '(' and ')'.
    s is a balanced parentheses string.
"""

import unittest


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack: list[int] = [0]  # running score at each nesting depth
        for c in s:
            if c == "(":
                stack.append(0)
            else:
                inner = stack.pop()
                stack[-1] += max(2 * inner, 1)
        return stack[0]


class TestScoreOfParantheses(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        s = "()"
        output = 1
        self.assertEqual(self.sol.scoreOfParentheses(s), output)

    def test_example_2(self):
        s = "(())"
        output = 2
        self.assertEqual(self.sol.scoreOfParentheses(s), output)

    def test_example_3(self):
        s = "()()"
        output = 2
        self.assertEqual(self.sol.scoreOfParentheses(s), output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
