"""
https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/description/?envType=daily-question&envId=2026-08-11
2996. Smallest Missing Integer Greater Than Sequential Prefix Sum

You are given a 0-indexed array of integers nums.
A prefix nums[0..i] is sequential if, for all 1 <= j <= i, nums[j] = nums[j - 1] + 1. In particular, the prefix consisting only of nums[0] is sequential.
Return the smallest integer x missing from nums such that x is greater than or equal to the sum of the longest sequential prefix.

Example 1:
Input: nums = [1,2,3,2,5]
Output: 6
Explanation: The longest sequential prefix of nums is [1,2,3] with a sum of 6. 6 is not in the array, therefore 6 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix.

Example 2:
Input: nums = [3,4,5,1,12,14,13]
Output: 15
Explanation: The longest sequential prefix of nums is [3,4,5] with a sum of 12. 12, 13, and 14 belong to the array while 15 does not. Therefore 15 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix.

Constraints:

    1 <= nums.length <= 50
    1 <= nums[i] <= 50
"""

import unittest
from typing import List


class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        sum = nums[0]
        n = len(nums)
        if n == 1:
            return sum + 1
        idx = 0
        for i in range(1, n):
            if nums[i] != nums[i - 1] + 1:
                break
            sum += nums[i]
            idx += 1
        if idx == n - 1:
            return sum
        rem = set(nums)
        check_count = n + 1
        while check_count:
            if sum not in rem:
                return sum
            else:
                sum += 1
            check_count -= 1


class TestMissingInteger(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        nums = [1, 2, 3, 2, 5]
        self.assertEqual(self.sol.missingInteger(nums), 6)

    def test_example_2(self):
        nums = [3, 4, 5, 1, 12, 14, 13]
        self.assertEqual(self.sol.missingInteger(nums), 15)

    def test_extra_example_1(self):
        nums = [29, 30, 31, 32, 33, 34, 35, 36, 37]
        self.assertEqual(self.sol.missingInteger(nums), 297)

    def test_extra_example_2(self):
        nums = [46, 8, 2, 4, 1, 4, 10, 2, 4, 10, 2, 5, 7, 3, 1]
        self.assertEqual(self.sol.missingInteger(nums), 47)


if __name__ == "__main__":
    unittest.main(verbosity=2)
