"""
https://leetcode.com/problems/find-target-indices-after-sorting-array/description/?envType=daily-question&envId=2026-10-19
2089. Find Target Indices After Sorting Array

You are given a 0-indexed integer array nums and a target element target.
A target index is an index i such that nums[i] == target.
Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

Example 1:
Input: nums = [1,2,5,2,3], target = 2
Output: [1,2]
Explanation: After sorting, nums is [1,2,2,3,5].
The indices where nums[i] == 2 are 1 and 2.

Example 2:
Input: nums = [1,2,5,2,3], target = 3
Output: [3]
Explanation: After sorting, nums is [1,2,2,3,5].
The index where nums[i] == 3 is 3.

Example 3:
Input: nums = [1,2,5,2,3], target = 5
Output: [4]
Explanation: After sorting, nums is [1,2,2,3,5].
The index where nums[i] == 5 is 4.

Constraints:
    1 <= nums.length <= 100
    1 <= nums[i], target <= 100
"""

import unittest


class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        start = 0
        end = 0
        for x in nums:
            if x < target:
                start += 1
                end += 1
            elif x == target:
                end += 1
        return list(range(start, end))


class TestTargetIndices(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        nums = [1, 2, 5, 2, 3]
        target = 2
        output = [1, 2]
        self.assertEqual(self.sol.targetIndices(nums, target), output)

    def test_example_2(self):
        nums = [1, 2, 5, 2, 3]
        target = 3
        output = [3]
        self.assertEqual(self.sol.targetIndices(nums, target), output)

    def test_example_3(self):
        nums = [1, 2, 5, 2, 3]
        target = 5
        output = [4]
        self.assertEqual(self.sol.targetIndices(nums, target), output)

    def test_example_4(self):
        nums = [1, 2, 5, 2, 3]
        target = 6
        output = []
        self.assertEqual(self.sol.targetIndices(nums, target), output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
