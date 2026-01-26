"""
Test cases for Search in Rotated Sorted Array (LeetCode 33)
https://leetcode.com/problems/search-in-rotated-sorted-array/
"""

import sys


def get_test_cases():
    """
    Returns list of test cases for Search in Rotated Sorted Array.
    Each test case is a tuple: (name, inputs, expected)
    """
    return [
        (
            "Example 1: Target found",
            {"nums": [4, 5, 6, 7, 0, 1, 2], "target": 0},
            4
        ),
        (
            "Example 2: Target not found",
            {"nums": [4, 5, 6, 7, 0, 1, 2], "target": 3},
            -1
        ),
        (
            "Example 3: Single element not found",
            {"nums": [1], "target": 0},
            -1
        ),
        (
            "Single element found",
            {"nums": [1], "target": 1},
            0
        ),
        (
            "Not rotated",
            {"nums": [1, 2, 3, 4, 5], "target": 3},
            2
        ),
    ]


def run_tests():
    """Run all test cases."""
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent))

    from Blind75.q33 import Solution
    from test_utils.test_runner import TestRunner

    runner = TestRunner(Solution, "search")

    for name, inputs, expected in get_test_cases():
        runner.add_test(name, inputs, expected)

    return runner.run()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
