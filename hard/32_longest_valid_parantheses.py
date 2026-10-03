"""
https://leetcode.com/problems/longest-valid-parentheses/description/?envType=daily-question&envId=2026-10-03
32. Longest Valid Parentheses

Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:
Input: s = ""
Output: 0

Constraints:
    0 <= s.length <= 3 * 1e4
    s[i] is '(', or ')'.
"""

import unittest


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = 0

        # Left -> right: catches stray ')'
        opened = closed = 0
        for ch in s:
            if ch == "(":
                opened += 1
            else:
                closed += 1
            if opened == closed:
                ans = max(ans, 2 * closed)
            elif closed > opened:
                opened = closed = 0

        # Right -> left: catches stray '('
        opened = closed = 0
        for ch in reversed(s):
            if ch == "(":
                opened += 1
            else:
                closed += 1
            if opened == closed:
                ans = max(ans, 2 * opened)
            elif opened > closed:
                opened = closed = 0

        return ans

        # stack approach
        # stack = [-1]
        # max_len = 0
        #
        # for i, c in enumerate(s):
        #     if c == '(':
        #         stack.append(i)
        #     else:
        #         stack.pop()
        #
        #         if not stack:
        #             stack.append(i)
        #         else:
        #             max_len = max(max_len, i - stack[-1])
        #
        # return max_len

        # dp approach
        # n = len(s)
        # dp = [0] * n
        # ans = 0
        # for i in range(1, n):
        #     if s[i] != ")":
        #         continue
        #     if s[i - 1] == "(":
        #         dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
        #     else:
        #         j = i - dp[i - 1] - 1
        #         if j >= 0 and s[j] == "(":
        #             dp[i] = dp[i - 1] + 2 + (dp[j - 1] if j >= 1 else 0)
        #     ans = max(ans, dp[i])
        # return ans


class TestLongestValidParantheses(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        s = "(()"
        output = 2
        self.assertEqual(self.sol.longestValidParentheses(s), output)

    def test_example_2(self):
        s = ")()())"
        output = 4
        self.assertEqual(self.sol.longestValidParentheses(s), output)

    def test_example_3(self):
        s = ""
        output = 0
        self.assertEqual(self.sol.longestValidParentheses(s), output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
