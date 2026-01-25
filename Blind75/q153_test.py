"""
Test cases for Find Minimum in Rotated Sorted Array (LeetCode 153)
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
"""

import sys


def get_test_cases():
    """
    Returns list of test cases for Find Minimum in Rotated Sorted Array.
    Each test case is a tuple: (name, inputs, expected)
    """
    return [
        (
            "Example 1: Rotated",
            {"nums": [3, 4, 5, 1, 2]},
            1
        ),
        (
            "Example 2: More rotation",
            {"nums": [4, 5, 6, 7, 0, 1, 2]},
            0
        ),
        (
            "Example 3: Not rotated",
            {"nums": [11, 13, 15, 17]},
            11
        ),
        (
            "Single element",
            {"nums": [1]},
            1
        ),
        (
            "Two elements rotated",
            {"nums": [2, 1]},
            1
        ),
    ]


def run_tests():
    """Run all test cases."""
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent))

    from Blind75.q153 import Solution
    from test_utils.test_runner import TestRunner

    runner = TestRunner(Solution, "findMin")

    for name, inputs, expected in get_test_cases():
        runner.add_test(name, inputs, expected)

    return runner.run()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
