"""
Test cases for Container with Most Water (LeetCode 11)
https://leetcode.com/problems/container-with-most-water/
"""

import sys


def get_test_cases():
    """
    Returns list of test cases for Container with Most Water.
    Each test case is a tuple: (name, inputs, expected)
    """
    return [
        (
            "Example 1: Standard case",
            {"height": [1, 8, 6, 2, 5, 4, 8, 3, 7]},
            49
        ),
        (
            "Example 2: Two elements",
            {"height": [1, 1]},
            1
        ),
        (
            "Decreasing heights",
            {"height": [5, 4, 3, 2, 1]},
            6
        ),
        (
            "Increasing heights",
            {"height": [1, 2, 3, 4, 5]},
            6
        ),
    ]


def run_tests():
    """Run all test cases."""
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent))

    from Blind75.q11 import Solution
    from test_utils.test_runner import TestRunner

    runner = TestRunner(Solution, "maxArea")

    for name, inputs, expected in get_test_cases():
        runner.add_test(name, inputs, expected)

    return runner.run()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
