"""
https://leetcode.com/problems/minimum-operations-to-sort-a-string/description/?envType=daily-question&envId=2026-10-21
3863. Minimum Operations to Sort a String

You are given a string s consisting of lowercase English letters.
In one operation, you can select any substring of s that is not the entire string and sort it in non-descending alphabetical order.
Return the minimum number of operations required to make s sorted in non-descending order. If it is not possible, return -1.

Example 1:
Input: s = "dog"
Output: 1
Explanation:
    Sort substring "og" to "go".
    Now, s = "dgo", which is sorted in ascending order. Thus, the answer is 1.

Example 2:
Input: s = "card"
Output: 2
Explanation:
    Sort substring "car" to "acr", so s = "acrd".
    Sort substring "rd" to "dr", making s = "acdr", which is sorted in ascending order. Thus, the answer is 2.

Example 3:
Input: s = "gf"
Output: -1
Explanation:
    It is impossible to sort s under the given constraints. Thus, the answer is -1.

Constraints:
    1 <= s.length <= 1e5
    s consists of only lowercase English letters.
"""

import unittest


class Solution:
    def minOperations(self, s: str) -> int:
        mni, mxi = 0, 0
        n = len(s)
        is_sorted = True
        for i in range(1, n):
            if s[i] < s[i - 1]:
                is_sorted = False
            if s[i] < s[mni]:
                mni = i
            if s[i] >= s[mxi]:
                mxi = i
        if is_sorted:
            return 0
        if n == 2:
            return -1
        if mni == 0 and mxi == n - 1:
            return 1
        if mni == 0 or mxi == n - 1:
            return 1
        if mni == n - 1 and mxi == 0:
            return 3
        return 2


class TestMinOperations(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        s, output = "dog", 1
        self.assertEqual(self.sol.minOperations(s), output)

    def test_example_2(self):
        s, output = "card", 2
        self.assertEqual(self.sol.minOperations(s), output)

    def test_example_3(self):
        s, output = "gf", -1
        self.assertEqual(self.sol.minOperations(s), output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
