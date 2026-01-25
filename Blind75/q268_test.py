"""
Test cases for Missing Number (LeetCode 268)
https://leetcode.com/problems/missing-number/
"""

import sys


def get_test_cases():
    """
    Returns list of test cases for Missing Number.
    Each test case is a tuple: (name, inputs, expected)
    """
    return [
        (
            "Example 1: Missing 2",
            {"nums": [3, 0, 1]},
            2
        ),
        (
            "Example 2: Missing 2",
            {"nums": [0, 1]},
            2
        ),
        (
            "Example 3: Missing 8",
            {"nums": [9, 6, 4, 2, 3, 5, 7, 0, 1]},
            8
        ),
        (
            "Missing 0",
            {"nums": [1]},
            0
        ),
    ]


def run_tests():
    """Run all test cases."""
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent))

    from Blind75.q268 import Solution
    from test_utils.test_runner import TestRunner

    runner = TestRunner(Solution, "missingNumber")

    for name, inputs, expected in get_test_cases():
        runner.add_test(name, inputs, expected)

    return runner.run()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
