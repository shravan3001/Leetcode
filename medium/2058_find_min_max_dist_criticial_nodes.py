"""
https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/description/?envType=daily-question&envId=2026-08-31
2058. Find the Minimum and Maximum Number of Nodes Between Critical Points

A critical point in a linked list is defined as either a local maxima or a local minima.
A node is a local maxima if the current node has a value strictly greater than the previous node and the next node.
A node is a local minima if the current node has a value strictly smaller than the previous node and the next node.
Note that a node can only be a local maxima/minima if there exists both a previous node and a next node.
Given a linked list head, return an array of length 2 containing [minDistance, maxDistance] where minDistance is the minimum distance between any two distinct critical points and maxDistance is the maximum distance between any two distinct critical points. If there are fewer than two critical points, return [-1, -1].

Example 1:
Input: head = [3,1]
Output: [-1,-1]
Explanation: There are no critical points in [3,1].

Example 2:
Input: head = [5,3,1,2,5,1,2]
Output: [1,3]
Explanation: There are three critical points:
- [5,3,1,2,5,1,2]: The third node is a local minima because 1 is less than 3 and 2.
- [5,3,1,2,5,1,2]: The fifth node is a local maxima because 5 is greater than 2 and 1.
- [5,3,1,2,5,1,2]: The sixth node is a local minima because 1 is less than 5 and 2.
The minimum distance is between the fifth and the sixth node. minDistance = 6 - 5 = 1.
The maximum distance is between the third and the sixth node. maxDistance = 6 - 3 = 3.

Example 3:
Input: head = [1,3,2,2,3,2,2,2,7]
Output: [3,3]
Explanation: There are two critical points:
- [1,3,2,2,3,2,2,2,7]: The second node is a local maxima because 3 is greater than 1 and 2.
- [1,3,2,2,3,2,2,2,7]: The fifth node is a local maxima because 3 is greater than 2 and 2.
Both the minimum and maximum distances are between the second and the fifth node.
Thus, minDistance and maxDistance is 5 - 2 = 3.
Note that the last node is not considered a local maxima because it does not have a next node.

Constraints:

    The number of nodes in the list is in the range [2, 105].
    1 <= Node.val <= 105
"""

import unittest
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: ListNode) -> List[int]:
        prv = head
        c = head.next
        if head.next.next is None:
            return [-1, -1]
        nxt = head.next.next
        c_idx = 1
        cps: List[int] = []

        def is_cp(prv: ListNode, c: ListNode, nxt: ListNode):
            return (prv.val < c.val and c.val > nxt.val) or (
                prv.val > c.val and c.val < nxt.val
            )

        if is_cp(prv, c, nxt):
            cps.append(c_idx)

        while nxt.next:
            prv = c
            c = nxt
            nxt = nxt.next
            c_idx += 1
            if is_cp(prv, c, nxt):
                cps.append(c_idx)

        if len(cps) < 2:
            return [-1, -1]

        minD = float("inf")
        maxD = cps[-1] - cps[0]
        for cp0, cp1 in zip(cps, cps[1:]):
            minD = min(cp1 - cp0, minD)

        return [minD, maxD]


class TestNodesBetweenCriticalPoints(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def make_list(self, nums: List[int]):
        head = ListNode(nums[0])
        curr = head
        for x in nums[1:]:
            nn = ListNode(x)
            curr.next = nn
            curr = nn
        return head

    def test_example_1(self):
        head = [3, 1]
        head = self.make_list(head)
        self.assertEqual(self.sol.nodesBetweenCriticalPoints(head), [-1, -1])

    def test_example_2(self):
        head = [5, 3, 1, 2, 5, 1, 2]
        head = self.make_list(head)
        self.assertEqual(self.sol.nodesBetweenCriticalPoints(head), [1, 3])

    def test_example_3(self):
        head = [1, 3, 2, 2, 3, 2, 2, 2, 7]
        head = self.make_list(head)
        self.assertEqual(self.sol.nodesBetweenCriticalPoints(head), [3, 3])


if __name__ == "__main__":
    unittest.main(verbosity=2)
