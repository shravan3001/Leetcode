"""
https://leetcode.com/problems/circle-and-rectangle-overlapping/description/?envType=daily-question&envId=2026-09-19
1401. Circle and Rectangle Overlapping

You are given a circle represented as (radius, xCenter, yCenter) and an axis-aligned rectangle represented as (x1, y1, x2, y2), where (x1, y1) are the coordinates of the bottom-left corner, and (x2, y2) are the coordinates of the top-right corner of the rectangle.
Return true if the circle and rectangle are overlapped otherwise return false. In other words, check if there is any point (xi, yi) that belongs to the circle and the rectangle at the same time.

Example 1:
Input: radius = 1, xCenter = 0, yCenter = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1
Output: true
Explanation: Circle and rectangle share the point (1,0).

Example 2:
Input: radius = 1, xCenter = 1, yCenter = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1
Output: false

Example 3:
Input: radius = 1, xCenter = 0, yCenter = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1
Output: true

Constraints:

    1 <= radius <= 2000
    -1e4 <= xCenter, yCenter <= 1e4
    -1e4 <= x1 < x2 <= 1e4
    -1e4 <= y1 < y2 <= 1e4

Hint:
Locate the closest point of the square to the circle, you can then find the distance from this point to the center of the circle and check if this is less than or equal to the radius.
"""

import unittest


class Solution:
    def checkOverlap(
        self,
        radius: int,
        xCenter: int,
        yCenter: int,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
    ) -> bool:
        # Closest point in the rectangle to the circle's center
        closest_x = max(x1, min(xCenter, x2))
        closest_y = max(y1, min(yCenter, y2))

        dx = xCenter - closest_x
        dy = yCenter - closest_y

        # Compare squared distances to avoid floating point / sqrt
        return dx * dx + dy * dy <= radius * radius


class TestCheckOverlap(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        radius = 1
        xCenter, yCenter = 0, 0
        x1, y1 = 1, -1
        x2, y2 = 3, 1
        output = True
        self.assertEqual(
            self.sol.checkOverlap(radius, xCenter, yCenter, x1, y1, x2, y2), output
        )

    def test_example_2(self):
        radius = 1
        xCenter, yCenter = 1, 1
        x1, y1 = 1, -3
        x2, y2 = 2, -1
        output = False
        self.assertEqual(
            self.sol.checkOverlap(radius, xCenter, yCenter, x1, y1, x2, y2), output
        )

    def test_example_3(self):
        radius = 1
        xCenter, yCenter = 0, 0
        x1, y1 = -1, 0
        x2, y2 = 0, 1
        output = True
        self.assertEqual(
            self.sol.checkOverlap(radius, xCenter, yCenter, x1, y1, x2, y2), output
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
