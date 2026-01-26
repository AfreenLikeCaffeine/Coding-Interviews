"""
Test cases for Valid Parentheses (LeetCode 20)
https://leetcode.com/problems/valid-parentheses/
"""

import sys


def get_test_cases():
    """
    Returns list of test cases for Valid Parentheses.
    Each test case is a tuple: (name, inputs, expected)
    """
    return [
        (
            "Example 1: Simple valid",
            {"s": "()"},
            True
        ),
        (
            "Example 2: Multiple types valid",
            {"s": "()[]{}"},
            True
        ),
        (
            "Example 3: Invalid mismatch",
            {"s": "(]"},
            False
        ),
        (
            "Nested valid",
            {"s": "([{}])"},
            True
        ),
        (
            "Unclosed bracket",
            {"s": "(("},
            False
        ),
        (
            "Empty string",
            {"s": ""},
            True
        ),
    ]


def run_tests():
    """Run all test cases."""
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent))

    from Blind75.q20 import Solution
    from test_utils.test_runner import TestRunner

    runner = TestRunner(Solution, "isValid")

    for name, inputs, expected in get_test_cases():
        runner.add_test(name, inputs, expected)

    return runner.run()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
