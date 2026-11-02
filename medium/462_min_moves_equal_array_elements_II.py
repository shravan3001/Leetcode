"""
https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/description/?envType=daily-question&envId=2026-11-02
462. Minimum Moves to Equal Array Elements II

Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.
In one move, you can increment or decrement an element of the array by 1.
Test cases are designed so that the answer will fit in a 32-bit integer.

Example 1:
Input: nums = [1,2,3]
Output: 2
Explanation:
Only two moves are needed (remember each move increments or decrements one element):
[1,2,3]  =>  [2,2,3]  =>  [2,2,2]

Example 2:
Input: nums = [1,10,2,9]
Output: 16

Constraints:
    n == nums.length
    1 <= nums.length <= 1e5
    -1e9 <= nums[i] <= 1e9
"""

import unittest


class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        median = nums[len(nums) // 2]
        return sum(abs(x - median) for x in nums)


class TestMinMoves2(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        nums = [1, 2, 3]
        output = 2
        self.assertEqual(self.sol.minMoves2(nums), output)

    def test_example_2(self):
        nums = [1, 10, 2, 9]
        output = 16
        self.assertEqual(self.sol.minMoves2(nums), output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
