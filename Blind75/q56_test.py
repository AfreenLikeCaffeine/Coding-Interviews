"""
Test cases for Merge Intervals (LeetCode 56)
https://leetcode.com/problems/merge-intervals/
"""

import sys


def get_test_cases():
    """
    Returns list of test cases for Merge Intervals.
    Each test case is a tuple: (name, inputs, expected)
    """
    return [
        (
            "Example 1: Overlapping intervals",
            {"intervals": [[1, 3], [2, 6], [8, 10], [15, 18]]},
            [[1, 6], [8, 10], [15, 18]]
        ),
        (
            "Example 2: Fully overlapping",
            {"intervals": [[1, 4], [4, 5]]},
            [[1, 5]]
        ),
        (
            "Single interval",
            {"intervals": [[1, 5]]},
            [[1, 5]]
        ),
        (
            "No overlap",
            {"intervals": [[1, 2], [4, 5], [7, 8]]},
            [[1, 2], [4, 5], [7, 8]]
        ),
    ]


def run_tests():
    """Run all test cases."""
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent))

    from Blind75.q56 import Solution
    from test_utils.test_runner import TestRunner

    runner = TestRunner(Solution, "merge")

    for name, inputs, expected in get_test_cases():
        runner.add_test(name, inputs, expected)

    return runner.run()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
