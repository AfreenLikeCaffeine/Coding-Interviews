"""
Test cases for Climbing Stairs (LeetCode 70)
https://leetcode.com/problems/climbing-stairs/
"""

import sys


def get_test_cases():
    """
    Returns list of test cases for Climbing Stairs.
    Each test case is a tuple: (name, inputs, expected)
    """
    return [
        (
            "Example 1: 2 stairs",
            {"n": 2},
            2
        ),
        (
            "Example 2: 3 stairs",
            {"n": 3},
            3
        ),
        (
            "1 stair",
            {"n": 1},
            1
        ),
        (
            "5 stairs",
            {"n": 5},
            8
        ),
    ]


def run_tests():
    """Run all test cases."""
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent))

    from Blind75.q70 import Solution
    from test_utils.test_runner import TestRunner

    runner = TestRunner(Solution, "climbStairs")

    for name, inputs, expected in get_test_cases():
        runner.add_test(name, inputs, expected)

    return runner.run()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
