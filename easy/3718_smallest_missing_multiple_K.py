"""
https://leetcode.com/problems/smallest-missing-multiple-of-k/description/?envType=daily-question&envId=2026-08-25
3718. Smallest Missing Multiple of K

Given an integer array nums and an integer k, return the smallest positive multiple of k that is missing from nums.
A multiple of k is any positive integer divisible by k.

Example 1:
Input: nums = [8,2,3,4,6], k = 2
Output: 10
Explanation:
The multiples of k = 2 are 2, 4, 6, 8, 10, 12... and the smallest multiple missing from nums is 10.

Example 2:
Input: nums = [1,4,7,10,15], k = 5
Output: 5
Explanation:
The multiples of k = 5 are 5, 10, 15, 20... and the smallest multiple missing from nums is 5.

Constraints:

    1 <= nums.length <= 100
    1 <= nums[i] <= 100
    1 <= k <= 100
"""

import unittest
from typing import List


class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        numset = set(nums)
        f = 1
        while True:
            p = k * f
            if p not in numset:
                return p
            f += 1
        return 0


class TestMissingMultiple(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        nums = [8, 2, 3, 4, 6]
        k = 2
        self.assertEqual(self.sol.missingMultiple(nums, k), 10)

    def test_example_2(self):
        nums = [1, 4, 7, 10, 15]
        k = 5
        self.assertEqual(self.sol.missingMultiple(nums, k), 5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
