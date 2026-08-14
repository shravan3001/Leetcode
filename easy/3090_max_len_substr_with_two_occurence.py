"""
https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/description/?envType=daily-question&envId=2026-08-14

3090. Maximum Length Substring With Two Occurrences
Given a string s, return the maximum length of a  such that it contains at most two occurrences of each character.

Example 1:
Input: s = "bcbbbcba"
Output: 4
Explanation:
The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".

Example 2:
Input: s = "aaaa"
Output: 2
Explanation:
The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".

Constraints:
    2 <= s.length <= 100
    s consists only of lowercase English letters.
"""

import unittest
from collections import defaultdict


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        cache = defaultdict(int)
        l = 0
        n = len(s)
        ans = 0
        for r in range(n):
            if cache[s[r]] == 2:
                while l < r and s[l] != s[r]:
                    cache[s[l]] -= 1
                    l += 1
                if s[l] == s[r]:
                    cache[s[l]] -= 1
                    l += 1
            cache[s[r]] += 1
            if ans < r - l + 1:
                ans = r - l + 1
        return ans


class TestMaximumLengthSubstring(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        s = "bcbbbcba"
        self.assertEqual(self.sol.maximumLengthSubstring(s), 4)

    def test_example_2(self):
        s = "aaaa"
        self.assertEqual(self.sol.maximumLengthSubstring(s), 2)

    def test_example_3(self):
        s = "bbbab"
        self.assertEqual(self.sol.maximumLengthSubstring(s), 3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
