"""
https://leetcode.com/problems/smallest-divisible-digit-product-i/description/?envType=daily-question&envId=2026-08-06

Example 1:
Input: n = 10, t = 2
Output: 10
Explanation:
The digit product of 10 is 0, which is divisible by 2, making it the smallest number greater than or equal to 10 that satisfies the condition.

Example 2:
Input: n = 15, t = 3
Output: 16
Explanation:
The digit product of 16 is 6, which is divisible by 3, making it the smallest number greater than or equal to 15 that satisfies the condition.

Constraints:
    1 <= n <= 100
    1 <= t <= 10
"""

import unittest


class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def digit_product(x: int) -> int:
            p = 1
            while x:
                p *= x % 10
                x //= 10
            return p

        while digit_product(n) % t != 0:
            n += 1
        return n


class TestSmallestNumber(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        n, t = 10, 2
        self.assertEqual(self.sol.smallestNumber(n, t), 10)

    def test_example_2(self):
        n, t = 15, 3
        self.assertEqual(self.sol.smallestNumber(n, t), 16)


if __name__ == "__main__":
    unittest.main(verbosity=2)
