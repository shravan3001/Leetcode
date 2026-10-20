"""
https://leetcode.com/problems/sum-of-sortable-integers/description/?envType=daily-question&envId=2026-10-20
3886. Sum of Sortable Integers

You are given an integer array nums of length n.
An integer k is called sortable if k divides n and you can sort nums in non-decreasing order by sequentially performing the following operations:
    Partition nums into consecutive subarrays of length k.
    Cyclically rotate each subarray independently any number of times to the left or to the right.
Return an integer denoting the sum of all possible sortable integers k.

Example 1:
Input: nums = [3,1,2]
Output: 3
Explanation:
    For n = 3, possible divisors are 1 and 3.
    For k = 1: each subarray has one element. No rotation can sort the array.
    For k = 3: the single subarray [3, 1, 2] can be rotated once to produce [1, 2, 3], which is sorted.
    Only k = 3 is sortable. Hence, the answer is 3.

Example 2:
Input: nums = [7,6,5]
Output: 0
Explanation:
    For n = 3, possible divisors are 1 and 3.
    For k = 1: each subarray has one element. No rotation can sort the array.
    For k = 3: the single subarray [7, 6, 5] cannot be rotated into non-decreasing order.
    No k is sortable. Hence, the answer is 0.

Example 3:
Input: nums = [5,8]
Output: 3
Explanation:
    For n = 2, possible divisors are 1 and 2.
    Since [5, 8] is already sorted, every divisor is sortable. Hence, the answer is 1 + 2 = 3.

Constraints:
    1 <= n == nums.length <= 1e5
    1 <= nums[i] <= 1e5
"""

import unittest


class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)

        def get_divisors(x: int):
            i = 1
            while i * i <= x:
                if x % i == 0:
                    yield i
                    if i != x // i:
                        yield x // i
                i += 1

        def check(s: int, e: int):
            """Is nums[s..e] a rotation of a sorted array? Returns (ok, min, max)."""
            drops = 0
            mx = mn = nums[s]
            for i in range(s + 1, e + 1):
                mx = max(mx, nums[i])
                mn = min(mn, nums[i])
                if nums[i] < nums[i - 1]:
                    drops += 1
                    if drops > 1:
                        return False, 0, 0
            # with one drop, wrapping around must not go down: last <= first
            if drops == 1 and nums[e] > nums[s]:
                return False, 0, 0
            return True, mn, mx

        ans = 0
        for k in get_divisors(n):
            ok = True
            prev_max = float("-inf")
            for s in range(0, n, k):
                good, mn, mx = check(s, s + k - 1)
                if not good or mn < prev_max:
                    ok = False
                    break
                prev_max = mx
            if ok:
                ans += k
        return ans


class TestSortableIntegers(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        self.assertEqual(self.sol.sortableIntegers([3, 1, 2]), 3)

    def test_example_2(self):
        self.assertEqual(self.sol.sortableIntegers([7, 6, 5]), 0)

    def test_example_3(self):
        self.assertEqual(self.sol.sortableIntegers([5, 8]), 3)

    def test_rotation_with_duplicates(self):
        self.assertEqual(self.sol.sortableIntegers([2, 2, 1, 2]), 4)

    def test_blocks_ordered(self):
        self.assertEqual(self.sol.sortableIntegers([2, 1, 4, 3]), 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
