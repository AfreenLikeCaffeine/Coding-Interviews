"""
Test cases for Product of Array Except Self (LeetCode 238)
https://leetcode.com/problems/product-of-array-except-self/
"""

import sys


def get_test_cases():
    """
    Returns list of test cases for Product of Array Except Self.
    Each test case is a tuple: (name, inputs, expected)
    """
    return [
        (
            "Example 1: Standard case",
            {"nums": [1, 2, 3, 4]},
            [24, 12, 8, 6]
        ),
        (
            "Example 2: With negative",
            {"nums": [-1, 1, 0, -3, 3]},
            [0, 0, 9, 0, 0]
        ),
        (
            "Two elements",
            {"nums": [2, 3]},
            [3, 2]
        ),
        (
            "Contains zero",
            {"nums": [1, 2, 0, 4]},
            [0, 0, 8, 0]
        ),
    ]


def run_tests():
    """Run all test cases."""
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent))

    from Blind75.q238 import Solution
    from test_utils.test_runner import TestRunner

    runner = TestRunner(Solution, "productExceptSelf")

    for name, inputs, expected in get_test_cases():
        runner.add_test(name, inputs, expected)

    return runner.run()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
