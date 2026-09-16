"""
https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/description/?envType=daily-question&envId=2026-09-16
1621. Number of Sets of K Non-Overlapping Line Segments

Given n points on a 1-D plane, where the ith point (from 0 to n-1) is at x = i, find the number of ways we can draw exactly k non-overlapping line segments such that each segment covers two or more points. The endpoints of each segment must have integral coordinates. The k line segments do not have to cover all n points, and they are allowed to share endpoints.
Return the number of ways we can draw k non-overlapping line segments. Since this number can be huge, return it modulo 109 + 7.

Example 1:
Input: n = 4, k = 2
Output: 5
Explanation: The two line segments are shown in red and blue.
The image above shows the 5 different ways {(0,2),(2,3)}, {(0,1),(1,3)}, {(0,1),(2,3)}, {(1,2),(2,3)}, {(0,1),(1,2)}.

Example 2:
Input: n = 3, k = 1
Output: 3
Explanation: The 3 ways are {(0,1)}, {(0,2)}, {(1,2)}.

Example 3:
Input: n = 30, k = 7
Output: 796297179
Explanation: The total number of possible ways to draw 7 line segments is 3796297200. Taking this number modulo 109 + 7 gives us 796297179.

Constraints:
    2 <= n <= 1000
    1 <= k <= n-1
"""

import unittest

MODN = 10**9 + 7


class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        # answer = C(n+k-1, 2k) mod 1e9+7
        top = n + k - 1
        bottom = 2 * k
        if bottom > top:
            return 0
        num = 1
        for i in range(bottom):
            num = num * (top - i) % MODN
        den = 1
        for i in range(1, bottom + 1):
            den = den * i % MODN
        return num * pow(den, MODN - 2, MODN) % MODN


class TestNumberOfSets(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        n, k = 4, 2
        output = 5
        self.assertEqual(self.sol.numberOfSets(n, k), output)

    def test_example_2(self):
        n, k = 3, 1
        output = 3
        self.assertEqual(self.sol.numberOfSets(n, k), output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
