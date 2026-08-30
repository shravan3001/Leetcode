"""
https://leetcode.com/problems/removing-minimum-and-maximum-from-array/description/?envType=daily-question&envId=2026-08-30
2091. Removing Minimum and Maximum From Array

You are given a 0-indexed array of distinct integers nums.
There is an element in nums that has the lowest value and an element that has the highest value. We call them the minimum and maximum respectively. Your goal is to remove both these elements from the array.
A deletion is defined as either removing an element from the front of the array or removing an element from the back of the array.
Return the minimum number of deletions it would take to remove both the minimum and maximum element from the array.

Example 1:
Input: nums = [2,10,7,5,4,1,8,6]
Output: 5
Explanation:
The minimum element in the array is nums[5], which is 1.
The maximum element in the array is nums[1], which is 10.
We can remove both the minimum and maximum by removing 2 elements from the front and 3 elements from the back.
This results in 2 + 3 = 5 deletions, which is the minimum number possible.

Example 2:
Input: nums = [0,-4,19,1,8,-2,-3,5]
Output: 3
Explanation:
The minimum element in the array is nums[1], which is -4.
The maximum element in the array is nums[2], which is 19.
We can remove both the minimum and maximum by removing 3 elements from the front.
This results in only 3 deletions, which is the minimum number possible.

Example 3:
Input: nums = [101]
Output: 1
Explanation:
There is only one element in the array, which makes it both the minimum and maximum element.
We can remove it with 1 deletion.

Constraints:

    1 <= nums.length <= 105
    -105 <= nums[i] <= 105
    The integers in nums are distinct.
"""

import unittest
from typing import List


class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 or n == 2:
            return n
        ans = 2 * n
        minV = float("inf")
        minIdx = 0
        maxV = float("-inf")
        maxIdx = 0
        for i, x in enumerate(nums):
            if x < minV:
                minIdx = i
                minV = x
            if x > maxV:
                maxIdx = i
                maxV = x

        rval = maxIdx if maxIdx > minIdx else minIdx
        lval = maxIdx if maxIdx < minIdx else minIdx

        # # deleting both from front
        # ans = min(ans, rval + 1)
        # # deleting both from back
        # ans = min(ans, n - lval)
        # # deleting one from front and one from back
        # ans = min(ans, lval + 1 + n - rval)

        ans = min(rval + 1, n - lval, lval + 1 + n - rval)

        return ans


class TestMinimumDeletions(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        nums = [2, 10, 7, 5, 4, 1, 8, 6]
        self.assertEqual(self.sol.minimumDeletions(nums), 5)

    def test_example_2(self):
        nums = [0, -4, 19, 1, 8, -2, -3, 5]
        self.assertEqual(self.sol.minimumDeletions(nums), 3)

    def test_example_3(self):
        nums = [101]
        self.assertEqual(self.sol.minimumDeletions(nums), 1)

    def test_example_4(self):
        nums = [0, 1, 8, -2, -4, 19, -3, 5]
        self.assertEqual(self.sol.minimumDeletions(nums), 4)


if __name__ == "__main__":
    unittest.main(verbosity=2)
