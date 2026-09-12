"""
https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/description/?envType=daily-question&envId=2026-09-12
3414. Maximum Score of Non-overlapping Intervals

You are given a 2D integer array intervals, where intervals[i] = [li, ri, weighti]. Interval i starts at position li and ends at ri, and has a weight of weighti. You can choose up to 4 non-overlapping intervals. The score of the chosen intervals is defined as the total sum of their weights.
Return the lexicographically smallest array of at most 4 indices from intervals with maximum score, representing your choice of non-overlapping intervals.
Two intervals are said to be non-overlapping if they do not share any points. In particular, intervals sharing a left or right boundary are considered overlapping.

Example 1:
Input: intervals = [[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]]
Output: [2,3]
Explanation:
You can choose the intervals with indices 2, and 3 with respective weights of 5, and 3.

Example 2:
Input: intervals = [[5,8,1],[6,7,7],[4,7,3],[9,10,6],[7,8,2],[11,14,3],[3,5,5]]
Output: [1,3,5,6]
Explanation:
You can choose the intervals with indices 1, 3, 5, and 6 with respective weights of 7, 6, 3, and 5.

Constraints:
    1 <= intevals.length <= 5 * 104
    intervals[i].length == 3
    intervals[i] = [li, ri, weighti]
    1 <= li <= ri <= 109
    1 <= weighti <= 109
"""

import unittest
from typing import List
import bisect


class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        if n == 0:
            return []
        arr = sorted(range(n), key=lambda i: intervals[i][1])
        rs = [intervals[i][1] for i in arr]
        ls = [intervals[i][0] for i in arr]
        ws = [intervals[i][2] for i in arr]

        dp_prev = [(0, ())] * (n + 1)  # k = 0
        for k in range(1, 5):
            dp_cur = [(0, ())] * (n + 1)
            for j in range(1, n + 1):
                elem_idx = arr[j - 1]
                l = ls[j - 1]
                w = ws[j - 1]
                skip = dp_cur[j - 1]
                cnt = bisect.bisect_left(rs, l)
                base = dp_prev[cnt]
                take = (base[0] + w, tuple(sorted(base[1] + (elem_idx,))))
                if take[0] > skip[0] or (take[0] == skip[0] and take[1] < skip[1]):
                    dp_cur[j] = take
                else:
                    dp_cur[j] = skip
            dp_prev = dp_cur
        return list(dp_prev[n][1])


class TestMaximumWeight(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        intervals = [[1, 3, 2], [4, 5, 2], [1, 5, 5], [6, 9, 3], [6, 7, 1], [8, 9, 1]]
        output = [2, 3]
        self.assertEqual(self.sol.maximumWeight(intervals), output)

    def test_example_2(self):
        intervals = [
            [5, 8, 1],
            [6, 7, 7],
            [4, 7, 3],
            [9, 10, 6],
            [7, 8, 2],
            [11, 14, 3],
            [3, 5, 5],
        ]
        output = [1, 3, 5, 6]
        self.assertEqual(self.sol.maximumWeight(intervals), output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
