"""
https://leetcode.com/problems/remove-methods-from-project/description/?envType=daily-question&envId=2026-08-05

Example 1:
Input: n = 4, k = 1, invocations = [[1,2],[0,1],[3,2]]
Output: [0,1,2,3]

Example 2:
Input: n = 5, k = 0, invocations = [[1,2],[0,2],[0,1],[3,4]]
Output: [3,4]
"""

import unittest
from collections import defaultdict, deque
from typing import List, Set


class Solution:
    def remainingMethods(
        self, n: int, k: int, invocations: List[List[int]]
    ) -> List[int]:
        graph = defaultdict(list)
        for a, b in invocations:
            graph[a].append(b)

        # 1) Suspicious set: everything reachable from k (k included).
        suspicious = {k}
        dq = deque([k])
        while dq:
            u = dq.popleft()
            for v in graph[u]:
                if v not in suspicious:
                    suspicious.add(v)
                    dq.append(v)

        # 2) All-or-nothing rule: if ANY method outside the suspicious set
        # invokes a method inside it, we cannot remove the group at all.
        for a, b in invocations:
            if b in suspicious and a not in suspicious:
                return list(range(n))

        # 3) Otherwise the whole suspicious set is safe to remove.
        return sorted(set(range(n)) - suspicious)


class TestRemainingMethods(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        n, k = 4, 1
        invocations = [[1, 2], [0, 1], [3, 2]]
        self.assertEqual(self.sol.remainingMethods(n, k, invocations), [0, 1, 2, 3])

    def test_example_2(self):
        n, k = 5, 0
        invocations = [[1, 2], [0, 2], [0, 1], [3, 4]]
        self.assertEqual(self.sol.remainingMethods(n, k, invocations), [3, 4])

    def test_no_invocations(self):
        # nothing calls anything, only k itself is "suspicious" and no one
        # relies on it, so it is removed and everyone else stays
        n, k = 3, 0
        invocations = []
        self.assertEqual(self.sol.remainingMethods(n, k, invocations), [1, 2])

    def test_single_method(self):
        # n = 1: k has no external caller possible, so it's removed
        n, k = 1, 0
        invocations = []
        self.assertEqual(self.sol.remainingMethods(n, k, invocations), [])

    def test_external_caller_rescues_whole_chain(self):
        # 1 -> 0 -> 2 : k=0 calls 2, but 0 is itself called externally by 1,
        # so the whole chain 0 -> 2 is legitimate and nothing is removed
        n, k = 3, 0
        invocations = [[1, 0], [0, 2]]
        self.assertEqual(self.sol.remainingMethods(n, k, invocations), [0, 1, 2])

    def test_cycle_within_suspicious_chain(self):
        # k=0 -> 1 -> 0 (cycle), nobody outside calls into the cycle
        n, k = 3, 0
        invocations = [[0, 1], [1, 0]]
        self.assertEqual(self.sol.remainingMethods(n, k, invocations), [2])


if __name__ == "__main__":
    unittest.main(verbosity=2)
