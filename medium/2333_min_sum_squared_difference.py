"""
https://leetcode.com/problems/minimum-sum-of-squared-difference/description/?envType=daily-question&envId=2026-10-10
2333. Minimum Sum of Squared Difference

You are given two positive 0-indexed integer arrays nums1 and nums2, both of length n.
The sum of squared difference of arrays nums1 and nums2 is defined as the sum of (nums1[i] - nums2[i])2 for each 0 <= i < n.
You are also given two positive integers k1 and k2. You can modify any of the elements of nums1 by +1 or -1 at most k1 times. Similarly, you can modify any of the elements of nums2 by +1 or -1 at most k2 times.
Return the minimum sum of squared difference after modifying array nums1 at most k1 times and modifying array nums2 at most k2 times.
Note: You are allowed to modify the array elements to become negative integers.

Example 1:
Input: nums1 = [1,2,3,4], nums2 = [2,10,20,19], k1 = 0, k2 = 0
Output: 579
Explanation: The elements in nums1 and nums2 cannot be modified because k1 = 0 and k2 = 0.
The sum of square difference will be: (1 - 2)2 + (2 - 10)2 + (3 - 20)2 + (4 - 19)2 = 579.

Example 2:
Input: nums1 = [1,4,10,12], nums2 = [5,8,6,9], k1 = 1, k2 = 1
Output: 43
Explanation: One way to obtain the minimum sum of square difference is:
- Increase nums1[0] once.
- Increase nums2[2] once.
The minimum of the sum of square difference will be:
(2 - 5)2 + (4 - 8)2 + (10 - 7)2 + (12 - 9)2 = 43.
Note that, there are other ways to obtain the minimum of the sum of square difference, but there is no way to obtain a sum smaller than 43.

Constraints:
    n == nums1.length == nums2.length
    1 <= n <= 1e5
    0 <= nums1[i], nums2[i] <= 1e5
    0 <= k1, k2 <= 1e9
"""

import unittest


class Solution:
    def minSumSquareDiff(
        self, nums1: list[int], nums2: list[int], k1: int, k2: int
    ) -> int:
        total = k1 + k2
        diffs = sorted(abs(x1 - x2) for x1, x2 in zip(nums1, nums2))
        if sum(diffs) <= total:
            return 0

        # run-length encode the sorted diffs: (value, count)
        diff_cnts: list[tuple[int, int]] = [(diffs[0], 1)]
        for d in diffs[1:]:
            if diff_cnts[-1][0] == d:
                diff_cnts[-1] = (d, diff_cnts[-1][1] + 1)
            else:
                diff_cnts.append((d, 1))

        # Shave the largest diffs down level by level.
        # cnt = number of elements currently at level `val`
        # (the top levels already merged down into it).
        cnt = 0
        for i in range(len(diff_cnts) - 1, -1, -1):
            val, c = diff_cnts[i]
            cnt += c
            prev = diff_cnts[i - 1][0] if i > 0 else 0
            cost = (val - prev) * cnt
            if cost <= total:
                total -= cost
                continue

            # Can't reach the next level: spread the remaining budget evenly.
            q, r = divmod(total, cnt)
            # r elements end at val - q - 1, the other cnt - r at val - q
            ans = r * (val - q - 1) ** 2 + (cnt - r) * (val - q) ** 2
            # untouched lower levels
            ans += sum(v * v * k for v, k in diff_cnts[:i])
            return ans

        return 0  # unreachable: sum(diffs) > total guarantees an early return

    # binary search method
    # k = k1 + k2
    # diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
    # if sum(diffs) <= k:
    #     return 0
    #
    # def cost(t):
    #     return sum(d - t for d in diffs if d > t)
    #
    # lo, hi = 0, max(diffs)
    # while lo < hi:
    #     mid = (lo + hi) // 2
    #     if cost(mid) <= k:
    #         hi = mid
    #     else:
    #         lo = mid + 1
    # t = lo
    #
    # k -= cost(t)
    # diffs = [min(d, t) for d in diffs]
    # # leftover budget: lower some elements at level t to t-1
    # for i, d in enumerate(diffs):
    #     if k == 0:
    #         break
    #     if d == t and t > 0:
    #         diffs[i] -= 1
    #         k -= 1
    # return sum(d * d for d in diffs)


class TestMinSumSquareDiff(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        nums1 = [1, 2, 3, 4]
        nums2 = [2, 10, 20, 19]
        k1, k2 = 0, 0
        output = 579
        self.assertEqual(self.sol.minSumSquareDiff(nums1, nums2, k1, k2), output)

    def test_example_2(self):
        nums1 = [1, 4, 10, 12]
        nums2 = [5, 8, 6, 9]
        k1, k2 = 1, 1
        output = 43
        self.assertEqual(self.sol.minSumSquareDiff(nums1, nums2, k1, k2), output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
