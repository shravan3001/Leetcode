"""
https://leetcode.com/problems/count-commas-in-range/description/?envType=daily-question&envId=2026-09-08
3870. Count Commas in Range

You are given an integer n.
Return the total number of commas used when writing all integers from [1, n] (inclusive) in standard number formatting.
In standard formatting:
    A comma is inserted after every three digits from the right.
    Numbers with fewer than 4 digits contain no commas.

Example 1:
Input: n = 1002
Output: 3
Explanation:
The numbers "1,000", "1,001", and "1,002" each contain one comma, giving a total of 3.

Example 2:
Input: n = 998
Output: 0
Explanation:
All numbers from 1 to 998 have fewer than four digits. Therefore, no commas are used.

Constraints:
    1 <= n <= 105
"""

import unittest


class Solution:
    def countCommas(self, n: int) -> int:
        if n <= 999:
            return 0
        elif n <= 999_000:
            return n - 1000 + 1
        return 0


class TestCountCommas(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        n = 1002
        output = 3
        self.assertEqual(self.sol.countCommas(n), output)

    def test_example_2(self):
        n = 998
        output = 0
        self.assertEqual(self.sol.countCommas(n), output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
