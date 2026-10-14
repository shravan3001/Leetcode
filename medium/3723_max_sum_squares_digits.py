"""
https://leetcode.com/problems/maximize-sum-of-squares-of-digits/description/?envType=daily-question&envId=2026-10-14
3723. Maximize Sum of Squares of Digits

You are given two positive integers num and sum.
A positive integer n is good if it satisfies both of the following:
    The number of digits in n is exactly num.
    The sum of digits in n is exactly sum.
The score of a good integer n is the sum of the squares of digits in n.
Return a string denoting the good integer n that achieves the maximum score. If there are multiple possible integers, return the maximum one. If no such integer exists, return an empty string.

Example 1:
Input: num = 2, sum = 3
Output: "30"
Explanation:
There are 3 good integers: 12, 21, and 30.
    The score of 12 is 12 + 22 = 5.
    The score of 21 is 22 + 12 = 5.
    The score of 30 is 32 + 02 = 9.
The maximum score is 9, which is achieved by the good integer 30. Therefore, the answer is "30".

Example 2:
Input: num = 2, sum = 17
Output: "98"
Explanation:
There are 2 good integers: 89 and 98.
    The score of 89 is 82 + 92 = 145.
    The score of 98 is 92 + 82 = 145.
The maximum score is 145. The maximum good integer that achieves this score is 98. Therefore, the answer is "98".

Example 3:
Input: num = 1, sum = 10
Output: ""
Explanation:
There are no integers that have exactly 1 digit and whose digits sum to 10. Therefore, the answer is "".

Constraints:
    1 <= num <= 2 * 1e5
    1 <= sum <= 2 * 1e6
"""

import unittest


class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""
        count = [0] * 10
        d = 9
        used = 0
        while d > 0:
            count[d], sum = divmod(sum, d)
            used += count[d]
            if sum == 0:
                break
            d -= 1
        ans = [str(d) * count[d] for d in range(9, -1, -1)]
        ans.extend("0" * (num - used))
        return "".join(ans)


class TestMaxSumOfSquares(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        num, sum = 2, 3
        output = "30"
        self.assertEqual(self.sol.maxSumOfSquares(num, sum), output)

    def test_example_2(self):
        num, sum = 2, 17
        output = "98"
        self.assertEqual(self.sol.maxSumOfSquares(num, sum), output)

    def test_example_3(self):
        num, sum = 1, 10
        output = ""
        self.assertEqual(self.sol.maxSumOfSquares(num, sum), output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
