"""
https://leetcode.com/problems/image-overlap/description/?envType=daily-question&envId=2026-09-13
835. Image Overlap

You are given two images, img1 and img2, represented as binary, square matrices of size n x n. A binary matrix has only 0s and 1s as values.
We translate one image however we choose by sliding all the 1 bits left, right, up, and/or down any number of units. We then place it on top of the other image. We can then calculate the overlap by counting the number of positions that have a 1 in both images.
Note also that a translation does not include any kind of rotation. Any 1 bits that are translated outside of the matrix borders are erased.
Return the largest possible overlap.

Example 1:
Input: img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]
Output: 3
Explanation: We translate img1 to right by 1 unit and down by 1 unit.
The number of positions that have a 1 in both images is 3 (shown in red).

Example 2:
Input: img1 = [[1]], img2 = [[1]]
Output: 1

Example 3:
Input: img1 = [[0]], img2 = [[0]]
Output: 0

Constraints:
    n == img1.length == img1[i].length
    n == img2.length == img2[i].length
    1 <= n <= 30
    img1[i][j] is either 0 or 1.
    img2[i][j] is either 0 or 1.

"""

import unittest
from typing import List
from collections import Counter


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        pts1 = [(i, j) for i in range(n) for j in range(n) if img1[i][j] == 1]
        pts2 = [(i, j) for i in range(n) for j in range(n) if img2[i][j] == 1]

        if not pts1 or not pts2:
            return 0

        counts = Counter()
        for x1, y1 in pts1:
            for x2, y2 in pts2:
                counts[(x1 - x2, y1 - y2)] += 1

        return max(counts.values())


class TestLargestOverlap(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        img1 = [[1, 1, 0], [0, 1, 0], [0, 1, 0]]
        img2 = [[0, 0, 0], [0, 1, 1], [0, 0, 1]]
        output = 3
        self.assertEqual(self.sol.largestOverlap(img1, img2), output)

    def test_example_2(self):
        img1 = [[1]]
        img2 = [[1]]
        output = 1
        self.assertEqual(self.sol.largestOverlap(img1, img2), output)

    def test_example_3(self):
        img1 = [[0]]
        img2 = [[0]]
        output = 0
        self.assertEqual(self.sol.largestOverlap(img1, img2), output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
