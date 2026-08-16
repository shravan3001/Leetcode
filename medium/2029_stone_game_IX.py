"""
https://leetcode.com/problems/stone-game-ix/description/?envType=daily-question&envId=2026-08-16
2029. Stone Game IX

Alice and Bob continue their games with stones. There is a row of n stones, and each stone has an associated value. You are given an integer array stones, where stones[i] is the value of the ith stone.
Alice and Bob take turns, with Alice starting first. On each turn, the player may remove any stone from stones. The player who removes a stone loses if the sum of the values of all removed stones is divisible by 3. Bob will win automatically if there are no remaining stones (even if it is Alice's turn).
Assuming both players play optimally, return true if Alice wins and false if Bob wins.

Example 1:
Input: stones = [2,1]
Output: true
Explanation: The game will be played as follows:
- Turn 1: Alice can remove either stone.
- Turn 2: Bob removes the remaining stone.
The sum of the removed stones is 1 + 2 = 3 and is divisible by 3. Therefore, Bob loses and Alice wins the game.

Example 2:
Input: stones = [2]
Output: false
Explanation: Alice will remove the only stone, and the sum of the values on the removed stones is 2.
Since all the stones are removed and the sum of values is not divisible by 3, Bob wins the game.

Example 3:
Input: stones = [5,1,2,4,3]
Output: false
Explanation: Bob will always win. One possible way for Bob to win is shown below:
- Turn 1: Alice can remove the second stone with value 1. Sum of removed stones = 1.
- Turn 2: Bob removes the fifth stone with value 3. Sum of removed stones = 1 + 3 = 4.
- Turn 3: Alices removes the fourth stone with value 4. Sum of removed stones = 1 + 3 + 4 = 8.
- Turn 4: Bob removes the third stone with value 2. Sum of removed stones = 1 + 3 + 4 + 2 = 10.
- Turn 5: Alice removes the first stone with value 5. Sum of removed stones = 1 + 3 + 4 + 2 + 5 = 15.
Alice loses the game because the sum of the removed stones (15) is divisible by 3. Bob wins the game.

Constraints:

    1 <= stones.length <= 105
    1 <= stones[i] <= 104
"""

import unittest
from typing import List


class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        rem = [0] * 3
        for x in stones:
            rem[x % 3] += 1
        def play(s: int, r0: int, r1: int, r2: int, Alice: bool):
            if not sum([r0, r1, r2]):
                return False
            if s == 1:
                if r1:
                    return play(2, r0, r1 - 1, r2, not Alice)
                elif r0:
                    return play(1, r0 - 1, r1, r2, not Alice)
                else:
                    return not Alice
            elif s == 2:
                if r2:
                    return play(1, r0, r1, r2 - 1, not Alice)
                elif r0:
                    return play(2, r0 - 1, r1, r2, not Alice)
                else:
                    return not Alice

        return (
            rem[1]
            and play(1, rem[0], rem[1] - 1, rem[2], False)
            or rem[2]
            and play(2, rem[0], rem[1], rem[2] - 1, False)
        )


class TestStoneGameIX(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        stones = [2, 1]
        self.assertEqual(self.sol.stoneGameIX(stones), True)

    def test_example_2(self):
        stones = [2]
        self.assertEqual(self.sol.stoneGameIX(stones), False)

    def test_example_3(self):
        stones = [5, 1, 2, 4, 3]
        self.assertEqual(self.sol.stoneGameIX(stones), False)


if __name__ == "__main__":
    unittest.main(verbosity=2)
