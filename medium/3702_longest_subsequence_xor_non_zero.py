"""
https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor/description/?envType=daily-question&envId=2026-08-15
3702. Longest Subsequence With Non-Zero Bitwise XOR

You are given an integer array nums.
Return the length of the longest in nums whose bitwise XOR is non-zero. If no such subsequence exists, return 0.

Example 1:
Input: nums = [1,2,3]
Output: 2
Explanation:
One longest subsequence is [2, 3]. The bitwise XOR is computed as 2 XOR 3 = 1, which is non-zero.

Example 2:
Input: nums = [2,3,4]
Output: 3
Explanation:
The longest subsequence is [2, 3, 4]. The bitwise XOR is computed as 2 XOR 3 XOR 4 = 5, which is non-zero.

Constraints:

    1 <= nums.length <= 1e5
    0 <= nums[i] <= 1e9
"""

import unittest
from typing import List


class Solution:
    def obvious_way(self, nums: List[int]) -> int:
        if all([x == 0 for x in nums]):
            return 0
        out = 0
        n = len(nums)
        for x in nums:
            out ^= x
        return n if out else n - 1

    def get_bit_array(self, n: int) -> List[int]:
        i = 0
        bits = [0] * 32
        while i < 32:
            if (n >> i) & 1:
                bits[i] = 1
            i += 1
        return bits

    def longestSubsequence(self, nums: List[int]) -> int:
        return self.obvious_way(nums)
        # if all([x == 0 for x in nums]):
        #     return 0
        # counts_bit_pos = [0] * 32
        # for x in nums:
        #     bits = self.get_bit_array(x)
        #     for i in range(32):
        #         counts_bit_pos[i] += bits[i]
        # n = len(nums)
        # return n if any([x & 1 == 1 for x in counts_bit_pos]) else n - 1


class TestLongestSubsequence(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        nums = [1, 2, 3]
        self.assertEqual(self.sol.longestSubsequence(nums), 2)

    def test_example_2(self):
        nums = [2, 3, 4]
        self.assertEqual(self.sol.longestSubsequence(nums), 3)

    def test_example_3(self):
        nums = [0, 0, 0]
        self.assertEqual(self.sol.longestSubsequence(nums), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
