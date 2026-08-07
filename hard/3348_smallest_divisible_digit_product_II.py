"""
https://leetcode.com/problems/smallest-divisible-digit-product-ii/description/?envType=daily-question&envId=2026-08-07

3348. Smallest Divisible Digit Product II
Hard

You are given a string num which represents a positive integer, and an integer t.
A number is called zero-free if none of its digits are 0.
Return a string representing the smallest zero-free number greater than or equal to num such that the product of its digits is divisible by t. If no such number exists, return "-1".

Example 1:
Input: num = "1234", t = 256
Output: "1488"
Explanation:
The smallest zero-free number that is greater than 1234 and has the product of its digits divisible by 256 is 1488, with the product of its digits equal to 256.

Example 2:
Input: num = "12355", t = 50
Output: "12355"
Explanation:
12355 is already zero-free and has the product of its digits divisible by 50, with the product of its digits equal to 150.

Example 3:
Input: num = "11111", t = 26
Output: "-1"
Explanation:
No number greater than 11111 has the product of its digits divisible by 26.

Constraints:
    2 <= num.length <= 2 * 105
    num consists only of digits in the range ['0', '9'].
    num does not contain leading zeros.
    1 <= t <= 1014

hint1: t should only have 2, 3, 5 and 7 as prime factors.
hint2: Find the shortest suffix that must be changed.
hint3: Try to form the string greedily.
"""

import unittest


class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        A = B = C = D = 0
        tt = t
        while tt % 2 == 0:
            tt //= 2
            A += 1
        while tt % 3 == 0:
            tt //= 3
            B += 1
        while tt % 5 == 0:
            tt //= 5
            C += 1
        while tt % 7 == 0:
            tt //= 7
            D += 1
        if tt != 1:
            return "-1"

        digit_exp = {
            1: (0, 0, 0, 0),
            2: (1, 0, 0, 0),
            3: (0, 1, 0, 0),
            4: (2, 0, 0, 0),
            5: (0, 0, 1, 0),
            6: (1, 1, 0, 0),
            7: (0, 0, 0, 1),
            8: (3, 0, 0, 0),
            9: (0, 2, 0, 0),
        }

        INF = float("inf")
        minLen = [
            [[[0] * (D + 1) for _ in range(C + 1)] for _ in range(B + 1)]
            for _ in range(A + 1)
        ]
        for a in range(A + 1):
            for b in range(B + 1):
                for c in range(C + 1):
                    for d in range(D + 1):
                        if a == b == c == d == 0:
                            continue
                        best = INF
                        for dig in range(2, 10):
                            ea, eb, ec, ed = digit_exp[dig]
                            na, nb, nc, nd = (
                                max(a - ea, 0),
                                max(b - eb, 0),
                                max(c - ec, 0),
                                max(d - ed, 0),
                            )
                            # Skip digits that make no progress at all (this would
                            # otherwise self-reference the cell currently being
                            # computed, which still holds its stale initial value).
                            if (na, nb, nc, nd) == (a, b, c, d):
                                continue
                            cand = 1 + minLen[na][nb][nc][nd]
                            if cand < best:
                                best = cand
                        minLen[a][b][c][d] = best

        ml = lambda a, b, c, d: minLen[a][b][c][d]
        clamp = lambda x: x if x > 0 else 0

        n = len(num)
        digits = [int(ch) for ch in num]
        firstZero = n
        for i, ch in enumerate(num):
            if ch == "0":
                firstZero = i
                break
        maxI = firstZero

        prefix = [(0, 0, 0, 0)] * (maxI + 1)
        pa = pb = pc = pd = 0
        for i in range(maxI):
            ea, eb, ec, ed = digit_exp[digits[i]]
            pa += ea
            pb += eb
            pc += ec
            pd += ed
            prefix[i + 1] = (pa, pb, pc, pd)

        def greedy_fill(req, length):
            a, b, c, d = req
            res, left = [], length
            for _ in range(length):
                for cand in range(1, 10):
                    ea, eb, ec, ed = digit_exp[cand]
                    na, nb, nc, nd = (
                        clamp(a - ea),
                        clamp(b - eb),
                        clamp(c - ec),
                        clamp(d - ed),
                    )
                    if ml(na, nb, nc, nd) <= left - 1:
                        res.append(str(cand))
                        a, b, c, d = na, nb, nc, nd
                        left -= 1
                        break
            return "".join(res)

        if maxI == n:
            pa, pb, pc, pd = prefix[n]
            if pa >= A and pb >= B and pc >= C and pd >= D:
                return num

        pivot_upper = firstZero if firstZero < n else n - 1
        answer = None
        for i in range(pivot_upper, -1, -1):
            pa, pb, pc, pd = prefix[i]
            avail = n - i - 1
            for v in range(digits[i] + 1, 10):
                ea, eb, ec, ed = digit_exp[v]
                ra, rb, rc, rd = (
                    clamp(A - pa - ea),
                    clamp(B - pb - eb),
                    clamp(C - pc - ec),
                    clamp(D - pd - ed),
                )
                if ml(ra, rb, rc, rd) <= avail:
                    answer = num[:i] + str(v) + greedy_fill((ra, rb, rc, rd), avail)
                    break
            if answer is not None:
                break

        if answer is not None:
            return answer

        M = ml(A, B, C, D)
        L = max(n + 1, M)
        return greedy_fill((A, B, C, D), L)


class TestSmallestNumber(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        num = "1234"
        t = 256
        self.assertEqual(self.sol.smallestNumber(num, t), "1488")

    def test_example_2(self):
        num = "12355"
        t = 50
        self.assertEqual(self.sol.smallestNumber(num, t), "12355")

    def test_example_3(self):
        num = "11111"
        t = 26
        self.assertEqual(self.sol.smallestNumber(num, t), "-1")


if __name__ == "__main__":
    unittest.main(verbosity=2)
