"""
https://leetcode.com/problems/longest-substring-of-one-repeating-character/description/?envType=daily-question&envId=2026-08-13
2213. Longest Substring of One Repeating Character

You are given a 0-indexed string s. You are also given a 0-indexed string queryCharacters of length k and a 0-indexed array of integer indices queryIndices of length k, both of which are used to describe k queries.
The ith query updates the character in s at index queryIndices[i] to the character queryCharacters[i].
Return an array lengths of length k where lengths[i] is the length of the longest substring of s consisting of only one repeating character after the ith query is performed.

Example 1:
Input: s = "babacc", queryCharacters = "bcb", queryIndices = [1,3,3]
Output: [3,3,4]
Explanation:
- 1st query updates s = "bbbacc". The longest substring consisting of one repeating character is "bbb" with length 3.
- 2nd query updates s = "bbbccc".
  The longest substring consisting of one repeating character can be "bbb" or "ccc" with length 3.
- 3rd query updates s = "bbbbcc". The longest substring consisting of one repeating character is "bbbb" with length 4.
Thus, we return [3,3,4].

Example 2:
Input: s = "abyzz", queryCharacters = "aa", queryIndices = [2,1]
Output: [2,3]
Explanation:
- 1st query updates s = "abazz". The longest substring consisting of one repeating character is "zz" with length 2.
- 2nd query updates s = "aaazz". The longest substring consisting of one repeating character is "aaa" with length 3.
Thus, we return [2,3].

Constraints:

    1 <= s.length <= 105
    s consists of lowercase English letters.
    k == queryCharacters.length == queryIndices.length
    1 <= k <= 105
    queryCharacters consists of lowercase English letters.
    0 <= queryIndices[i] < s.length
"""

import unittest
from typing import List


class Node:
    def __init__(self):
        self.l_char = ""
        self.l_count = 0
        self.r_char = ""
        self.r_count = 0
        self.max_substr = 0
        self.is_single_char = False

    def __repr__(self):
        return (
            f"Node(max_substr={self.max_substr}, is_single_char={self.is_single_char})"
        )


