"""
https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/description/?envType=daily-question&envId=2026-09-15
2472. Maximum Number of Non-overlapping Palindrome Substrings

You are given a string s and a positive integer k.
Select a set of non-overlapping substrings from the string s that satisfy the following conditions:
    The length of each substring is at least k.
    Each substring is a palindrome.
Return the maximum number of substrings in an optimal selection.
A substring is a contiguous sequence of characters within a string.

Example 1:
Input: s = "abaccdbbd", k = 3
Output: 2
Explanation: We can select the substrings underlined in s = "abaccdbbd". Both "aba" and "dbbd" are palindromes and have a length of at least k = 3.
It can be shown that we cannot find a selection with more than two valid substrings.

Example 2:
Input: s = "adbcda", k = 2
Output: 0
Explanation: There is no palindrome substring of length at least 2 in the string.

Constraints:
    1 <= k <= s.length <= 2000
    s consists of lowercase English letters.

Hint 1
Try to use dynamic programming to solve the problem.
Hint 2
let dp[i] be the answer for the prefix s[0…i].
Hint 3
The final answer to the problem will be dp[n-1]. How do you compute this dp?
"""

import unittest


class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        if n < k:
            return 0

        # pal[l][r] = True if s[l..r] is a palindrome
        pal = [[False] * n for _ in range(n)]
        for r in range(n):
            for l in range(r, -1, -1):
                if s[l] == s[r] and (r - l < 2 or pal[l + 1][r - 1]):
                    pal[l][r] = True

        dp = [0] * (n + 1)
        for i in range(n):
            dp[i + 1] = dp[i]  # option: skip position i
            for length in (k, k + 1):
                l = i - length + 1
                if l >= 0 and pal[l][i]:
                    dp[i + 1] = max(dp[i + 1], dp[l] + 1)
                    break  # shorter valid palindrome is always at least as good
        return dp[n]


class TestMaxPalindrome(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        s = "abaccdbbd"
        k = 3
        output = 2
        self.assertEqual(self.sol.maxPalindromes(s, k), output)

    def test_example_2(self):
        s = "adbcda"
        k = 2
        output = 0
        self.assertEqual(self.sol.maxPalindromes(s, k), output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
