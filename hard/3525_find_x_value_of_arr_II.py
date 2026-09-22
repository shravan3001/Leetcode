"""
https://leetcode.com/problems/find-x-value-of-array-ii/description/?envType=daily-question&envId=2026-09-22
3525. Find X Value of Array II

You are given an array of positive integers nums and a positive integer k. You are also given a 2D array queries, where queries[i] = [indexi, valuei, starti, xi].
You are allowed to perform an operation once on nums, where you can remove any suffix from nums such that nums remains non-empty.
The x-value of nums for a given x is defined as the number of ways to perform this operation so that the product of the remaining elements leaves a remainder of x modulo k.
For each query in queries you need to determine the x-value of nums for xi after performing the following actions:
    Update nums[indexi] to valuei. Only this step persists for the rest of the queries.
    Remove the prefix nums[0..(starti - 1)] (where nums[0..(-1)] will be used to represent the empty prefix).
Return an array result of size queries.length where result[i] is the answer for the ith query.
A prefix of an array is a subarray that starts from the beginning of the array and extends to any point within it.
A suffix of an array is a subarray that starts at any point within the array and extends to the end of the array.
Note that the prefix and suffix to be chosen for the operation can be empty.
Note that x-value has a different definition in this version.

Example 1:
Input: nums = [1,2,3,4,5], k = 3, queries = [[2,2,0,2],[3,3,3,0],[0,1,0,1]]
Output: [2,2,2]
Explanation:
    For query 0, nums becomes [1, 2, 2, 4, 5], and the empty prefix must be removed. The possible operations are:
        Remove the suffix [2, 4, 5]. nums becomes [1, 2].
        Remove the empty suffix. nums becomes [1, 2, 2, 4, 5] with a product 80, which gives remainder 2 when divided by 3.
    For query 1, nums becomes [1, 2, 2, 3, 5], and the prefix [1, 2, 2] must be removed. The possible operations are:
        Remove the empty suffix. nums becomes [3, 5].
        Remove the suffix [5]. nums becomes [3].
    For query 2, nums becomes [1, 2, 2, 3, 5], and the empty prefix must be removed. The possible operations are:
        Remove the suffix [2, 2, 3, 5]. nums becomes [1].
        Remove the suffix [3, 5]. nums becomes [1, 2, 2].

Example 2:
Input: nums = [1,2,4,8,16,32], k = 4, queries = [[0,2,0,2],[0,2,0,1]]
Output: [1,0]
Explanation:
    For query 0, nums becomes [2, 2, 4, 8, 16, 32]. The only possible operation is:
        Remove the suffix [2, 4, 8, 16, 32].
    For query 1, nums becomes [2, 2, 4, 8, 16, 32]. There is no possible way to perform the operation.

Example 3:
Input: nums = [1,1,2,1,1], k = 2, queries = [[2,1,0,1]]
Output: [5]

Constraints:
    1 <= nums[i] <= 1e9
    1 <= nums.length <= 1e5
    1 <= k <= 5
    1 <= queries.length <= 2 * 1e4
    queries[i] == [indexi, valuei, starti, xi]
    0 <= indexi <= nums.length - 1
    1 <= valuei <= 1e9
    0 <= starti <= nums.length - 1
    0 <= xi <= k - 1

Hint:
Hint 1
Use a segment tree to efficiently maintain and merge product prefix information for the array nums.
Hint 2
In each segment tree node, store a frequency count of prefix product remainders for every x in the range [0, k - 1].
Hint 3
For each query, update nums[index] to value, then merge the segments corresponding to nums[start..n - 1] to compute the x-value for xi.
"""

from typing import Optional, List, Tuple
import unittest


