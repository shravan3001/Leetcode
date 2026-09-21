"""
https://leetcode.com/problems/find-x-value-of-array-i/description/?envType=daily-question&envId=2026-09-21
3524. Find X Value of Array I

You are given an array of positive integers nums, and a positive integer k.
You are allowed to perform an operation once on nums, where in each operation you can remove any non-overlapping prefix and suffix from nums such that nums remains non-empty.
You need to find the x-value of nums, which is the number of ways to perform this operation so that the product of the remaining elements leaves a remainder of x when divided by k.
Return an array result of size k where result[x] is the x-value of nums for 0 <= x <= k - 1.
A prefix of an array is a subarray that starts from the beginning of the array and extends to any point within it.
A suffix of an array is a subarray that starts at any point within the array and extends to the end of the array.
Note that the prefix and suffix to be chosen for the operation can be empty.

Example 1:
Input: nums = [1,2,3,4,5], k = 3
Output: [9,2,4]
Explanation:
    For x = 0, the possible operations include all possible ways to remove non-overlapping prefix/suffix that do not remove nums[2] == 3.
    For x = 1, the possible operations are:
        Remove the empty prefix and the suffix [2, 3, 4, 5]. nums becomes [1].
        Remove the prefix [1, 2, 3] and the suffix [5]. nums becomes [4].
    For x = 2, the possible operations are:
        Remove the empty prefix and the suffix [3, 4, 5]. nums becomes [1, 2].
        Remove the prefix [1] and the suffix [3, 4, 5]. nums becomes [2].
        Remove the prefix [1, 2, 3] and the empty suffix. nums becomes [4, 5].
        Remove the prefix [1, 2, 3, 4] and the empty suffix. nums becomes [5].

Example 2:
Input: nums = [1,2,4,8,16,32], k = 4
Output: [18,1,2,0]
Explanation:
    For x = 0, the only operations that do not result in x = 0 are:
        Remove the empty prefix and the suffix [4, 8, 16, 32]. nums becomes [1, 2].
        Remove the empty prefix and the suffix [2, 4, 8, 16, 32]. nums becomes [1].
        Remove the prefix [1] and the suffix [4, 8, 16, 32]. nums becomes [2].
    For x = 1, the only possible operation is:
        Remove the empty prefix and the suffix [2, 4, 8, 16, 32]. nums becomes [1].
    For x = 2, the possible operations are:
        Remove the empty prefix and the suffix [4, 8, 16, 32]. nums becomes [1, 2].
        Remove the prefix [1] and the suffix [4, 8, 16, 32]. nums becomes [2].
    For x = 3, there is no possible way to perform the operation.

Example 3:
Input: nums = [1,1,2,1,1], k = 2
Output: [9,6]

Constraints:
    1 <= nums[i] <= 1e9
    1 <= nums.length <= 1e5
    1 <= k <= 5
"""

from typing import List
import unittest


class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans: List[int] = [0] * k
        prev = [0] * k
        nums = [x % k for x in nums]
        prev[nums[0]] = 1
        ans[nums[0]] = 1

        for i in range(1, n):
            curr = [0] * k
            curr[nums[i]] += 1
            for r in range(k):
                nr = (r * nums[i]) % k
                curr[nr] += prev[r]
            for r in range(k):
                ans[r] += curr[r]
            prev = curr
        return ans


class TestResultArray(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        nums = [1, 2, 3, 4, 5]
        k = 3
        output = [9, 2, 4]
        self.assertEqual(self.sol.resultArray(nums, k), output)

    def test_example_2(self):
        nums = [1, 2, 4, 8, 16, 32]
        k = 4
        output = [18, 1, 2, 0]
        self.assertEqual(self.sol.resultArray(nums, k), output)

    def test_example_3(self):
        nums = [1, 1, 2, 1, 1]
        k = 2
        output = [9, 6]
        self.assertEqual(self.sol.resultArray(nums, k), output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
