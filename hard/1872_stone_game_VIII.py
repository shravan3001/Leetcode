"""
https://leetcode.com/problems/stone-game-viii/description/?envType=daily-question&envId=2026-08-24
1872. Stone Game VIII

Alice and Bob take turns playing a game, with Alice starting first.
There are n stones arranged in a row. On each player's turn, while the number of stones is more than one, they will do the following:
    Choose an integer x > 1, and remove the leftmost x stones from the row.
    Add the sum of the removed stones' values to the player's score.
    Place a new stone, whose value is equal to that sum, on the left side of the row.
The game stops when only one stone is left in the row.
The score difference between Alice and Bob is (Alice's score - Bob's score). Alice's goal is to maximize the score difference, and Bob's goal is the minimize the score difference.
Given an integer array stones of length n where stones[i] represents the value of the ith stone from the left, return the score difference between Alice and Bob if they both play optimally.

Example 1:
Input: stones = [-1,2,-3,4,-5]
Output: 5
Explanation:
- Alice removes the first 4 stones, adds (-1) + 2 + (-3) + 4 = 2 to her score, and places a stone of
  value 2 on the left. stones = [2,-5].
- Bob removes the first 2 stones, adds 2 + (-5) = -3 to his score, and places a stone of value -3 on
  the left. stones = [-3].
The difference between their scores is 2 - (-3) = 5.

Example 2:
Input: stones = [7,-6,5,10,5,-2,-6]
Output: 13
Explanation:
- Alice removes all stones, adds 7 + (-6) + 5 + 10 + 5 + (-2) + (-6) = 13 to her score, and places a
  stone of value 13 on the left. stones = [13].
The difference between their scores is 13 - 0 = 13.

Example 3:
Input: stones = [-10,-12]
Output: -22
Explanation:
- Alice can only make one move, which is to remove both stones. She adds (-10) + (-12) = -22 to her
  score and places a stone of value -22 on the left. stones = [-22].
The difference between their scores is (-22) - 0 = -22.

Constraints:

    n == stones.length
    2 <= n <= 105
    -104 <= stones[i] <= 104
"""

import unittest
from typing import List


class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        dp = [[0] * 2 for _ in range(n)]
        sfsum = [0] * n
        sfsum[-1] = stones[-1]
        for i in range(n - 1, 0, -1):
            sfsum[i - 1] = sfsum[i] + stones[i - 1]

        mx, mn = 0, 0
        total = sfsum[0]

        for i in range(n - 2, -1, -1):
            dp[i][0] = mn - total
            dp[i][1] = mx + total

            mx = max(mx, dp[i][0] - sfsum[i + 1])
            mn = min(mn, dp[i][1] + sfsum[i + 1])

        return dp[0][1]


class TestStoneGameVIII(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        stones = [-1, 2, -3, 4, -5]
        self.assertEqual(self.sol.stoneGameVIII(stones), 5)

    def test_example_2(self):
        stones = [7, -6, 5, 10, 5, -2, -6]
        self.assertEqual(self.sol.stoneGameVIII(stones), 13)

    def test_example_3(self):
        stones = [-10, -12]
        self.assertEqual(self.sol.stoneGameVIII(stones), -22)

    def test_example_4(self):
        stones = [
            66,
            -47,
            34,
            -64,
            -88,
            -23,
            63,
            74,
            46,
            39,
            -34,
            -44,
            -49,
            -12,
            36,
            12,
            38,
            47,
            6,
            89,
            -93,
            60,
            -89,
        ]
        self.assertEqual(self.sol.stoneGameVIII(stones), 100)


if __name__ == "__main__":
    unittest.main(verbosity=2)
