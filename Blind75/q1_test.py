"""
Test cases for Two Sum (LeetCode 1)
https://leetcode.com/problems/two-sum/
"""

import sys


def get_test_cases():
    """
    Returns list of test cases for Two Sum.
    Each test case is a tuple: (name, inputs, expected)
    """
    return [
        (
            "Example 1: Basic case",
            {"nums": [2, 7, 11, 15], "target": 9},
            [0, 1]
        ),
        (
            "Example 2: Two elements",
            {"nums": [3, 3], "target": 6},
            [0, 1]
        ),
        (
            "Edge case: Negative numbers",
            {"nums": [-1, -2, -3, -4, -5], "target": -8},
            [2, 4]
        ),
        (
            "Edge case: Zero in array",
            {"nums": [0, 4, 3, 0], "target": 0},
            [0, 3]
        ),
    ]


def run_tests():
    """Run all test cases."""
    from pathlib import Path

    # Add parent directory to path for imports
    sys.path.insert(0, str(Path(__file__).parent.parent))

    from Blind75.q1 import Solution
    from test_utils.test_runner import TestRunner

    runner = TestRunner(Solution, "twoSum")

    for name, inputs, expected in get_test_cases():
        runner.add_test(name, inputs, expected)

    return runner.run()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
