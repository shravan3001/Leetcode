"""
https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/description/?envType=daily-question&envId=2026-09-24
3550. Smallest Index With Digit Sum Equal to Index

You are given an integer array nums.
Return the smallest index i such that the sum of the digits of nums[i] is equal to i.
If no such index exists, return -1.

Example 1:
Input: nums = [1,3,2]
Output: 2
Explanation:
    For nums[2] = 2, the sum of digits is 2, which is equal to index i = 2. Thus, the output is 2.

Example 2:
Input: nums = [1,10,11]
Output: 1
Explanation:
    For nums[1] = 10, the sum of digits is 1 + 0 = 1, which is equal to index i = 1.
    For nums[2] = 11, the sum of digits is 1 + 1 = 2, which is equal to index i = 2.
    Since index 1 is the smallest, the output is 1.

Example 3:
Input: nums = [1,2,3]
Output: -1
Explanation:
    Since no index satisfies the condition, the output is -1.

Constraints:
    1 <= nums.length <= 100
    0 <= nums[i] <= 1000

"""

import unittest
from typing import List


class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        ans = -1
        for i, x in enumerate(nums):
            s = 0
            while x:
                s += x % 10
                x //= 10
            if i == s:
                ans = i
                break
        return ans


class TestSmallestIndex(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        nums = [1, 3, 2]
        output = 2
        self.assertEqual(self.sol.smallestIndex(nums), output)

    def test_example_2(self):
        nums = [1, 10, 11]
        output = 1
        self.assertEqual(self.sol.smallestIndex(nums), output)

    def test_example_3(self):
        nums = [1, 2, 3]
        output = -1
        self.assertEqual(self.sol.smallestIndex(nums), output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
