"""
https://leetcode.com/problems/valid-parenthesis-string/description/?envType=daily-question&envId=2026-10-04
678. Valid Parenthesis String

Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
The following rules define a valid string:
    Any left parenthesis '(' must have a corresponding right parenthesis ')'.
    Any right parenthesis ')' must have a corresponding left parenthesis '('.
    Left parenthesis '(' must go before the corresponding right parenthesis ')'.
    '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "(*)"
Output: true

Example 3:
Input: s = "(*))"
Output: true

Example 4:
Input: s = "("
Output: false

Constraints:
    1 <= s.length <= 100
    s[i] is '(', ')' or '*'.

Hint 1
Use backtracking to explore all possible combinations of treating '*' as either '(', ')', or an empty string. If any combination leads to a valid string, return true.
Hint 2
DP[i][j] represents whether the substring s[i:j] is valid.
Hint 3
Keep track of the count of open parentheses encountered so far. If you encounter a close parenthesis, it should balance with an open parenthesis. Utilize a stack to handle this effectively.
Hint 4
How about using 2 stacks instead of 1? Think about it.
"""

import unittest


class Solution:
    def checkValidString(self, s: str) -> bool:
        lo = hi = 0  # min / max possible number of unmatched '('
        for c in s:
            if c == "(":
                lo += 1
                hi += 1
            elif c == ")":
                lo -= 1
                hi -= 1
            else:  # '*' can be '(', ')' or ''
                lo -= 1
                hi += 1

            if hi < 0:  # too many ')' even if every '*' were '('
                return False
            lo = max(lo, 0)  # can't have negative open count

        return lo == 0  # some assignment closes everything


class TestCheckValidString(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        s = "()"
        output = True
        self.assertEqual(self.sol.checkValidString(s), output)

    def test_example_2(self):
        s = "(*)"
        output = True
        self.assertEqual(self.sol.checkValidString(s), output)

    def test_example_3(self):
        s = "(*))"
        output = True
        self.assertEqual(self.sol.checkValidString(s), output)

    def test_example_4(self):
        s = "("
        output = False
        self.assertEqual(self.sol.checkValidString(s), output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
