"""
https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/description/?envType=daily-question&envId=2026-10-09
1541. Minimum Insertions to Balance a Parentheses String

Given a parentheses string s containing only the characters '(' and ')'. A parentheses string is balanced if:
    Any left parenthesis '(' must have a corresponding two consecutive right parenthesis '))'.
    Left parenthesis '(' must go before the corresponding two consecutive right parenthesis '))'.
In other words, we treat '(' as an opening parenthesis and '))' as a closing parenthesis.
    For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))" and "(()))" are not balanced.
You can insert the characters '(' and ')' at any position of the string to balance it if needed.
Return the minimum number of insertions needed to make s balanced.

Example 1:
Input: s = "(()))"
Output: 1
Explanation: The second '(' has two matching '))', but the first '(' has only ')' matching. We need to add one more ')' at the end of the string to be "(())))" which is balanced.

Example 2:
Input: s = "())"
Output: 0
Explanation: The string is already balanced.

Example 3:
Input: s = "))())("
Output: 3
Explanation: Add '(' to match the first '))', Add '))' to match the last '('.

Constraints:
    1 <= s.length <= 105
    s consists of '(' and ')' only.
"""

import unittest


class Solution:
    def minInsertions(self, s: str) -> int:
        ans = 0
        depth = 0
        i, n = 0, len(s)
        while i < n:
            if s[i] == "(":
                depth += 1
            else:
                depth -= 1
                if depth < 0:
                    depth = 0
                    ans += 1
                if i + 1 < n:
                    if s[i + 1] == ")":
                        i += 1
                    else:
                        ans += 1
                else:
                    ans += 1
            i += 1
        ans += depth * 2
        return ans


class TestMinInsertions(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        s = "(()))"
        output = 1
        self.assertEqual(self.sol.minInsertions(s), output)

    def test_example_2(self):
        s = "())"
        output = 0
        self.assertEqual(self.sol.minInsertions(s), output)

    def test_example_3(self):
        s = "))())("
        output = 3
        self.assertEqual(self.sol.minInsertions(s), output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
