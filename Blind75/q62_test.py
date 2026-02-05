"""
Test cases for Unique Paths (LeetCode 62)
https://leetcode.com/problems/unique-paths/
"""

import sys


def get_test_cases():
    """
    Returns list of test cases for Unique Paths.
    Each test case is a tuple: (name, inputs, expected)
    """
    return [
        (
            "Example 1: 3x7 grid",
            {"m": 3, "n": 7},
            28
        ),
        (
            "Example 2: 3x2 grid",
            {"m": 3, "n": 2},
            3
        ),
        (
            "Edge case: 1x1 grid",
            {"m": 1, "n": 1},
            1
        ),
        (
            "Edge case: 1xn grid (single row)",
            {"m": 1, "n": 5},
            1
        ),
        (
            "Edge case: mx1 grid (single column)",
            {"m": 5, "n": 1},
            1
        ),
    ]


def run_tests():
    """Run all test cases."""
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent))

    from Blind75.q62 import Solution
    from test_utils.test_runner import TestRunner

    runner = TestRunner(Solution, "uniquePaths")

    for name, inputs, expected in get_test_cases():
        runner.add_test(name, inputs, expected)

    return runner.run()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
