"""
https://leetcode.com/problems/minimum-operations-to-sort-a-permutation/description/?envType=daily-question&envId=2026-10-22
3942. Minimum Operations to Sort a Permutation

You are given an integer array nums of length n, where nums is a permutation of the integers from 0 to n - 1.
You may perform only the following operations:
    Reverse the entire array.
    Rotate Left by One: Move the first element to the end of the array, and rest elements to left by one position.
Return an integer denoting the minimum number of operations required to sort the array in increasing order. If it is not possible to sort the array using only the given operations, return -1.

Example 1:
Input: nums = [0,2,1]
Output: 2
Explanation:
    Rotate Left by one: [2, 1, 0]
    Reverse the array: [0, 1, 2]
The array becomes sorted in 2 operations, which is minimal

Example 2:
Input: nums = [1,0,2]
Output: 2
Explanation:
    Reverse the array: [2, 0, 1]
    Rotate Left by one: [0, 1, 2]
The array becomes sorted in 2 operations, which is minimal.

Example 3:
Input: nums = [2,0,1,3]
Output: -1
Explanation:
It is impossible to reach [2, 0, 1, 3]. Thus, the answer is -1.

Constraints:
    1 <= n == nums.length <= 1e5
    0 <= nums[i] <= n - 1
    nums is a permutation of integers from 0 to n - 1.

Hint 1
1a. (Case Analysis) The operations generate only rotations of nums and rotations of reverse(nums).
Hint 2
1b. (Case Analysis) So sorting is possible if and only if nums is a rotation of increasing order, or a rotation of decreasing order.
Hint 3
1c. (Case Analysis) If nums is increasing cyclically and nums[i] = 0, then rotating left i times sorts the array, or we may reverse, rotate, then reverse again. Take the minimum between these possibilities.
Hint 4
1d. (Case Analysis) If nums is decreasing cyclically, try both possibilities: reverse first, or rotate first and then reverse. Take the minimum valid cost.
Hint 5
2a. (Breadth-First Search) As follows from Hint 1a and 1b, each reachable array can be represented as a state. Since all reachable arrays belong to one of two families, we can compress a state into (type, shift). type = 0: a rotation of the original array. type = 1: a rotation of the reversed array. shift denotes the number of left rotations applied within that family.
Hint 6
2b. (Breadth-First Search) A left rotation changes shift to (shift + 1) % n. A reverse toggles type, while also changing the corresponding shift to (n - shift) % n.
Hint 7
2c. (Breadth-First Search) Build a graph on these 2n states using the two allowed operations, then run BFS from (0, 0) to the state representing the input array.
"""

import unittest
from collections import deque


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        if n == 2:
            return 0 if nums[0] == 0 else 1  # [0,1] -> 0, [1,0] -> reverse

        # Determine the cyclic direction and verify the whole array matches it.
        if nums[1] == (nums[0] + 1) % n:
            d = 1
        elif nums[1] == (nums[0] - 1) % n:
            d = -1
        else:
            return -1
        p = nums[0]
        for i in range(n):
            if nums[i] != (p + d * i) % n:
                return -1

        # State: (direction, value at index 0). a[i] = (p + d*i) % n
        def idx(direction: int, start: int) -> int:
            return (0 if direction == 1 else 1) * n + start

        start = idx(d, p)
        target = idx(1, 0)
        if start == target:
            return 0

        dist = [-1] * (2 * n)
        dist[start] = 0
        q = deque([(d, p)])
        while q:
            cd, cp = q.popleft()
            cur = dist[idx(cd, cp)]
            for nd, np_ in (
                (cd, (cp + cd) % n),  # rotate left by one
                (-cd, (cp + cd * (n - 1)) % n),  # reverse
            ):
                k = idx(nd, np_)
                if dist[k] == -1:
                    dist[k] = cur + 1
                    if k == target:
                        return dist[k]
                    q.append((nd, np_))
        return -1

        # n = len(nums)
        # if n == 0:
        #     return -1
        #
        # res = float('inf')
        # target = list(range(n))
        #
        # # Candidate 1: The sorted state is a cyclic shift of the original array.
        # # Since it's a permutation of 0..n-1, if any cyclic shift is sorted,
        # # it must be the one that starts with 0.
        # k = nums.index(0)
        # # Check if L^k(nums) == [0, 1, ..., n-1]
        # # In Python, slicing and list comparison is O(n) and typically faster than loops.
        # if nums[k:] + nums[:k] == target:
        #     # Min operations to reach L^k(nums) is min(k, (n-k) + 2)
        #     res = min(res, k, n - k + 2)
        #
        # # Candidate 2: The sorted state is a cyclic shift of the reversed array.
        # # Similarly, the only candidate is the cyclic shift starting with 0.
        # rev_nums = nums[::-1]
        # k_rev = rev_nums.index(0)
        # # Check if L^k_rev(rev_nums) == [0, 1, ..., n-1]
        # if rev_nums[k_rev:] + rev_nums[:k_rev] == target:
        #     # Min operations to reach L^k_rev(reverse(nums)) is min(k_rev + 1, (n-k_rev) + 1)
        #     # Paths: R then L^k_rev (1+k_rev) OR L^{n-k_rev} then R (n-k_rev+1)
        #     res = min(res, k_rev + 1, n - k_rev + 1)
        #
        # # If no sorted state was reached, it is impossible.
        # if res == float('inf'):
        #     return -1
        #
        # return int(res)


class TestMimOperations(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        nums = [0, 2, 1]
        output = 2
        self.assertEqual(self.sol.minOperations(nums), output)

    def test_example_2(self):
        nums = [2, 0, 1, 3]
        output = -1
        self.assertEqual(self.sol.minOperations(nums), output)

    def test_example_3(self):
        nums = [1, 0, 2]
        output = 2
        self.assertEqual(self.sol.minOperations(nums), output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
