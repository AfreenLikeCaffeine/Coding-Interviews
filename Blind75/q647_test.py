"""
Test cases for Palindromic Substrings (LeetCode 647)
https://leetcode.com/problems/palindromic-substrings/
"""

import sys


def get_test_cases():
    """
    Returns list of test cases for Palindromic Substrings.
    Each test case is a tuple: (name, inputs, expected)
    """
    return [
        (
            "Example 1: abc",
            {"s": "abc"},
            3  # a, b, c
        ),
        (
            "Example 2: aaa",
            {"s": "aaa"},
            6  # a, a, a, aa, aa, aaa
        ),
        (
            "Single char",
            {"s": "a"},
            1
        ),
        (
            "Palindrome word",
            {"s": "aba"},
            4  # a, b, a, aba
        ),
    ]


def run_tests():
    """Run all test cases."""
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent))

    from Blind75.q647 import Solution
    from test_utils.test_runner import TestRunner

    runner = TestRunner(Solution, "countSubstrings")

    for name, inputs, expected in get_test_cases():
        runner.add_test(name, inputs, expected)

    return runner.run()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
