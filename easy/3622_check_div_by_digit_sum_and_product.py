"""
https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/description/?envType=daily-question&envId=2026-08-22
3622. Check Divisibility by Digit Sum and Product

You are given a positive integer n. Determine whether n is divisible by the sum of the following two values:
    The digit sum of n (the sum of its digits).
    The digit product of n (the product of its digits).
Return true if n is divisible by this sum; otherwise, return false.

Example 1:
Input: n = 99
Output: true
Explanation:
Since 99 is divisible by the sum (9 + 9 = 18) plus product (9 * 9 = 81) of its digits (total 99), the output is true.

Example 2:
Input: n = 23
Output: false
Explanation:
Since 23 is not divisible by the sum (2 + 3 = 5) plus product (2 * 3 = 6) of its digits (total 11), the output is false.

Constraints:

    1 <= n <= 106
"""

import unittest


class Solution:
    def checkDivisibility(self, n: int) -> bool:
        x = n
        s = 0
        p = 1
        while x:
            d = x % 10
            s += d
            p *= d
            x //= 10
        return n % (p + s) == 0


class TestCheckDivisibility(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        self.assertEqual(self.sol.checkDivisibility(99), True)

    def test_example_2(self):
        self.assertEqual(self.sol.checkDivisibility(23), False)


if __name__ == "__main__":
    unittest.main(verbosity=2)
