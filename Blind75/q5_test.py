"""
Test cases for Longest Palindromic Substring (LeetCode 5)
https://leetcode.com/problems/longest-palindromic-substring/
"""

import sys


def get_test_cases():
    """
    Returns list of test cases for Longest Palindromic Substring.
    Each test case is a tuple: (name, inputs, expected)
    """
    return [
        (
            "Example 1: babad",
            {"s": "babad"},
            ["bab", "aba"]  # Either is valid
        ),
        (
            "Example 2: cbbd",
            {"s": "cbbd"},
            ["bb"]
        ),
        (
            "Single character",
            {"s": "a"},
            ["a"]
        ),
        (
            "All same characters",
            {"s": "aaaa"},
            ["aaaa"]
        ),
    ]


def run_tests():
    """Run all test cases."""
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent))

    from Blind75.q5 import Solution
    from test_utils.test_runner import TestRunner

    def palindrome_comparator(actual, expected_list):
        """Check if actual is one of the valid palindromes."""
        return actual in expected_list

    runner = TestRunner(Solution, "longestPalindrome")

    for name, inputs, expected in get_test_cases():
        runner.add_test(name, inputs, expected, palindrome_comparator)

    return runner.run()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
