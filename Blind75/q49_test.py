"""
Test cases for Group Anagrams (LeetCode 49)
https://leetcode.com/problems/group-anagrams/
"""

import sys


def get_test_cases():
    """
    Returns list of test cases for Group Anagrams.
    Each test case is a tuple: (name, inputs, expected)
    """
    return [
        (
            "Example 1: Multiple groups",
            {"strs": ["eat", "tea", "tan", "ate", "nat", "bat"]},
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        ),
        (
            "Example 2: Empty string",
            {"strs": [""]},
            [[""]]
        ),
        (
            "Example 3: Single char",
            {"strs": ["a"]},
            [["a"]]
        ),
    ]


def run_tests():
    """Run all test cases."""
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent))

    from Blind75.q49 import Solution
    from test_utils.test_runner import TestRunner

    def anagram_comparator(actual, expected):
        """Compare anagram groups ignoring order of groups and within groups."""
        actual_sorted = {frozenset(group) for group in actual}
        expected_sorted = {frozenset(group) for group in expected}
        return actual_sorted == expected_sorted

    runner = TestRunner(Solution, "groupAnagrams")

    for name, inputs, expected in get_test_cases():
        runner.add_test(name, inputs, expected, anagram_comparator)

    return runner.run()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
