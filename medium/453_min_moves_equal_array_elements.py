"""
https://leetcode.com/problems/minimum-moves-to-equal-array-elements/description/?envType=daily-question&envId=2026-11-01
453. Minimum Moves to Equal Array Elements

Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.
In one move, you can increment n - 1 elements of the array by 1.

Example 1:
Input: nums = [1,2,3]
Output: 3
Explanation: Only three moves are needed (remember each move increments two elements):
[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

Example 2:
Input: nums = [1,1,1]
Output: 0

Constraints:
    n == nums.length
    1 <= nums.length <= 1e5
    -1e9 <= nums[i] <= 1e9
    The answer is guaranteed to fit in a 32-bit integer.
"""

import unittest


class Solution:
    def minMoves(self, nums: list[int]) -> int:
        return sum(nums) - min(nums) * len(nums)


class TestMinMoves(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        nums = [1, 2, 3]
        output = 3
        self.assertEqual(self.sol.minMoves(nums), output)

    def test_example_2(self):
        nums = [1, 1, 1]
        output = 0
        self.assertEqual(self.sol.minMoves(nums), output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
