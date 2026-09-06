"""
https://leetcode.com/problems/distinct-subsequences/description/?envType=daily-question&envId=2026-09-06
115. Distinct Subsequences

Given two strings s and t, return the number of distinct subsequences of s which equals t.
The test cases are generated so that the answer fits on a 32-bit signed integer.

Example 1:
Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
rabbbit
rabbbit

Example 2:
Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from s.
babgbag
babgbag
babgbag
babgbag
babgbag

Constraints:
    1 <= s.length, t.length <= 1000
    s and t consist of English letters.
"""

import unittest


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        sn = len(s)
        tn = len(t)
        dp = [[-1] * tn for _ in range(sn)]

        def solve(si: int, ti: int) -> int:
            if ti == tn:
                return 1
            if sn - si < tn - ti or si == sn:
                return 0
            if dp[si][ti] != -1:
                return dp[si][ti]
            skip = solve(si + 1, ti)
            take = solve(si + 1, ti + 1) if s[si] == t[ti] else 0
            dp[si][ti] = skip + take
            return dp[si][ti]

        return solve(0, 0)


class TestNumDistict(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        s = "rabbbit"
        t = "rabbit"
        output = 3
        self.assertEqual(self.sol.numDistinct(s, t), output)

    def test_example_2(self):
        s = "babgbag"
        t = "bag"
        output = 5
        self.assertEqual(self.sol.numDistinct(s, t), output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
