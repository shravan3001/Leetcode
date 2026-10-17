"""
https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/description/?envType=daily-question&envId=2026-10-17
3551. Minimum Swaps to Sort by Digit Sum

You are given an array nums of distinct positive integers. You need to sort the array in increasing order based on the sum of the digits of each number. If two numbers have the same digit sum, the smaller number appears first in the sorted order.
Return the minimum number of swaps required to rearrange nums into this sorted order.
A swap is defined as exchanging the values at two distinct positions in the array.

Example 1:
Input: nums = [37,100]
Output: 1
Explanation:
    Compute the digit sum for each integer: [3 + 7 = 10, 1 + 0 + 0 = 1] → [10, 1]
    Sort the integers based on digit sum: [100, 37]. Swap 37 with 100 to obtain the sorted order.
    Thus, the minimum number of swaps required to rearrange nums is 1.

Example 2:
Input: nums = [22,14,33,7]
Output: 0
Explanation:
    Compute the digit sum for each integer: [2 + 2 = 4, 1 + 4 = 5, 3 + 3 = 6, 7 = 7] → [4, 5, 6, 7]
    Sort the integers based on digit sum: [22, 14, 33, 7]. The array is already sorted.
    Thus, the minimum number of swaps required to rearrange nums is 0.

Example 3:
Input: nums = [18,43,34,16]
Output: 2
Explanation:
    Compute the digit sum for each integer: [1 + 8 = 9, 4 + 3 = 7, 3 + 4 = 7, 1 + 6 = 7] → [9, 7, 7, 7]
    Sort the integers based on digit sum: [16, 34, 43, 18]. Swap 18 with 16, and swap 43 with 34 to obtain the sorted order.
    Thus, the minimum number of swaps required to rearrange nums is 2.

Constraints:
    1 <= nums.length <= 1e5
    1 <= nums[i] <= 1e9
    nums consists of distinct positive integers.

Hint 1
First, sort the array based on digit sum (and value as a tiebreaker). Then, map each original value to its index in the sorted array.
Hint 2
Now, the problem reduces to finding the minimum number of swaps to sort this mapped array. The answer is n - number_of_cycles in the permutation.
"""

import unittest


class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        n = len(nums)
        idxs = list(range(n))
        sorted_idxs = sorted(
            range(n), key=lambda i: (sum(int(d) for d in str(nums[i])), nums[i])
        )
        visited = [False] * n
        cycles = 0
        for start in range(n):
            if visited[start]:
                continue
            cycles += 1
            j = start
            while not visited[j]:
                visited[j] = True
                j = sorted_idxs[j]

        return n - cycles


class TestMinSwaps(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        nums = [37, 100]
        output = 1
        self.assertEqual(self.sol.minSwaps(nums), output)

    def test_example_2(self):
        nums = [22, 14, 33, 7]
        output = 0
        self.assertEqual(self.sol.minSwaps(nums), output)

    def test_example_3(self):
        nums = [18, 43, 34, 16]
        output = 2
        self.assertEqual(self.sol.minSwaps(nums), output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
