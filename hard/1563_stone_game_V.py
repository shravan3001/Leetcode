"""
https://leetcode.com/problems/stone-game-v/description/?envType=daily-question&envId=2026-08-17
1563. Stone Game V

There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.
In each round of the game, Alice divides the row into two non-empty rows (i.e. left row and right row), then Bob calculates the value of each row which is the sum of the values of all the stones in this row. Bob throws away the row which has the maximum value, and Alice's score increases by the value of the remaining row. If the value of the two rows are equal, Bob lets Alice decide which row will be thrown away. The next round starts with the remaining row.
The game ends when there is only one stone remaining. Alice's score is initially zero.
Return the maximum score that Alice can obtain.

Example 1:
Input: stoneValue = [6,2,3,4,5,5]
Output: 18
Explanation: In the first round, Alice divides the row to [6,2,3], [4,5,5]. The left row has the value 11 and the right row has value 14. Bob throws away the right row and Alice's score is now 11.
In the second round Alice divides the row to [6], [2,3]. This time Bob throws away the left row and Alice's score becomes 16 (11 + 5).
The last round Alice has only one choice to divide the row which is [2], [3]. Bob throws away the right row and Alice's score is now 18 (16 + 2). The game ends because only one stone is remaining in the row.

Example 2:
Input: stoneValue = [7,7,7,7,7,7,7]
Output: 28

Example 3:
Input: stoneValue = [4]
Output: 0

Constraints:

    1 <= stoneValue.length <= 500
    1 <= stoneValue[i] <= 106
"""

import unittest
from typing import List


class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        pfsum = [0] * n
        pfsum[0] = stoneValue[0]
        for i in range(1, n):
            pfsum[i] = pfsum[i - 1] + stoneValue[i]

        def get_sum(s: int, e: int):
            return pfsum[e] if s == 0 else pfsum[e] - pfsum[s - 1]

        dp = [[0] * n for _ in range(n)]

        fmax = lambda a, b: a if a > b else b

        def solve(s: int, e: int) -> int:
            if s == e:
                # game ends when row length is 1
                return 0
            if dp[s][e]:
                return dp[s][e]
            ans = 0
            for m in range(s, e):
                lsum = get_sum(s, m)
                rsum = get_sum(m + 1, e)
                if lsum < rsum:
                    ans = fmax(ans, lsum + solve(s, m))
                elif lsum > rsum:
                    ans = fmax(ans, rsum + solve(m + 1, e))
                else:
                    ans = fmax(ans, lsum + fmax(solve(s, m), solve(m + 1, e)))
            dp[s][e] = ans
            return dp[s][e]

        return solve(0, n - 1)


class TestStoneGameV(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        stoneValue = [6, 2, 3, 4, 5, 5]
        self.assertEqual(self.sol.stoneGameV(stoneValue), 18)

    def test_example_2(self):
        stoneValue = [7, 7, 7, 7, 7, 7, 7]
        self.assertEqual(self.sol.stoneGameV(stoneValue), 28)

    def test_example_3(self):
        stoneValue = [4]
        self.assertEqual(self.sol.stoneGameV(stoneValue), 0)

    def test_example_4(self):
        stoneValue = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(self.sol.stoneGameV(stoneValue), 37)


if __name__ == "__main__":
    unittest.main(verbosity=2)
