"""
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/?envType=daily-question&envId=2026-10-06
921. Minimum Add to Make Parentheses Valid

A parentheses string is valid if and only if:
    It is the empty string,
    It can be written as AB (A concatenated with B), where A and B are valid strings, or
    It can be written as (A), where A is a valid string.
You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.
    For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.

Example 1:
Input: s = "())"
Output: 1

Example 2:
Input: s = "((("
Output: 3

Constraints:
    1 <= s.length <= 1000
    s[i] is either '(' or ')'.
"""

import unittest


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_count = 0
        ans = 0
        for c in s:
            if c == "(":
                open_count += 1
            else:
                open_count -= 1
            if open_count < 0:
                ans += 1
                open_count += 1
        ans += open_count
        return ans


class TestMinAddToMakeValid(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        s = "())"
        output = 1
        self.assertEqual(self.sol.minAddToMakeValid(s), output)

    def test_example_2(self):
        s = "((("
        output = 3
        self.assertEqual(self.sol.minAddToMakeValid(s), output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
