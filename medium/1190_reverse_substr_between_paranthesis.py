"""
https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/description/?envType=daily-question&envId=2026-09-27
1190. Reverse Substrings Between Each Pair of Parentheses

You are given a string s that consists of lower case English letters and brackets.
Reverse the strings in each pair of matching parentheses, starting from the innermost one.
Your result should not contain any brackets.

Example 1:
Input: s = "(abcd)"
Output: "dcba"

Example 2:
Input: s = "(u(love)i)"
Output: "iloveu"
Explanation: The substring "love" is reversed first, then the whole string is reversed.

Example 3:
Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.

Constraints:
    1 <= s.length <= 2000
    s only contains lower case English characters and parentheses.
    It is guaranteed that all parentheses are balanced.
"""

import unittest


class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack: list[str] = []
        rev_list: list[str] = []
        for c in s:
            if c == ")":
                rev_list.clear()
                while (revc := stack.pop()) != "(":
                    rev_list.append(revc)
                stack.extend(rev_list)
            else:
                stack.append(c)

        return "".join(stack)


class TestReverseParanthesis(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        s = "(abcd)"
        output = "dcba"
        self.assertEqual(self.sol.reverseParentheses(s), output)

    def test_example_2(self):
        s = "(u(love)i)"
        output = "iloveu"
        self.assertEqual(self.sol.reverseParentheses(s), output)

    def test_example_3(self):
        s = "(ed(et(oc))el)"
        output = "leetcode"
        self.assertEqual(self.sol.reverseParentheses(s), output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
