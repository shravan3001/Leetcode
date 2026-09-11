"""
https://leetcode.com/problems/unique-3-digit-even-numbers/description/?envType=daily-question&envId=2026-09-11
3483. Unique 3-Digit Even Numbers

You are given an array of digits called digits. Your task is to determine the number of distinct three-digit even numbers that can be formed using these digits.
Note: Each copy of a digit can only be used once per number, and there may not be leading zeros.

Example 1:
Input: digits = [1,2,3,4]
Output: 12
Explanation: The 12 distinct 3-digit even numbers that can be formed are 124, 132, 134, 142, 214, 234, 312, 314, 324, 342, 412, and 432. Note that 222 cannot be formed because there is only 1 copy of the digit 2.

Example 2:
Input: digits = [0,2,2]
Output: 2
Explanation: The only 3-digit even numbers that can be formed are 202 and 220. Note that the digit 2 can be used twice because it appears twice in the array.

Example 3:
Input: digits = [6,6,6]
Output: 1
Explanation: Only 666 can be formed.

Example 4:
Input: digits = [1,3,5]
Output: 0
Explanation: No even 3-digit numbers can be formed.

Constraints:
    3 <= digits.length <= 10
    0 <= digits[i] <= 9
"""

import unittest
from typing import List
from collections import Counter, defaultdict


class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        c = Counter(digits)
        evens: set[int] = set()
        for i in range(100, 1000, 2):
            x = i
            ds = defaultdict(int)
            skip = False
            while x:
                ds[x % 10] += 1
                x //= 10
            for d, cnt in ds.items():
                if c.get(d, 0) < cnt:
                    skip = True
                    break
            if not skip:
                evens.add(i)
        return len(evens)


class TestTotalNumbers(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        digits = [1, 2, 3, 4]
        output = 12
        self.assertEqual(self.sol.totalNumbers(digits), output)

    def test_example_2(self):
        digits = [0, 2, 2]
        output = 2
        self.assertEqual(self.sol.totalNumbers(digits), output)

    def test_example_3(self):
        digits = [6, 6, 6]
        output = 1
        self.assertEqual(self.sol.totalNumbers(digits), output)

    def test_example_4(self):
        digits = [1, 3, 5]
        output = 0
        self.assertEqual(self.sol.totalNumbers(digits), output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
