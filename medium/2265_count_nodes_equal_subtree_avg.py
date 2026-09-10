"""
https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/description/?envType=daily-question&envId=2026-09-10
2265. Count Nodes Equal to Average of Subtree

Given the root of a binary tree, return the number of nodes where the value of the node is equal to the average of the values in its subtree.
Note:
    The average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.
    A subtree of root is a tree consisting of root and all of its descendants.

Example 1:
Input: root = [4,8,5,0,1,null,6]
Output: 5
Explanation:
For the node with value 4: The average of its subtree is (4 + 8 + 5 + 0 + 1 + 6) / 6 = 24 / 6 = 4.
For the node with value 5: The average of its subtree is (5 + 6) / 2 = 11 / 2 = 5.
For the node with value 0: The average of its subtree is 0 / 1 = 0.
For the node with value 1: The average of its subtree is 1 / 1 = 1.
For the node with value 6: The average of its subtree is 6 / 1 = 6.

Example 2:
Input: root = [1]
Output: 1
Explanation: For the node with value 1: The average of its subtree is 1 / 1 = 1.

Constraints:
    The number of nodes in the tree is in the range [1, 1000].
    0 <= Node.val <= 1000
"""

from typing import List
import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def make_binary_tree(nums: List[int]) -> TreeNode:
    from collections import deque

    n = len(nums)
    q: deque[tuple[int, TreeNode]] = deque()
    root = TreeNode(nums[0])
    q.append((0, root))
    while q:
        i, r = q.popleft()
        li = 2 * i + 1
        ri = 2 * i + 2
        if li < n and nums[li] != -1:
            r.left = TreeNode(nums[li])
            q.append((li, r.left))
        if ri < n and nums[ri] != -1:
            r.right = TreeNode(nums[ri])
            q.append((ri, r.right))
    return root


class Solution:
    def helper(self, root: TreeNode) -> tuple[int, int, int]:
        sum_l, count_l, ans_l = self.helper(root.left) if root.left else (0, 0, 0)
        sum_r, count_r, ans_r = self.helper(root.right) if root.right else (0, 0, 0)
        s, c, a = sum_l + sum_r + root.val, count_l + count_r + 1, ans_l + ans_r
        avg = s // c
        if avg == root.val:
            a += 1
        return s, c, a

    def averageOfSubtree(self, root: TreeNode) -> int:
        return self.helper(root)[2]


class TestAverageOfSubtree(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        nums = [4, 8, 5, 0, 1, -1, 6]
        root = make_binary_tree(nums)
        output = 5
        self.assertEqual(self.sol.averageOfSubtree(root), output)

    def test_example_2(self):
        nums = [1]
        root = make_binary_tree(nums)
        output = 1
        self.assertEqual(self.sol.averageOfSubtree(root), output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
