"""
1510. Stone Game IV

Alice and Bob take turns playing a game, with Alice starting first.
Initially, there are n stones in a pile. On each player's turn, that player makes a move consisting of removing any non-zero square number of stones in the pile.
Also, if a player cannot make a move, he/she loses the game.
Given a positive integer n, return true if and only if Alice wins the game otherwise return false, assuming both players play optimally.

Example 1:
Input: n = 1
Output: true
Explanation: Alice can remove 1 stone winning the game because Bob doesn't have any moves.

Example 2:
Input: n = 2
Output: false
Explanation: Alice can only remove 1 stone, after that Bob removes the last one winning the game (2 -> 1 -> 0).

Example 3:
Input: n = 4
Output: true
Explanation: n is already a perfect square, Alice can win with one move, removing 4 stones (4 -> 0).

Constraints:

    1 <= n <= 1e5
"""

import unittest


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        dp[1] = True
        for i in range(2, n + 1):
            step = 1
            step_root = 1
            while step <= i:
                if dp[i - step] == False:
                    dp[i] = True
                    break
                step_root += 1
                step = step_root**2
        return dp[n]


class TestWinnerSquareGame(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        n = 1
        self.assertEqual(self.sol.winnerSquareGame(n), True)

    def test_example_2(self):
        n = 2
        self.assertEqual(self.sol.winnerSquareGame(n), False)

    def test_example_3(self):
        n = 4
        self.assertEqual(self.sol.winnerSquareGame(n), True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
