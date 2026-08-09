"""
https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/description/?envType=daily-question&envId=2026-08-08
3302. Find the Lexicographically Smallest Valid Sequence

You are given two strings word1 and word2.

A string x is called almost equal to y if you can change at most one character in x to make it identical to y.

A sequence of indices seq is called valid if:

    The indices are sorted in ascending order.
    Concatenating the characters at these indices in word1 in the same order results in a string that is almost equal to word2.

Return an array of size word2.length representing the valid sequence of indices. If no such sequence of indices exists, return an empty array.

Note that the answer must represent the lexicographically smallest array, not the corresponding string formed by those indices.

Example 1:
Input: word1 = "vbcca", word2 = "abc"
Output: [0,1,2]
Explanation:
The lexicographically smallest valid sequence of indices is [0, 1, 2]:
    Change word1[0] to 'a'.
    word1[1] is already 'b'.
    word1[2] is already 'c'.

Example 2:
Input: word1 = "bacdc", word2 = "abc"
Output: [1,2,4]
Explanation:
The lexicographically smallest valid sequence of indices is [1, 2, 4]:
    word1[1] is already 'a'.
    Change word1[2] to 'b'.
    word1[4] is already 'c'.

Example 3:
Input: word1 = "aaaaaa", word2 = "aaabc"
Output: []
Explanation:
There is no valid sequence of indices.

Example 4:
Input: word1 = "abc", word2 = "ab"
Output: [0,1]

Constraints:
    1 <= word2.length < word1.length <= 3 * 105
    word1 and word2 consist only of lowercase English letters.
"""

import unittest
from typing import List


class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n1, m = len(word1), len(word2)

        # dp[i] = longest suffix of word2 that is an EXACT subsequence of word1[i:]
        dp = [0] * (n1 + 1)
        # g[i]  = longest suffix of word2 matchable from word1[i:] with AT MOST 1 substitution
        g = [0] * (n1 + 1)

        for i in range(n1 - 1, -1, -1):
            # dp[i]: extend dp[i+1] by one if word1[i] matches the next needed char
            if dp[i + 1] < m and word1[i] == word2[m - dp[i + 1] - 1]:
                dp[i] = dp[i + 1] + 1
            else:
                dp[i] = dp[i + 1]

            # g[i]: best of three options
            best = g[i + 1]  # skip word1[i] entirely
            if dp[i + 1] < m:
                best = max(
                    best, dp[i + 1] + 1
                )  # spend the substitution HERE, extending an exact match
            if g[i + 1] < m and word1[i] == word2[m - g[i + 1] - 1]:
                best = max(
                    best, g[i + 1] + 1
                )  # extend an already-substituted match exactly
            g[i] = best

        ans = []
        i, budget = 0, 1  # i = pointer into word1, budget = changes left (0 or 1)
        for j in range(m):
            need = m - j - 1  # length still required after this pick
            p = i
            chosen = -1
            while p < n1:
                if word1[p] == word2[j]:
                    ok = (g[p + 1] >= need) if budget == 1 else (dp[p + 1] >= need)
                    if ok:
                        chosen = p
                        break
                elif budget >= 1 and dp[p + 1] >= need:
                    chosen = p
                    break
                p += 1
            if chosen == -1:
                return []
            ans.append(chosen)
            if word1[chosen] != word2[j]:
                budget -= 1
            i = chosen + 1
        return ans


class TestValidSequence(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        w1 = "vbcca"
        w2 = "abc"
        self.assertEqual(self.sol.validSequence(w1, w2), [0, 1, 2])

    def test_example_2(self):
        w1 = "bacdc"
        w2 = "abc"
        self.assertEqual(self.sol.validSequence(w1, w2), [1, 2, 4])

    def test_example_3(self):
        w1 = "aaaaaa"
        w2 = "aaabc"
        self.assertEqual(self.sol.validSequence(w1, w2), [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
