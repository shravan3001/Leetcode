"""
https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target/description/?envType=daily-question&envId=2026-08-27
3720. Lexicographically Smallest Permutation Greater Than Target

You are given two strings s and target, both having length n, consisting of lowercase English letters.
Return the lexicographically smallest of s that is strictly greater than target. If no permutation of s is lexicographically strictly greater than target, return an empty string.
A string a is lexicographically strictly greater than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b.

Example 1:
Input: s = "abc", target = "bba"
Output: "bca"
Explanation:
    The permutations of s (in lexicographical order) are "abc", "acb", "bac", "bca", "cab", and "cba".
    The lexicographically smallest permutation that is strictly greater than target is "bca".

Example 2:
Input: s = "leet", target = "code"
Output: "eelt"
Explanation:
    The permutations of s (in lexicographical order) are "eelt", "eetl", "elet", "elte", "etel", "etle", "leet", "lete", "ltee", "teel", "tele", and "tlee".
    The lexicographically smallest permutation that is strictly greater than target is "eelt".

Example 3:
Input: s = "baba", target = "bbaa"
Output: ""
Explanation:
    The permutations of s (in lexicographical order) are "aabb", "abab", "abba", "baab", "baba", and "bbaa".
    None of them is lexicographically strictly greater than target. Therefore, the answer is "".

Constraints:

    1 <= s.length == target.length <= 300
    s and target consist of only lowercase English letters.

Hint 1
Maintain frequency counts of s.
Hint 2
Walk left-to-right; if equal to target[i] is possible, take it and continue.
Hint 3
If not, try the smallest letter strictly greater than target[i].
Hint 4
If neither, backtrack left to the most recent index where you matched target and try to bump there.
"""

from typing import Counter
import unittest


class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        base_cnts = Counter(s)

        # Find the maximum prefix length for which s's multiset can supply
        # target[0:k] exactly.
        temp = Counter(base_cnts)
        max_k = 0
        for i in range(n):
            c = target[i]
            if temp[c] > 0:
                temp[c] -= 1
                max_k = i + 1
            else:
                break

        # Try longest matching prefix first (down to 0), since matching as
        # much of target as possible before diverging upward yields the
        # smallest possible result that's still > target.
        for k in range(max_k, -1, -1):
            if k == n:
                # s would equal target exactly - not strictly greater.
                continue

            # Counts remaining after using target[0:k] as the prefix.
            cur = Counter(base_cnts)
            valid = True
            for i in range(k):
                cur[target[i]] -= 1
                if cur[target[i]] < 0:
                    valid = False
                    break
            if not valid:
                continue

            # Find smallest available letter strictly greater than target[k].
            found = None
            for ch in sorted(cur.keys()):
                if cur[ch] > 0 and ch > target[k]:
                    found = ch
                    break

            if found is not None:
                cur[found] -= 1
                remaining_letters = []
                for ch in sorted(cur.keys()):
                    remaining_letters.extend([ch] * cur[ch])
                return target[:k] + found + "".join(remaining_letters)

        return ""


class TestLexGreaterPermutation(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        s = "abc"
        target = "bba"
        self.assertEqual(self.sol.lexGreaterPermutation(s, target), "bca")

    def test_example_2(self):
        s = "leet"
        target = "code"
        self.assertEqual(self.sol.lexGreaterPermutation(s, target), "eelt")

    def test_example_3(self):
        s = "baba"
        target = "bbaa"
        self.assertEqual(self.sol.lexGreaterPermutation(s, target), "")

    def test_example_4(self):
        s = "ab"
        target = "ab"
        self.assertEqual(self.sol.lexGreaterPermutation(s, target), "ba")


if __name__ == "__main__":
    unittest.main(verbosity=2)
