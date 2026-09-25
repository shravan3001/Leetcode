"""
https://leetcode.com/problems/brace-expansion-ii/description/?envType=daily-question&envId=2026-09-25
1096. Brace Expansion II

Under the grammar given below, strings can represent a set of lowercase words. Let R(expr) denote the set of words the expression represents.
The grammar can best be understood through simple examples:
    Single letters represent a singleton set containing that word.
        R("a") = {"a"}
        R("w") = {"w"}
    When we take a comma-delimited list of two or more expressions, we take the union of possibilities.
        R("{a,b,c}") = {"a","b","c"}
        R("{{a,b},{b,c}}") = {"a","b","c"} (notice the final set only contains each word at most once)
    When we concatenate two expressions, we take the set of possible concatenations between two words where the first word comes from the first expression and the second word comes from the second expression.
        R("{a,b}{c,d}") = {"ac","ad","bc","bd"}
        R("a{b,c}{d,e}f{g,h}") = {"abdfg", "abdfh", "abefg", "abefh", "acdfg", "acdfh", "acefg", "acefh"}
Formally, the three rules for our grammar:
    For every lowercase letter x, we have R(x) = {x}.
    For expressions e1, e2, ... , ek with k >= 2, we have R({e1, e2, ...}) = R(e1) ∪ R(e2) ∪ ...
    For expressions e1 and e2, we have R(e1 + e2) = {a + b for (a, b) in R(e1) × R(e2)}, where + denotes concatenation, and × denotes the cartesian product.
Given an expression representing a set of words under the given grammar, return the sorted list of words that the expression represents.

Example 1:
Input: expression = "{a,b}{c,{d,e}}"
Output: ["ac","ad","ae","bc","bd","be"]

Example 2:
Input: expression = "{{a,z},a{b,c},{ab,z}}"
Output: ["a","ab","ac","z"]
Explanation: Each distinct word is written only once in the final answer.

Constraints:
    1 <= expression.length <= 60
    expression[i] consists of '{', '}', ','or lowercase English letters.
    The given expression represents a set of words based on the grammar given in the description.
"""

from typing import List, Set
import unittest


class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        self.expr = expression
        self.i = 0
        result = self._parse_union()
        return sorted(result)

    def _parse_union(self) -> Set[str]:
        """Parse comma-separated terms at the current level: e1,e2,e3,..."""
        sets = [self._parse_concat()]
        while self.i < len(self.expr) and self.expr[self.i] == ",":
            self.i += 1  # skip ','
            sets.append(self._parse_concat())
        result: Set[str] = set()
        for s in sets:
            result |= s
        return result

    def _parse_concat(self) -> Set[str]:
        """Parse a run of concatenated factors until ',' or '}' or end of string."""
        result = {""}
        while self.i < len(self.expr) and self.expr[self.i] not in ",}":
            factor = self._parse_factor()
            result = {a + b for a in result for b in factor}
        return result

    def _parse_factor(self) -> Set[str]:
        """Parse either a '{...}' group or a single letter."""
        if self.expr[self.i] == "{":
            self.i += 1  # skip '{'
            inner = self._parse_union()
            self.i += 1  # skip '}'
            return inner
        else:
            c = self.expr[self.i]
            self.i += 1
            return {c}


class TestBraceExpressionII(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        expression = "{a,b}{c,{d,e}}"
        output = ["ac", "ad", "ae", "bc", "bd", "be"]
        self.assertEqual(self.sol.braceExpansionII(expression), output)

    def test_example_2(self):
        expression = "{{a,z},a{b,c},{ab,z}}"
        output = ["a", "ab", "ac", "z"]
        self.assertEqual(self.sol.braceExpansionII(expression), output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
