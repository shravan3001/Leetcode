"""
https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/description/?envType=daily-question&envId=2026-09-18
1520. Maximum Number of Non-Overlapping Substrings

Given a string s of lowercase letters, you need to find the maximum number of non-empty substrings of s that meet the following conditions:
    The substrings do not overlap, that is for any two substrings s[i..j] and s[x..y], either j < x or i > y is true.
    A substring that contains a certain character c must also contain all occurrences of c.
Find the maximum number of substrings that meet the above conditions. If there are multiple solutions with the same number of substrings, return the one with minimum total length. It can be shown that there exists a unique solution of minimum total length.
Notice that you can return the substrings in any order.

Example 1:
Input: s = "adefaddaccc"
Output: ["e","f","ccc"]
Explanation: The following are all the possible substrings that meet the conditions:
[
  "adefaddaccc"
  "adefadda",
  "ef",
  "e",
  "f",
  "ccc",
]
If we choose the first string, we cannot choose anything else and we'd get only 1. If we choose "adefadda", we are left with "ccc" which is the only one that doesn't overlap, thus obtaining 2 substrings. Notice also, that it's not optimal to choose "ef" since it can be split into two. Therefore, the optimal way is to choose ["e","f","ccc"] which gives us 3 substrings. No other solution of the same number of substrings exist.

Example 2:
Input: s = "abbaccd"
Output: ["d","bb","cc"]
Explanation: Notice that while the set of substrings ["d","abba","cc"] also has length 3, it's considered incorrect since it has larger total length.

Constraints:
    1 <= s.length <= 1e5
    s contains only lowercase English letters.

Hint 1
Notice that it's impossible for any two valid substrings to overlap unless one is inside another.
Hint 2
We can start by finding the starting and ending index for each character.
Hint 3
From these indices, we can form the substrings by expanding each character's range if necessary (if another character exists in the range with smaller/larger starting/ending index).
Hint 4
Sort the valid substrings by length and greedily take those with the smallest length, discarding the ones that overlap those we took.
"""

import unittest


class Solution:
    def getFirstAndLast(self, s: str) -> tuple[list[int], list[int]]:
        firsts = [-1] * 26
        lasts = [-1] * 26

        for i, c in enumerate(s):
            idx = ord(c) - ord("a")
            lasts[idx] = i
            if firsts[idx] == -1:
                firsts[idx] = i
        return firsts, lasts

    def maxNumOfSubstrings(self, s: str) -> list[str]:
        firsts, lasts = self.getFirstAndLast(s)

        # Build one candidate range per character, expanded until closed.
        candidates: list[tuple[int, int]] = []
        for c in range(26):
            if firsts[c] == -1:
                continue

            left, right = firsts[c], lasts[c]
            valid = True
            i = left
            while i <= right:
                idx = ord(s[i]) - ord("a")
                # A char inside the range starts before it: the range would have
                # to extend left, and that wider range is another char's candidate.
                if firsts[idx] < left:
                    valid = False
                    break
                right = max(right, lasts[idx])
                i += 1

            if valid:
                candidates.append((left, right))

        # Valid ranges are either nested or disjoint, so greedily taking the
        # shortest ones that don't overlap what we already have is optimal.
        candidates.sort(key=lambda r: (r[1] - r[0], r[0]))

        chosen: list[tuple[int, int]] = []
        for left, right in candidates:
            if all(right < l or left > r for l, r in chosen):
                chosen.append((left, right))

        return [s[l : r + 1] for l, r in chosen]


class TestMaxNumOfSubstrings(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        s = "adefaddaccc"
        output = ["e", "f", "ccc"]
        self.assertEqual(self.sol.maxNumOfSubstrings(s), output)

    def test_example_2(self):
        s = "abbaccd"
        output = ["d", "bb", "cc"]
        self.assertEqual(self.sol.maxNumOfSubstrings(s), output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
