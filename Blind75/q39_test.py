"""
Test cases for Combination Sum (LeetCode 39)
https://leetcode.com/problems/combination-sum/
"""

import sys


def get_test_cases():
    """
    Returns list of test cases for Combination Sum.
    Each test case is a tuple: (name, inputs, expected)
    """
    return [
        (
            "Example 1: Multiple combinations",
            {"candidates": [2, 3, 6, 7], "target": 7},
            [[2, 2, 3], [7]]
        ),
        (
            "Example 2: Repeated use",
            {"candidates": [2, 3, 5], "target": 8},
            [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        ),
        (
            "Example 3: No solution",
            {"candidates": [2], "target": 1},
            []
        ),
    ]


def run_tests():
    """Run all test cases."""
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent))

    from Blind75.q39 import Solution
    from test_utils.test_runner import TestRunner
    from test_utils.comparators import compare_2d_lists

    def combination_comparator(actual, expected):
        """Compare combinations ignoring order."""
        return compare_2d_lists(actual, expected, order_matters=False)

    runner = TestRunner(Solution, "combinationSum")

    for name, inputs, expected in get_test_cases():
        runner.add_test(name, inputs, expected, combination_comparator)

    return runner.run()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
