"""
https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/description/?envType=daily-question&envId=2026-11-04
3505. Minimum Operations to Make Elements Within K Subarrays Equal

You are given an integer array nums and two integers, x and k. You can perform the following operation any number of times (including zero):
    Increase or decrease any element of nums by 1.
Return the minimum number of operations needed to have at least k non-overlapping subarrays of size exactly x in nums, where all elements within each subarray are equal.

Example 1:
Input: nums = [5,-2,1,3,7,3,6,4,-1], x = 3, k = 2
Output: 8
Explanation:
    Use 3 operations to add 3 to nums[1] and use 2 operations to subtract 2 from nums[3]. The resulting array is [5, 1, 1, 1, 7, 3, 6, 4, -1].
    Use 1 operation to add 1 to nums[5] and use 2 operations to subtract 2 from nums[6]. The resulting array is [5, 1, 1, 1, 7, 4, 4, 4, -1].
    Now, all elements within each subarray [1, 1, 1] (from indices 1 to 3) and [4, 4, 4] (from indices 5 to 7) are equal. Since 8 total operations were used, 8 is the output.

Example 2:
Input: nums = [9,-2,-2,-2,1,5], x = 2, k = 2
Output: 3
Explanation:
    Use 3 operations to subtract 3 from nums[4]. The resulting array is [9, -2, -2, -2, -2, 5].
    Now, all elements within each subarray [-2, -2] (from indices 1 to 2) and [-2, -2] (from indices 3 to 4) are equal. Since 3 operations were used, 3 is the output.

Constraints:
    2 <= nums.length <= 1e5
    -1e6 <= nums[i] <= 1e6
    2 <= x <= nums.length
    1 <= k <= 15
    2 <= k * x <= nums.length
"""

import unittest


class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)

        # ---- Step 1: cost of making each window of size x equal ----
        vals = sorted(set(nums))
        rank = {v: i + 1 for i, v in enumerate(vals)}  # 1-indexed
        m = len(vals)
        cnt = [0] * (m + 1)  # Fenwick tree over counts
        sm = [0] * (m + 1)  # Fenwick tree over sums
        top = 1 << (m.bit_length())  # highest power of two for binary descent

        def update(pos: int, dc: int, ds: int) -> None:
            while pos <= m:
                cnt[pos] += dc
                sm[pos] += ds
                pos += pos & -pos

        def prefix(pos: int) -> tuple[int, int]:
            c = s = 0
            while pos > 0:
                c += cnt[pos]
                s += sm[pos]
                pos -= pos & -pos
            return c, s

        def kth(target: int) -> int:
            """Smallest compressed index whose prefix count >= target."""
            pos = 0
            step = top
            while step:
                nxt = pos + step
                if nxt <= m and cnt[nxt] < target:
                    pos = nxt
                    target -= cnt[nxt]
                step >>= 1
            return pos + 1

        mid = (x + 1) // 2
        total = 0
        costs = [0] * (n - x + 1)
        for i in range(n):
            update(rank[nums[i]], 1, nums[i])
            total += nums[i]
            if i >= x:
                update(rank[nums[i - x]], -1, -nums[i - x])
                total -= nums[i - x]
            if i >= x - 1:
                idx = kth(mid)
                med = vals[idx - 1]
                c_le, s_le = prefix(idx)
                costs[i - x + 1] = med * c_le - s_le + (total - s_le) - med * (x - c_le)

        # ---- Step 2: pick k non-overlapping windows with min total cost ----
        INF = float("inf")
        prev = [0] * (n + 1)  # dp with 0 windows
        for _ in range(k):
            cur = [INF] * (n + 1)
            for i in range(x, n + 1):
                cur[i] = min(cur[i - 1], prev[i - x] + costs[i - x])
            prev = cur
        return prev[n]


class TestMinOperations(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        nums = [5, -2, 1, 3, 7, 3, 6, 4, -1]
        x = 3
        k = 2
        output = 8
        self.assertEqual(self.sol.minOperations(nums, x, k), output)

    def test_example_2(self):
        nums = [9, -2, -2, -2, 1, 5]
        x = 2
        k = 2
        output = 3
        self.assertEqual(self.sol.minOperations(nums, x, k), output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
