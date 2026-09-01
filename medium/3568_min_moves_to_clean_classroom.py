"""
https://leetcode.com/problems/minimum-moves-to-clean-the-classroom/description/?envType=daily-question&envId=2026-09-01
3568. Minimum Moves to Clean the Classroom

You are given an m x n grid classroom where a student volunteer is tasked with cleaning up litter scattered around the room. Each cell in the grid is one of the following:
    'S': Starting position of the student
    'L': Litter that must be collected (once collected, the cell becomes empty)
    'R': Reset area that restores the student's energy to full capacity, regardless of their current energy level (can be used multiple times)
    'X': Obstacle the student cannot pass through
    '.': Empty space
You are also given an integer energy, representing the student's maximum energy capacity. The student starts with this energy from the starting position 'S'.
Each move to an adjacent cell (up, down, left, or right) costs 1 unit of energy. If the energy reaches 0, the student can only continue if they are on a reset area 'R', which resets the energy to its maximum capacity energy.
Return the minimum number of moves required to collect all litter items, or -1 if it's impossible.

Example 1:
Input: classroom = ["S.", "XL"], energy = 2
Output: 2
Explanation:
    The student starts at cell (0, 0) with 2 units of energy.
    Since cell (1, 0) contains an obstacle 'X', the student cannot move directly downward.
    A valid sequence of moves to collect all litter is as follows:
        Move 1: From (0, 0) → (0, 1) with 1 unit of energy and 1 unit remaining.
        Move 2: From (0, 1) → (1, 1) to collect the litter 'L'.
    The student collects all the litter using 2 moves. Thus, the output is 2.

Example 2:
Input: classroom = ["LS", "RL"], energy = 4
Output: 3
Explanation:
    The student starts at cell (0, 1) with 4 units of energy.
    A valid sequence of moves to collect all litter is as follows:
        Move 1: From (0, 1) → (0, 0) to collect the first litter 'L' with 1 unit of energy used and 3 units remaining.
        Move 2: From (0, 0) → (1, 0) to 'R' to reset and restore energy back to 4.
        Move 3: From (1, 0) → (1, 1) to collect the second litter 'L'.
    The student collects all the litter using 3 moves. Thus, the output is 3.

Example 3:
Input: classroom = ["L.S", "RXL"], energy = 3
Output: -1
Explanation:
No valid path collects all 'L'.

Constraints:
    1 <= m == classroom.length <= 20
    1 <= n == classroom[i].length <= 20
    classroom[i][j] is one of 'S', 'L', 'R', 'X', or '.'
    1 <= energy <= 50
    There is exactly one 'S' in the grid.
    There are at most 10 'L' cells in the grid.

Hint 1
Use BFS with states (x, y, mask, e, steps), initializing with (sx, sy, 0, energy, 0), and for each move update e (–1 per step), update mask on 'L', reset e=energy on 'R', and return steps when mask == fullMask.
Hint 2
Maintain a 3D array bestEnergy[x][y][mask] storing the maximum e seen for each (x,y,mask) and skip any new state with e <= bestEnergy[x][y][mask] to prune.
"""

import unittest
from typing import List, NamedTuple
from collections import deque


class QData(NamedTuple):
    r: int
    c: int
    mask: int
    energy: int


next_positon_offsets = [[0, 1], [0, -1], [1, 0], [-1, 0]]


class Solution:
    def generate_bpm(
        self, classroom: List[str], rows: int, cols: int
    ) -> tuple[dict[tuple[int, int], int], int]:
        bit_pos = 0
        bit_pos_map = {}
        for r in range(rows):
            for c in range(cols):
                if classroom[r][c] == "L":
                    bit_pos_map[(r, c)] = bit_pos
                    bit_pos += 1
        return bit_pos_map, bit_pos

    def get_start_pos(
        self, classroom: List[str], rows: int, cols: int
    ) -> tuple[int, int]:
        for r in range(rows):
            for c in range(cols):
                if classroom[r][c] == "S":
                    return r, c
        # unreachable, S is guaranteed present
        return -1, -1

    def valid_position(self, x, y, rows, cols):
        return 0 <= x < rows and 0 <= y < cols

    def minMoves(self, classroom: List[str], energy: int) -> int:
        rows = len(classroom)
        cols = len(classroom[0])
        bpm, l_count = self.generate_bpm(classroom, rows, cols)
        full_mask = (1 << l_count) - 1

        sx, sy = self.get_start_pos(classroom, rows, cols)

        if full_mask == 0:
            return 0

        mask_dim = 1 << l_count
        dp = [[[-1] * mask_dim for _ in range(cols)] for _ in range(rows)]
        dp[sx][sy][0] = energy

        q: deque[QData] = deque()
        q.append(QData(r=sx, c=sy, mask=0, energy=energy))
        step_count = 0

        while q:
            lvl_c = len(q)
            for _ in range(lvl_c):
                qdata = q.popleft()
                # skip stale/dominated states
                if qdata.energy < dp[qdata.r][qdata.c][qdata.mask]:
                    continue

                c = classroom[qdata.r][qdata.c]
                n_mask = qdata.mask
                if c == "L":
                    bit_pos = bpm[(qdata.r, qdata.c)]
                    n_mask = qdata.mask | (1 << bit_pos)
                    if n_mask == full_mask:
                        return step_count

                eff_energy = energy if c == "R" else qdata.energy
                n_energy = eff_energy - 1
                if n_energy < 0:
                    continue

                for r_off, c_off in next_positon_offsets:
                    nr = qdata.r + r_off
                    nc = qdata.c + c_off
                    if not self.valid_position(nr, nc, rows, cols):
                        continue
                    if classroom[nr][nc] == "X":
                        continue
                    if n_energy > dp[nr][nc][n_mask]:
                        dp[nr][nc][n_mask] = n_energy
                        q.append(QData(r=nr, c=nc, mask=n_mask, energy=n_energy))
            step_count += 1

        return -1


class TestMinMoves(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        classroom = ["S.", "XL"]
        energy = 2
        output = 2
        self.assertEqual(self.sol.minMoves(classroom, energy), output)

    def test_example_2(self):
        classroom = ["LS", "RL"]
        energy = 4
        output = 3
        self.assertEqual(self.sol.minMoves(classroom, energy), output)

    def test_example_3(self):
        classroom = ["L.S", "RXL"]
        energy = 3
        output = -1
        self.assertEqual(self.sol.minMoves(classroom, energy), output)

    def test_no_litter(self):
        classroom = ["S."]
        energy = 5
        output = 0
        self.assertEqual(self.sol.minMoves(classroom, energy), output)

    def test_obstacle_blocks_shortcut(self):
        classroom = ["S X", "X X", "L.."]
        energy = 10
        self.assertEqual(self.sol.minMoves(classroom, energy), 4)


if __name__ == "__main__":
    unittest.main(verbosity=2)