class SegmentTree:
    def __init__(self, s: str):
        self.n = len(s)
        self.tree = [Node() for _ in range(4 * self.n)]
        self.buildTree(s, 0, 0, self.n - 1)

    def buildTree(self, s: str, node_idx: int, start: int, end: int):
        if start == end:
            self.tree[node_idx].max_substr = 1
            self.tree[node_idx].l_char = s[start]
            self.tree[node_idx].l_count = 1
            self.tree[node_idx].r_char = s[start]
            self.tree[node_idx].r_count = 1
            self.tree[node_idx].is_single_char = True
            return
        mid = (start + end) // 2
        l_node_idx = 2 * node_idx + 1
        r_node_idx = 2 * node_idx + 2
        self.buildTree(s, l_node_idx, start, mid)
        self.buildTree(s, r_node_idx, mid + 1, end)
        self.merge_l_r(node_idx, l_node_idx, r_node_idx)

    def merge_l_r(self, pidx, lidx, ridx):
        # if left and right are single chars substr
        if self.tree[lidx].is_single_char and self.tree[ridx].is_single_char:
            # if both characters match
            if self.tree[lidx].l_char == self.tree[ridx].l_char:
                self.tree[pidx].is_single_char = True
                self.tree[pidx].l_char = self.tree[lidx].l_char
                self.tree[pidx].l_count = (
                    self.tree[lidx].l_count + self.tree[ridx].r_count
                )
                self.tree[pidx].r_char = self.tree[lidx].l_char
                self.tree[pidx].r_count = self.tree[pidx].l_count
                self.tree[pidx].max_substr = self.tree[pidx].l_count
            # if both characters dont match
            else:
                self.tree[pidx].is_single_char = False
                self.tree[pidx].l_char = self.tree[lidx].l_char
                self.tree[pidx].l_count = self.tree[lidx].l_count
                self.tree[pidx].r_char = self.tree[ridx].r_char
                self.tree[pidx].r_count = self.tree[ridx].r_count
                self.tree[pidx].max_substr = max(
                    self.tree[lidx].max_substr, self.tree[ridx].max_substr
                )
        # if left is single char and right isnt
        elif self.tree[lidx].is_single_char and not self.tree[ridx].is_single_char:
            # if char of lnode and lchar of rnode match
            self.tree[pidx].is_single_char = False
            self.tree[pidx].l_char = self.tree[lidx].l_char
            self.tree[pidx].r_char = self.tree[ridx].r_char
            if self.tree[lidx].r_char == self.tree[ridx].l_char:
                self.tree[pidx].l_count = (
                    self.tree[lidx].r_count + self.tree[ridx].l_count
                )
            else:
                self.tree[pidx].l_count = self.tree[lidx].r_count
            self.tree[pidx].r_count = self.tree[ridx].r_count
            self.tree[pidx].max_substr = max(
                self.tree[lidx].max_substr,
                self.tree[ridx].max_substr,
                self.tree[pidx].l_count,
            )
        # if left is not single char and right is
        elif not self.tree[lidx].is_single_char and self.tree[ridx].is_single_char:
            # if rchar of lnode and char of rnode match
            self.tree[pidx].is_single_char = False
            self.tree[pidx].r_char = self.tree[ridx].r_char
            self.tree[pidx].l_char = self.tree[lidx].l_char
            if self.tree[lidx].r_char == self.tree[ridx].l_char:
                self.tree[pidx].r_count = (
                    self.tree[lidx].r_count + self.tree[ridx].l_count
                )
            else:
                self.tree[pidx].r_count = self.tree[ridx].r_count
            self.tree[pidx].l_count = self.tree[lidx].l_count
            self.tree[pidx].max_substr = max(
                self.tree[lidx].max_substr,
                self.tree[ridx].max_substr,
                self.tree[pidx].r_count,
            )
        # if left and right arent single chars
        else:
            self.tree[pidx].is_single_char = False
            self.tree[pidx].l_char = self.tree[lidx].l_char
            self.tree[pidx].l_count = self.tree[lidx].l_count
            self.tree[pidx].r_char = self.tree[ridx].r_char
            self.tree[pidx].r_count = self.tree[ridx].r_count
            new_candidate = (
                self.tree[lidx].r_count + self.tree[ridx].l_count
                if self.tree[lidx].r_char == self.tree[ridx].l_char
                else 0
            )
            self.tree[pidx].max_substr = max(
                self.tree[lidx].max_substr, self.tree[ridx].max_substr, new_candidate
            )

    def update(self, i, c):
        self._update(0, 0, self.n - 1, i, c)

    def _update(self, node_idx, start, end, i, c):
        if start == end:
            # print(f"updating node:{node_idx}")
            self.tree[node_idx].l_char = c
            self.tree[node_idx].r_char = c
            return

        mid = (start + end) // 2
        lidx = 2 * node_idx + 1
        ridx = 2 * node_idx + 2
        if start <= i <= mid:
            self._update(lidx, start, mid, i, c)
        else:
            self._update(ridx, mid + 1, end, i, c)
        self.merge_l_r(node_idx, lidx, ridx)

    def get_max_subtr_rep(self):
        return self.tree[0].max_substr

    def display(self):
        """Public method to trigger the visual print of the tree."""
        print("\n=== Segment Tree Structure ===")
        self._print_tree(node=0, start=0, end=self.n - 1, level=0, prefix="")
        print("==============================\n")

    def _print_tree(self, node, start, end, level, prefix):
        # Base check to ensure we don't read outside the active tree bounds
        if start > end:
            return

        # Visualizing the current node: shows Tree Index, Covered Range, and Sum Value
        node_info = f"[Node {node}] Range [{start},{end}] -> Sum: {self.tree[node]}"
        print(prefix + node_info)

        if start == end:
            return  # It's a leaf node, no children to print

        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2

        # Calculate indentation and branch lines for children
        # '├── ' represents a middle branch, '└── ' represents the final branch
        next_prefix_left = prefix + "├── "
        next_prefix_right = prefix + "└── "

        # Adjust padding for the deeper sub-branches
        indent_left = prefix + "│   "
        indent_right = prefix + "    "

        # Recursively display the left and right subtrees
        self._print_tree(left_child, start, mid, level + 1, indent_left)
        self._print_tree(right_child, mid + 1, end, level + 1, indent_right)


class Solution:

    def longestRepeating(
        self, s: str, queryCharacters: str, queryIndices: List[int]
    ) -> List[int]:
        k = len(queryCharacters)
        ans = [0] * k
        st = SegmentTree(s)
        # st.display()
        for qi in range(k):
            st.update(queryIndices[qi], queryCharacters[qi])
            ans[qi] = st.get_max_subtr_rep()
        return ans


class TestLongestRepeating(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        s = "babacc"
        queryCharacters = "bcb"
        queryIndices = [1, 3, 3]
        self.assertEqual(
            self.sol.longestRepeating(s, queryCharacters, queryIndices), [3, 3, 4]
        )

    def test_example_2(self):
        s = "abyzz"
        queryCharacters = "aa"
        queryIndices = [2, 1]
        self.assertEqual(
            self.sol.longestRepeating(s, queryCharacters, queryIndices), [2, 3]
        )

    def test_example_3(self):
        s = "zzz"
        queryCharacters = "a"
        queryIndices = [0]
        self.assertEqual(
            self.sol.longestRepeating(s, queryCharacters, queryIndices), [2]
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
