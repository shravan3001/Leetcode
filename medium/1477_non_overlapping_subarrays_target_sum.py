"""
https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/description/?envType=daily-question&envId=2026-09-17
1477. Find Two Non-overlapping Sub-arrays Each With Target Sum

You are given an array of integers arr and an integer target.
You have to find two non-overlapping sub-arrays of arr each with a sum equal target. There can be multiple answers so you have to find an answer where the sum of the lengths of the two sub-arrays is minimum.
Return the minimum sum of the lengths of the two required sub-arrays, or return -1 if you cannot find such two sub-arrays.

Example 1:
Input: arr = [3,2,2,4,3], target = 3
Output: 2
Explanation: Only two sub-arrays have sum = 3 ([3] and [3]). The sum of their lengths is 2.

Example 2:
Input: arr = [7,3,4,7], target = 7
Output: 2
Explanation: Although we have three non-overlapping sub-arrays of sum = 7 ([7], [3,4] and [7]), but we will choose the first and third sub-arrays as the sum of their lengths is 2.

Example 3:
Input: arr = [4,3,2,6,2,3,4], target = 6
Output: -1
Explanation: We have only one sub-array of sum = 6.

Constraints:
    1 <= arr.length <= 105
    1 <= arr[i] <= 1000
    1 <= target <= 108

"""

import unittest


class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        INF = float("inf")
        best = [
            INF
        ] * n  # best[i] = min length of a valid subarray ending at index <= i
        ans = INF
        left = 0
        cur_sum = 0

        for right in range(n):
            cur_sum += arr[right]
            while cur_sum > target:
                cur_sum -= arr[left]
                left += 1

            if cur_sum == target:
                cur_len = right - left + 1
                if left > 0 and best[left - 1] != INF:
                    ans = min(ans, cur_len + best[left - 1])
                best[right] = min(best[right - 1] if right > 0 else INF, cur_len)
            else:
                best[right] = best[right - 1] if right > 0 else INF

        return ans if ans != INF else -1


class TestMinSumOfLengths(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        arr = [3, 2, 2, 4, 3]
        target = 3
        output = 2
        self.assertEqual(self.sol.minSumOfLengths(arr, target), output)

    def test_example_2(self):
        arr = [7, 3, 4, 7]
        target = 7
        output = 2
        self.assertEqual(self.sol.minSumOfLengths(arr, target), output)

    def test_example_3(self):
        arr = [4, 3, 2, 6, 2, 3, 4]
        target = 6
        output = -1
        self.assertEqual(self.sol.minSumOfLengths(arr, target), output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