class SegTree:
    def __init__(self, nums: List[int], k: int) -> None:
        self.n = len(nums)
        self.nums = nums[:]
        self.k = k
        # cnt[node] : list length k, cnt[y] = #positions j in node's range with
        #             product(s..j) % k == y  (i.e. distribution assuming an
        #             incoming multiplier of 1)
        # total[node]: product of entire range mod k (a scalar, not a distribution)
        self.cnt  = [None] * (4 * self.n)
        self.total = [0] * (4 * self.n)
        self._build(0, 0, self.n - 1)

    def _mid(self, s: int, e: int) -> int:
        return (s + e) // 2

    def _children(self, node: int) -> Tuple[int, int]:
        return 2 * node + 1, 2 * node + 2

    def _build(self, node: int, s: int, e: int) -> None:
        if s == e:
            v = self.nums[s] % self.k
            c = [0] * self.k
            c[v] = 1
            self.cnt[node] = c
            self.total[node] = v
            return
        m = self._mid(s, e)
        l, r = self._children(node)
        self._build(l, s, m)
        self._build(r, m + 1, e)
        self._pull(node, l, r)

    def _pull(self, node: int, l: int, r: int) -> None:
        # combine children l (left) and r (right), already in left-to-right order
        k = self.k
        lc, rc = self.cnt[l], self.cnt[r]
        lt = self.total[l]
        combined = [0] * k
        for y in range(k):
            combined[y] += lc[y]
        for y in range(k):
            if rc[y]:
                combined[(lt * y) % k] += rc[y]
        self.cnt[node] = combined
        self.total[node] = (lt * self.total[r]) % k

    def update(self, idx: int, val: int) -> None:
        self._update(0, 0, self.n - 1, idx, val)

    def _update(self, node: int, s: int, e: int, idx: int, val: int) -> None:
        if s == e:
            v = val % self.k
            c = [0] * self.k
            c[v] = 1
            self.cnt[node] = c
            self.total[node] = v
            self.nums[s] = val
            return
        m = self._mid(s, e)
        l, r = self._children(node)
        if idx <= m:
            self._update(l, s, m, idx, val)
        else:
            self._update(r, m + 1, e, idx, val)
        self._pull(node, l, r)

    def query(self, ql: int, qr: int) -> List[int]:
        # returns cnt distribution (as if starting multiplier = 1) for range [ql, qr]
        res = self._query(0, 0, self.n - 1, ql, qr)
        if res is None:
            return [0] * self.k
        return res[0]

    def _query(
        self, node: int, s: int, e: int, ql: int, qr: int
    ) -> Optional[Tuple[List[int], int]]:
        if s > qr or e < ql:
            return None
        if ql <= s and e <= qr:
            return (self.cnt[node], self.total[node])
        m = self._mid(s, e)
        l, r = self._children(node)
        left_res = self._query(l, s, m, ql, qr)
        right_res = self._query(r, m + 1, e, ql, qr)
        if left_res is None:
            return right_res
        if right_res is None:
            return left_res
        lc, lt = left_res
        rc, rt = right_res
        k = self.k
        combined = [0] * k
        for y in range(k):
            combined[y] += lc[y]
        for y in range(k):
            if rc[y]:
                combined[(lt * y) % k] += rc[y]
        return (combined, (lt * rt) % k)


class Solution:
    def resultArray(
        self, nums: List[int], k: int, queries: List[List[int]]
    ) -> List[int]:
        ans: List[int] = []
        st = SegTree(nums, k)
        n = len(nums)

        for idx, val, start, xi in queries:
            st.update(idx, val)
            ans.append(st.query(start, n - 1)[xi])
        return ans


class TestResultArray(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        nums = [1, 2, 3, 4, 5]
        k = 3
        queries = [[2, 2, 0, 2], [3, 3, 3, 0], [0, 1, 0, 1]]
        output = [2, 2, 2]
        self.assertEqual(self.sol.resultArray(nums, k, queries), output)

    def test_example_2(self):
        nums = [1, 2, 4, 8, 16, 32]
        k = 4
        queries = [[0, 2, 0, 2], [0, 2, 0, 1]]
        output = [1, 0]
        self.assertEqual(self.sol.resultArray(nums, k, queries), output)

    def test_example_3(self):
        nums = [1, 1, 2, 1, 1]
        k = 2
        queries = [[2, 1, 0, 1]]
        output = [5]
        self.assertEqual(self.sol.resultArray(nums, k, queries), output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
