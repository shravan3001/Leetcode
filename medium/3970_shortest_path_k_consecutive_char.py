"""
https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/description/?envType=daily-question&envId=2026-10-30
3970. Shortest Path With At Most K Consecutive Identical Characters

You are given an integer n representing the number of nodes in a directed weighted graph, numbered from 0 to n - 1. This is represented by a 2D integer array edges, where edges[i] = [ui, vi, wi] represents a directed edge from node ui to node vi with weight wi.
You are also given a string labels of length n, where labels[i] is the character assigned to node i, and an integer k.
Return the minimum total edge weight of a path from node 0 to node n - 1 such that the concatenation of the labels of the nodes along the path contains at most k consecutive identical characters. If no valid path exists, return -1.

Example 1:
Input: n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = "aab", k = 1
Output: 3
Explanation:
The optimal valid path from node 0 to node 2 is as follows:
    Use edges[2] = [0, 2, 3] to reach node 2 with a weight wi = 3.
The corresponding concatenation of labels is "ab", which satisfies at most k = 1 consecutive identical characters. Thus, the answer is 3.

Example 2:
Input: n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = "aab", k = 2
Output: 2
Explanation:
The optimal valid path from node 0 to node 2 is as follows:
    Use edges[0] = [0, 1, 1] to reach node 1 with weight wi = 1.
    Use edges[1] = [1, 2, 1] to reach node 2 with weight wi = 1.
The corresponding concatenation of labels is "aab", which satisfies at most k = 2 consecutive identical characters. Thus, the answer is 2.

Example 3:
Input: n = 3, edges = [[0,1,1],[1,2,1]], labels = "aaa", k = 2
Output: -1
Explanation:
There is no valid path from node 0 to node 2 that satisfies at most k = 2 consecutive identical characters. Thus, the answer is -1.

Constraints:
    1 <= n == labels.length <= 5 * 1e4
    0 <= edges.length <= 5 * 1e4
    edges[i] == [ui, vi, wi]
    0 <= ui, vi <= n - 1
    ui != vi
    1 <= wi <= 1e4
    labels consists of lowercase English letters
    1 <= k <= 50

Hint 1
The validity of a path depends not only on the current node, but also on how many consecutive times the current node’s label has appeared at the end of the path.
Hint 2
Use Dijkstra on states (node, count), where count is the current consecutive run length of labels[node].
Hint 3
When moving from node u to node v, the next count becomes count + 1 if labels[u] == labels[v], otherwise it becomes 1. Ignore transitions where the next count exceeds k.
Hint 4
The answer is the minimum distance among all states ending at node n - 1.
"""

import unittest
import heapq


class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        adj: list[list[tuple[int, int]]] = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))

        K = k + 1  # run lengths are 1..k, index 0 unused
        INF = float("inf")
        dist = [INF] * (n * K)
        dist[0 * K + 1] = 0
        heap: list[tuple[int, int, int]] = [(0, 0, 1)]  # (distance, node, run_len)

        while heap:
            d, u, c = heapq.heappop(heap)
            if d > dist[u * K + c]:
                continue  # stale entry
            if u == n - 1:
                return d  # first pop of target is optimal (also handles n == 1)
            lu = labels[u]
            for v, w in adj[u]:
                nc = c + 1 if labels[v] == lu else 1
                if nc > k:
                    continue
                nd = d + w
                idx = v * K + nc
                if nd < dist[idx]:
                    dist[idx] = nd
                    heapq.heappush(heap, (nd, v, nc))
        return -1


class TestShortestPath(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        n = 3
        edges = [[0, 1, 1], [1, 2, 1], [0, 2, 3]]
        labels = "aab"
        k = 1
        output = 3
        self.assertEqual(self.sol.shortestPath(n, edges, labels, k), output)

    def test_example_2(self):
        n = 3
        edges = [[0, 1, 1], [1, 2, 1], [0, 2, 3]]
        labels = "aab"
        k = 2
        output = 2
        self.assertEqual(self.sol.shortestPath(n, edges, labels, k), output)

    def test_example_3(self):
        n = 3
        edges = [[0, 1, 1], [1, 2, 1]]
        labels = "aaa"
        k = 2
        output = -1
        self.assertEqual(self.sol.shortestPath(n, edges, labels, k), output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
