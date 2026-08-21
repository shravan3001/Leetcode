"""
https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/description/?envType=daily-question&envId=2026-08-21
3116. Kth Smallest Amount With Single Denomination Combination

You are given an integer array coins representing coins of different denominations and an integer k.
You have an infinite number of coins of each denomination. However, you are not allowed to combine coins of different denominations.
Return the kth smallest amount that can be made using these coins.

Example 1:
Input: coins = [3,6,9], k = 3
Output: 9
Explanation: The given coins can make the following amounts:
Coin 3 produces multiples of 3: 3, 6, 9, 12, 15, etc.
Coin 6 produces multiples of 6: 6, 12, 18, 24, etc.
Coin 9 produces multiples of 9: 9, 18, 27, 36, etc.
All of the coins combined produce: 3, 6, 9, 12, 15, etc.

Example 2:
Input: coins = [5,2], k = 7
Output: 12
Explanation: The given coins can make the following amounts:
Coin 5 produces multiples of 5: 5, 10, 15, 20, etc.
Coin 2 produces multiples of 2: 2, 4, 6, 8, 10, 12, etc.
All of the coins combined produce: 2, 4, 5, 6, 8, 10, 12, 14, 15, etc.

Constraints:

    1 <= coins.length <= 15
    1 <= coins[i] <= 25
    1 <= k <= 2 * 1e9
    coins contains pairwise distinct integers.
"""

import unittest
from typing import List, Tuple
from functools import lru_cache


class Solution:
    @lru_cache(maxsize=None)
    def _gcd(self, x: int, y: int):
        if x % y == 0:
            return y
        return self._gcd(y, x % y)

    @lru_cache(maxsize=None)
    def _lcm(self, x: int, y: int):
        gcd = self._gcd(x, y)
        return (x * y) // gcd

    def gcd_lcm(self, nums: List[int]):
        if len(nums) == 1:
            return nums[0], nums[0]
        gcd = self._gcd(nums[0], nums[1])
        lcm = self._lcm(nums[0], nums[1])
        for x in nums[2:]:
            gcd = self._gcd(gcd, x)
            lcm = self._lcm(lcm, x)
        return gcd, lcm

    def count_multiples(self, l: int, r: int, x: int):
        if x <= 0:
            return 0
        return (r // x) - ((l - 1) // x)

    def get_count(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        ans = 0
        # applying principles of inclusion exclusion
        for bit_mask_key in range(1, 2**n):
            # if number of set bits is odd then add, else remove
            # set bit implies that index coin denomination
            set_nums = []
            set_bit_count = 0
            for idx in range(n):
                if bit_mask_key & 1:
                    set_nums.append(nums[idx])
                    set_bit_count += 1
                bit_mask_key >>= 1
            _, lcm = self.gcd_lcm(set_nums)
            cnt_multiples = self.count_multiples(l, r, lcm)
            ans += (-1) ** (set_bit_count + 1) * cnt_multiples
        return ans

    def findKthSmallest(self, coins: List[int], k: int) -> int:
        minV = min(coins)
        maxV = max(coins) * k
        while minV < maxV:
            candidate = (minV + maxV) // 2
            count = self.get_count(coins, 1, candidate)
            if count >= k:
                maxV = candidate
            else:
                minV = candidate + 1
        return minV


class TestGCD(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_gcd_1(self):
        self.assertEqual(self.sol.gcd_lcm([5, 2]), (1, 10))

    def test_gcd_2(self):
        self.assertEqual(self.sol.gcd_lcm([2, 5]), (1, 10))

    def test_gcd_3(self):
        self.assertEqual(self.sol.gcd_lcm([6, 3]), (3, 6))

    def test_gcd_4(self):
        self.assertEqual(self.sol.gcd_lcm([9, 6]), (3, 18))

    def test_gcd_5(self):
        self.assertEqual(self.sol.gcd_lcm([12, 6, 2]), (2, 12))

    def test_gcd_6(self):
        self.assertEqual(self.sol.gcd_lcm([15, 10, 3]), (1, 30))

    def test_gcd_7(self):
        self.assertEqual(self.sol.gcd_lcm([15]), (15, 15))


class TestFindKthSmallest(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        coins = [3, 6, 9]
        k = 3
        self.assertEqual(self.sol.findKthSmallest(coins, k), 9)

    def test_example_2(self):
        coins = [5, 2]
        k = 7
        self.assertEqual(self.sol.findKthSmallest(coins, k), 12)


if __name__ == "__main__":
    unittest.main(verbosity=2)
