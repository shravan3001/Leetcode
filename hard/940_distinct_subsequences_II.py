"""
https://leetcode.com/problems/distinct-subsequences-ii/description/?envType=daily-question&envId=2026-09-07
940. Distinct Subsequences II

Given a string s, return the number of distinct non-empty subsequences of s. Since the answer may be very large, return it modulo 109 + 7.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not.

Example 1:
Input: s = "abc"
Output: 7
Explanation: The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc", and "abc".

Example 2:
Input: s = "aba"
Output: 6
Explanation: The 6 distinct subsequences are "a", "b", "ab", "aa", "ba", and "aba".

Example 3:
Input: s = "aaa"
Output: 3
Explanation: The 3 distinct subsequences are "a", "aa" and "aaa".

Constraints:
    1 <= s.length <= 2000
    s consists of lowercase English letters.
"""

import unittest

MODN = 10**9 + 7


class Solution:
    def distinctSubseqII(self, s: str) -> int:
        n = len(s)

        dp = [0] * (n + 1)
        dp[0] = 1

        last = [-1] * 26

        for i in range(1, n + 1):
            dp[i] = (2 * dp[i - 1]) % MODN

            idx = ord(s[i - 1]) - ord("a")
            if last[idx] != -1:
                dp[i] = (dp[i] - dp[last[idx]] + MODN) % MODN

            last[idx] = i - 1

        return (dp[n] - 1) % MODN


class TestDistinctSubseqII(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        s = "abc"
        output = 7
        self.assertEqual(self.sol.distinctSubseqII(s), output)

    def test_example_2(self):
        s = "aba"
        output = 6
        self.assertEqual(self.sol.distinctSubseqII(s), output)

    def test_example_3(self):
        s = "aaa"
        output = 3
        self.assertEqual(self.sol.distinctSubseqII(s), output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
