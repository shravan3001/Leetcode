"""
https://leetcode.com/problems/palindromic-path-queries-in-a-tree/description/?envType=daily-question&envId=2026-10-29
3841. Palindromic Path Queries in a Tree

You are given an undirected tree with n nodes labeled 0 to n - 1. This is represented by a 2D array edges of length n - 1, where edges[i] = [ui, vi] indicates an undirected edge between nodes ui and vi.
You are also given a string s of length n consisting of lowercase English letters, where s[i] represents the character assigned to node i.
You are also given a string array queries, where each queries[i] is either:
    "update ui c": Change the character at node ui to c. Formally, update s[ui] = c.
    "query ui vi": Determine whether the string formed by the characters on the unique path from ui to vi (inclusive) can be rearranged into a palindrome.
Return a boolean array answer, where answer[j] is true if the jth query of type "query ui vi"​​​​​​​ can be rearranged into a palindrome, and false otherwise.

Example 1:
Input: n = 3, edges = [[0,1],[1,2]], s = "aac", queries = ["query 0 2","update 1 b","query 0 2"]
Output: [true,false]
Explanation:
    "query 0 2": Path 0 → 1 → 2 gives "aac", which can be rearranged to form "aca", a palindrome. Thus, answer[0] = true.
    "update 1 b": Update node 1 to 'b', now s = "abc".
    "query 0 2": Path characters are "abc", which cannot be rearranged to form a palindrome. Thus, answer[1] = false.
Thus, answer = [true, false].

Example 2:
Input: n = 4, edges = [[0,1],[0,2],[0,3]], s = "abca", queries = ["query 1 2","update 0 b","query 2 3","update 3 a","query 1 3"]
Output: [false,false,true]
Explanation:
    "query 1 2": Path 1 → 0 → 2 gives "bac", which cannot be rearranged to form a palindrome. Thus, answer[0] = false.
    "update 0 b": Update node 0 to 'b', now s = "bbca".
    "query 2 3": Path 2 → 0 → 3 gives "cba", which cannot be rearranged to form a palindrome. Thus, answer[1] = false.
    "update 3 a": Update node 3 to 'a', s = "bbca".
    "query 1 3": Path 1 → 0 → 3 gives "bba", which can be rearranged to form "bab", a palindrome. Thus, answer[2] = true.
Thus, answer = [false, false, true].

Constraints:
    1 <= n == s.length <= 5 * 1e4
    edges.length == n - 1
    edges[i] = [ui, vi]
    0 <= ui, vi <= n - 1
    s consists of lowercase English letters.
    The input is generated such that edges represents a valid tree.
    1 <= queries.length <= 5 * 1e4
        queries[i] = "update ui c" or
        queries[i] = "query ui vi"
        0 <= ui, vi <= n - 1
        c is a lowercase English letter.

Hint 1
Use heavy light decomposition to break each path query into O(log n) segments.
Hint 2
Represent characters as a 26-bit mask and maintain segment data with XOR. A path can form a palindrome if the resulting mask has at most one bit set.
"""

import unittest


class Solution:
    def palindromePath(
        self, n: int, edges: list[list[int]], s: str, queries: list[str]
    ) -> list[bool]:
        # Idea:
        #   P[v] = XOR of 26-bit char masks on the root -> v path.
        #   path(u, v) mask = P[u] ^ P[v] ^ bit(lca(u, v))
        #   Updating node u flips P[x] for every x in subtree(u) by the same
        #   mask delta, i.e. a range XOR on the Euler tour, handled with a
        #   Fenwick tree (range update, point query).
        adj: list[list[int]] = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        chars = [ord(c) - 97 for c in s]

        parent = [-1] * n
        depth = [0] * n
        tin = [0] * n
        base = [0] * n  # root->v XOR mask for the initial string
        order: list[int] = []

        base[0] = 1 << chars[0]
        stack = [0]
        while stack:  # iterative preorder: subtrees are contiguous
            u = stack.pop()
            tin[u] = len(order)
            order.append(u)
            for w in adj[u]:
                if w != parent[u]:
                    parent[w] = u
                    depth[w] = depth[u] + 1
                    base[w] = base[u] ^ (1 << chars[w])
                    stack.append(w)

        size = [1] * n
        for u in reversed(order):
            if parent[u] != -1:
                size[parent[u]] += size[u]

        # Binary lifting for LCA
        LOG = max(1, (n - 1).bit_length())
        up = [[0] * n for _ in range(LOG)]
        up[0] = [p if p != -1 else 0 for p in parent]
        for k in range(1, LOG):
            prev, cur = up[k - 1], up[k]
            for v in range(n):
                cur[v] = prev[prev[v]]

        def lca(a: int, b: int) -> int:
            if depth[a] < depth[b]:
                a, b = b, a
            diff = depth[a] - depth[b]
            for k in range(LOG):
                if diff >> k & 1:
                    a = up[k][a]
            if a == b:
                return a
            for k in range(LOG - 1, -1, -1):
                if up[k][a] != up[k][b]:
                    a, b = up[k][a], up[k][b]
            return up[0][a]

        # Fenwick tree over XOR (1-indexed)
        tree = [0] * (n + 2)

        def bit_xor(i: int, val: int) -> None:
            i += 1
            while i <= n + 1:
                tree[i] ^= val
                i += i & -i

        def prefix(i: int) -> int:
            i += 1
            res = 0
            while i > 0:
                res ^= tree[i]
                i -= i & -i
            return res

        ans: list[bool] = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                new = ord(parts[2]) - 97
                if new != chars[u]:
                    delta = (1 << chars[u]) ^ (1 << new)
                    chars[u] = new
                    bit_xor(tin[u], delta)
                    bit_xor(tin[u] + size[u], delta)
            else:
                u, v = int(parts[1]), int(parts[2])
                l = lca(u, v)
                mask = (
                    base[u]
                    ^ prefix(tin[u])
                    ^ base[v]
                    ^ prefix(tin[v])
                    ^ (1 << chars[l])
                )
                ans.append(mask & (mask - 1) == 0)
        return ans


class TestPalindromePath(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        n = 3
        edges = [[0, 1], [1, 2]]
        s = "aac"
        queries = ["query 0 2", "update 1 b", "query 0 2"]
        output = [True, False]
        self.assertEqual(self.sol.palindromePath(n, edges, s, queries), output)

    def test_example_2(self):
        n = 4
        edges = [[0, 1], [0, 2], [0, 3]]
        s = "abca"
        queries = ["query 1 2", "update 0 b", "query 2 3", "update 3 a", "query 1 3"]
        output = [False, False, True]
        self.assertEqual(self.sol.palindromePath(n, edges, s, queries), output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
