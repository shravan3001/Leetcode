"""
https://leetcode.com/problems/stone-game-ii/description/?envType=daily-question&envId=2026-08-09

1140. Stone Game II

Alice and Bob continue their games with piles of stones. There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i]. The objective of the game is to end with the most stones.
Alice and Bob take turns, with Alice starting first.
On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M. Then, we set M = max(M, X). Initially, M = 1.
The game continues until all the stones have been taken.
Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.

Example 1:
Input: piles = [2,7,9,4,4]
Output: 10
Explanation:
    If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 stones in total.
    If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 stones in total.
So we return 10 since it's larger.

Example 2:
Input: piles = [1,2,3,4,5,100]
Output: 104

Constraints:

    1 <= piles.length <= 100
    1 <= piles[i] <= 104

Hint1:
Use dynamic programming: the states are (i, m) for the answer of piles[i:] and that given m.
"""

import unittest
from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        from functools import lru_cache

        n = len(piles)
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        @lru_cache(maxsize=None)
        def dp(i: int, m: int) -> int:
            if i == n:
                return 0
            if i + 2 * m >= n:
                return suffix_sum[i]
            best = 0
            for x in range(1, 2 * m + 1):
                # current player takes piles[i:i+x], opponent then plays optimally on the rest
                taken = suffix_sum[i] - suffix_sum[i + x] if i + x <= n else 0
                best = max(best, taken + suffix_sum[i + x] - dp(i + x, max(m, x)))
            return best

        result = dp(0, 1)
        dp.cache_clear()
        return result


class TestStoneGameII(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        piles = [2, 7, 9, 4, 4]
        self.assertEqual(self.sol.stoneGameII(piles), 10)

    def test_example_2(self):
        piles = [1, 2, 3, 4, 5, 100]
        self.assertEqual(self.sol.stoneGameII(piles), 104)


if __name__ == "__main__":
    unittest.main(verbosity=2)
