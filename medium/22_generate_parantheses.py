"""
https://leetcode.com/problems/generate-parentheses/description/?envType=daily-question&envId=2026-10-02
22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Constraints:
    1 <= n <= 8
"""

import unittest


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans: list[str] = []
        curr: list[str] = []
        max_length = 2 * n

        def generate(open_cnt: int, close_cnt: int) -> None:
            if len(curr) == max_length:
                ans.append("".join(curr))
                return
            if open_cnt < n:
                curr.append("(")
                generate(open_cnt + 1, close_cnt)
                curr.pop()
            if close_cnt < open_cnt:
                curr.append(")")
                generate(open_cnt, close_cnt + 1)
                curr.pop()

        generate(0, 0)
        return ans


class TestGenerateParantheses(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        n = 3
        output = ["((()))", "(()())", "(())()", "()(())", "()()()"]
        self.assertEqual(set(self.sol.generateParenthesis(n)), set(output))

    def test_example_2(self):
        n = 1
        output = ["()"]
        self.assertEqual(set(self.sol.generateParenthesis(n)), set(output))


if __name__ == "__main__":
    unittest.main(verbosity=2)
