"""
301. Remove Invalid Parentheses

Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.
Return a list of unique strings that are valid with the minimum number of removals. You may return the answer in any order.

Example 1:
Input: s = "()())()"
Output: ["(())()","()()()"]

Example 2:
Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]

Example 3:
Input: s = ")("
Output: [""]

Constraints:
    1 <= s.length <= 25
    s consists of lowercase English letters and parentheses '(' and ')'.
    There will be at most 20 parentheses in s.
"""

import unittest
from collections import deque


class Solution:
    def is_valid_parantheses(self, s: str) -> bool:
        open_cnt = 0
        for c in s:
            if c == "(":
                open_cnt += 1
            elif c == ")":
                open_cnt -= 1
                if open_cnt < 0:
                    return False
        return open_cnt == 0

    def removeInvalidParentheses(self, s: str) -> list[str]:
        ans: list[str] = []
        q: deque[str] = deque([s])
        visited: set[str] = {s}
        found_ans = False

        while q:
            for _ in range(len(q)):
                curr_s = q.popleft()
                if self.is_valid_parantheses(curr_s):
                    found_ans = True
                    ans.append(curr_s)
                    continue
                if not found_ans:
                    for i, c in enumerate(curr_s):
                        if c == "(" or c == ")":
                            nxt = curr_s[:i] + curr_s[i + 1 :]
                            if nxt not in visited:
                                visited.add(nxt)
                                q.append(nxt)
            if found_ans:
                break
        return ans


class TestRemoveInvalidParantheses(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        s = "()())()"
        output = ["(())()", "()()()"]
        self.assertEqual(set(self.sol.removeInvalidParentheses(s)), set(output))

    def test_example_2(self):
        s = "(a)())()"
        output = ["(a())()", "(a)()()"]
        self.assertEqual(set(self.sol.removeInvalidParentheses(s)), set(output))

    def test_example_3(self):
        s = ")("
        output = [""]
        self.assertEqual(set(self.sol.removeInvalidParentheses(s)), set(output))


if __name__ == "__main__":
    unittest.main(verbosity=2)
