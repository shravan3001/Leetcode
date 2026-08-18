"""
https://leetcode.com/problems/find-the-largest-almost-missing-integer/description/?envType=daily-question&envId=2026-08-18
3471. Find the Largest Almost Missing Integer

You are given an integer array nums and an integer k.
An integer x is almost missing from nums if x appears in exactly one subarray of size k within nums.
Return the largest almost missing integer from nums. If no such integer exists, return -1.
A subarray is a contiguous sequence of elements within an array.

Example 1:
Input: nums = [3,9,2,1,7], k = 3
Output: 7
Explanation:
    1 appears in 2 subarrays of size 3: [9, 2, 1] and [2, 1, 7].
    2 appears in 3 subarrays of size 3: [3, 9, 2], [9, 2, 1], [2, 1, 7].
    3 appears in 1 subarray of size 3: [3, 9, 2].
    7 appears in 1 subarray of size 3: [2, 1, 7].
    9 appears in 2 subarrays of size 3: [3, 9, 2], and [9, 2, 1].
We return 7 since it is the largest integer that appears in exactly one subarray of size k.

Example 2:
Input: nums = [3,9,7,2,1,7], k = 4
Output: 3
Explanation:
    1 appears in 2 subarrays of size 4: [9, 7, 2, 1], [7, 2, 1, 7].
    2 appears in 3 subarrays of size 4: [3, 9, 7, 2], [9, 7, 2, 1], [7, 2, 1, 7].
    3 appears in 1 subarray of size 4: [3, 9, 7, 2].
    7 appears in 3 subarrays of size 4: [3, 9, 7, 2], [9, 7, 2, 1], [7, 2, 1, 7].
    9 appears in 2 subarrays of size 4: [3, 9, 7, 2], [9, 7, 2, 1].
We return 3 since it is the largest and only integer that appears in exactly one subarray of size k.

Example 3:
Input: nums = [0,0], k = 1
Output: -1
Explanation:
There is no integer that appears in only one subarray of size 1.

Constraints:

    1 <= nums.length <= 50
    0 <= nums[i] <= 50
    1 <= k <= nums.length
"""

import unittest
from typing import List
from collections import Counter


class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        c = Counter(nums)
        if k == 1:
            for x in sorted(nums, reverse=True):
                if c[x] == 1:
                    return x
            return -1
        if k == n:
            return max(nums)
        ans = -1
        if c[nums[0]] == 1:
            ans = nums[0]
        if c[nums[-1]] == 1:
            ans = max(ans, nums[-1])
        return ans


class TestLargestInteger(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        nums = [3, 9, 2, 1, 7]
        k = 3
        self.assertEqual(self.sol.largestInteger(nums, k), 7)

    def test_example_2(self):
        nums = [3, 9, 7, 2, 1, 7]
        k = 4
        self.assertEqual(self.sol.largestInteger(nums, k), 3)

    def test_example_3(self):
        nums = [0, 0]
        k = 1
        self.assertEqual(self.sol.largestInteger(nums, k), -1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
