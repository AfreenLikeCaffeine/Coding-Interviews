"""
Test cases for Number of Islands (LeetCode 200)
https://leetcode.com/problems/number-of-islands/
"""

import sys


def get_test_cases():
    """
    Returns list of test cases for Number of Islands.
    Each test case is a tuple: (name, inputs, expected)
    """
    return [
        (
            "Example 1: One island",
            {"grid": [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"]
            ]},
            1
        ),
        (
            "Example 2: Three islands",
            {"grid": [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"]
            ]},
            3
        ),
        (
            "Empty grid",
            {"grid": []},
            0
        ),
        (
            "All water",
            {"grid": [["0", "0"], ["0", "0"]]},
            0
        ),
        (
            "All land",
            {"grid": [["1", "1"], ["1", "1"]]},
            1
        ),
    ]


def run_tests():
    """Run all test cases."""
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent))

    from Blind75.q200 import Solution
    from test_utils.test_runner import TestRunner

    runner = TestRunner(Solution, "numIslands")

    for name, inputs, expected in get_test_cases():
        runner.add_test(name, inputs, expected)

    return runner.run()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
