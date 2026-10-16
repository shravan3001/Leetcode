"""
https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/description/?envType=daily-question&envId=2026-10-16
2916. Subarrays Distinct Element Sum of Squares II

You are given a 0-indexed integer array nums.
The distinct count of a subarray of nums is defined as:
    Let nums[i..j] be a subarray of nums consisting of all the indices from i to j such that 0 <= i <= j < nums.length. Then the number of distinct values in nums[i..j] is called the distinct count of nums[i..j].
Return the sum of the squares of distinct counts of all subarrays of nums.
Since the answer may be very large, return it modulo 109 + 7.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,2,1]
Output: 15
Explanation: Six possible subarrays are:
[1]: 1 distinct value
[2]: 1 distinct value
[1]: 1 distinct value
[1,2]: 2 distinct values
[2,1]: 2 distinct values
[1,2,1]: 2 distinct values
The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 + 22 + 22 + 22 = 15.

Example 2:
Input: nums = [2,2]
Output: 3
Explanation: Three possible subarrays are:
[2]: 1 distinct value
[2]: 1 distinct value
[2,2]: 1 distinct value
The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 = 3.

Constraints:
    1 <= nums.length <= 1e5
    1 <= nums[i] <= 1e5

Hint 1
Consider the sum of the count of distinct values of subarrays ending with index i, let’s call it sum. Now if you need the sum of all subarrays ending with index i + 1 think how it can be related to sum and what extra will be needed to add to this.
Hint 2
You can find that extra sum using the segment tree.
"""

import unittest


class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Segment tree: s = sum of d, sq = sum of d^2, lz = pending add.
        # Exact (non-modded) values for s and lz are small enough (<= ~1e10),
        # but sq is reduced mod MOD.
        size = 1
        while size < n:
            size *= 2
        s = [0] * (2 * size)
        sq = [0] * (2 * size)
        lz = [0] * (2 * size)
        ln = [0] * (2 * size)
        for i in range(size):
            ln[size + i] = 1
        for i in range(size - 1, 0, -1):
            ln[i] = ln[2 * i] + ln[2 * i + 1]

        def apply(node: int, k: int) -> None:
            sq[node] = (sq[node] + 2 * k * s[node] + k * k * ln[node]) % MOD
            s[node] += k * ln[node]
            lz[node] += k

        def push(node: int) -> None:
            if lz[node]:
                apply(2 * node, lz[node])
                apply(2 * node + 1, lz[node])
                lz[node] = 0

        def update(node: int, lo: int, hi: int, l: int, r: int) -> None:
            if r < lo or hi < l:
                return
            if l <= lo and hi <= r:
                apply(node, 1)
                return
            push(node)
            mid = (lo + hi) // 2
            update(2 * node, lo, mid, l, r)
            update(2 * node + 1, mid + 1, hi, l, r)
            s[node] = s[2 * node] + s[2 * node + 1]
            sq[node] = (sq[2 * node] + sq[2 * node + 1]) % MOD

        last = {}
        ans = 0
        for r, x in enumerate(nums):
            prev = last.get(x, -1)
            update(1, 0, size - 1, prev + 1, r)
            last[x] = r
            ans = (ans + sq[1]) % MOD
        return ans


class TestSumCounts(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        nums = [1, 2, 1]
        output = 15
        self.assertEqual(self.sol.sumCounts(nums), output)

    def test_example_2(self):
        nums = [2, 2]
        output = 3
        self.assertEqual(self.sol.sumCounts(nums), output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
