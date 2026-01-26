"""
Test cases for Longest Consecutive Sequence (LeetCode 128)
https://leetcode.com/problems/longest-consecutive-sequence/
"""

import sys


def get_test_cases():
    """
    Returns list of test cases for Longest Consecutive Sequence.
    Each test case is a tuple: (name, inputs, expected)
    """
    return [
        (
            "Example 1: Mixed order",
            {"nums": [100, 4, 200, 1, 3, 2]},
            4
        ),
        (
            "Example 2: Longer sequence",
            {"nums": [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]},
            9
        ),
        (
            "Empty array",
            {"nums": []},
            0
        ),
        (
            "Single element",
            {"nums": [1]},
            1
        ),
    ]


def run_tests():
    """Run all test cases."""
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent))

    from Blind75.q128 import Solution
    from test_utils.test_runner import TestRunner

    runner = TestRunner(Solution, "longestConsecutive")

    for name, inputs, expected in get_test_cases():
        runner.add_test(name, inputs, expected)

    return runner.run()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
