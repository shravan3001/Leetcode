"""
https://leetcode.com/problems/lexicographically-smallest-palindromic-permutation-greater-than-target/description/?envType=daily-question&envId=2026-08-28
3734. Lexicographically Smallest Palindromic Permutation Greater Than Target

You are given two strings s and target, each of length n, consisting of lowercase English letters.
Return the string that is both a of s and strictly greater than target. If no such permutation exists, return an empty string.

Example 1:
Input: s = "baba", target = "abba"
Output: "baab"
Explanation:
    The palindromic permutations of s (in lexicographical order) are "abba" and "baab".
    The lexicographically smallest permutation that is strictly greater than target is "baab".

Example 2:
Input: s = "baba", target = "bbaa"
Output: ""
Explanation:
    The palindromic permutations of s (in lexicographical order) are "abba" and "baab".
    None of them is lexicographically strictly greater than target. Therefore, the answer is "".

Example 3:
Input: s = "abc", target = "abb"
Output: ""
Explanation:
s has no palindromic permutations. Therefore, the answer is "".

Example 4:
Input: s = "aac", target = "abb"
Output: "aca"
Explanation:
    The only palindromic permutation of s is "aca".
    "aca" is strictly greater than target. Therefore, the answer is "aca".

Constraints:

    1 <= n == s.length == target.length <= 300
    s and target consist of only lowercase English letters.

Hint 1
A palindromic permutation exists only if at most one character has an odd count (for odd-length strings) or all counts are even (for even-length strings).
Hint 2
Focus on constructing the first half of the palindrome. The second half is determined by mirroring.
Hint 3
To be lexicographically greater than target, the first half must be greater than or equal to target's first half, with careful handling of the middle character for odd-length strings.
Hint 4
Use a backtracking approach or greedy selection for each position in the first half, trying the smallest available character that can still produce a valid palindrome.
Hint 5
After building the first half, mirror it (and add the middle character if needed) to form the full palindrome and verify it is strictly greater than target.
"""

import unittest
import string
from collections import Counter


class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = Counter(s)
        odd_chars = [c for c in cnt if cnt[c] % 2 == 1]

        if n % 2 == 0:
            if odd_chars:
                return ""
            mid_char = None
        else:
            if len(odd_chars) != 1:
                return ""
            mid_char = odd_chars[0]

        m = n // 2
        half_counts = {c: cnt[c] // 2 for c in cnt}
        target_half = target[:m]

        # ---------- Case B: try h == target_half exactly ----------
        thc = Counter(target_half)
        case_b_feasible = all(thc[c] <= half_counts.get(c, 0) for c in thc)
        if case_b_feasible:
            h = target_half
            rev = h[::-1]
            full = h + mid_char + rev if n % 2 == 1 else h + rev
            if full > target:
                return full

        # ---------- Case A: find smallest h > target_half from multiset ----------
        charset = string.ascii_lowercase
        prefix_counts = dict(half_counts)

        best_i = -1
        best_char = None
        best_counts_at_i = None
        feasible_prefix = True

        for i in range(m):
            if not feasible_prefix:
                break
            ti = target_half[i]

            candidates = [c for c in charset if c > ti and prefix_counts.get(c, 0) > 0]
            if candidates:
                c = min(candidates)
                best_i = i
                best_char = c
                best_counts_at_i = dict(prefix_counts)

            if prefix_counts.get(ti, 0) > 0:
                prefix_counts[ti] -= 1
            else:
                feasible_prefix = False

        if best_i == -1:
            return ""

        h_list = list(target_half[:best_i]) + [best_char]
        rem_counts = dict(best_counts_at_i)
        rem_counts[best_char] -= 1

        tail_chars = []
        for c in charset:
            tail_chars.extend([c] * rem_counts.get(c, 0))
        h_list.extend(tail_chars)

        h = "".join(h_list)
        rev = h[::-1]
        full = h + mid_char + rev if n % 2 == 1 else h + rev
        return full


class TestLexPalindromicPermutation(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        s = "baba"
        t = "abba"
        self.assertEqual(self.sol.lexPalindromicPermutation(s, t), "baab")

    def test_example_2(self):
        s = "baba"
        t = "baab"
        self.assertEqual(self.sol.lexPalindromicPermutation(s, t), "")

    def test_example_3(self):
        s = "abc"
        t = "abb"
        self.assertEqual(self.sol.lexPalindromicPermutation(s, t), "")


if __name__ == "__main__":
    unittest.main(verbosity=2)
