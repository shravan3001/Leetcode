"""
https://leetcode.com/problems/remove-outermost-parentheses/description/?envType=daily-question&envId=2026-10-08
1021. Remove Outermost Parentheses

A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.
    For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.
Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.
Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

Example 1:
Input: s = "(()())(())"
Output: "()()()"
Explanation:
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

Example 2:
Input: s = "(()())(())(()(()))"
Output: "()()()()(())"
Explanation:
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".

Example 3:
Input: s = "()()"
Output: ""
Explanation:
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".

Constraints:
    1 <= s.length <= 1e5
    s[i] is either '(' or ')'.
    s is a valid parentheses string.
"""

import unittest


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans: list[str] = []
        depth = 0
        for c in s:
            if c == "(":
                depth += 1
                if depth > 1:
                    ans.append(c)
            else:
                depth -= 1
                if depth >= 1:
                    ans.append(c)
        return "".join(ans)


class TestRemoveOuterParantheses(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        s = "(()())(())"
        output = "()()()"
        self.assertEqual(self.sol.removeOuterParentheses(s), output)

    def test_example_2(self):
        s = "(()())(())(()(()))"
        output = "()()()()(())"
        self.assertEqual(self.sol.removeOuterParentheses(s), output)

    def test_example_3(self):
        s = "()()"
        output = ""
        self.assertEqual(self.sol.removeOuterParentheses(s), output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
