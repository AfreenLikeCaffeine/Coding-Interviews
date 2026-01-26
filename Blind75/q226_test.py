"""
Test cases for Invert Binary Tree (LeetCode 226)
https://leetcode.com/problems/invert-binary-tree/
"""

import sys


def get_test_cases():
    """
    Returns list of test cases for Invert Binary Tree.
    Each test case is a tuple: (name, inputs, expected)
    """
    return [
        (
            "Example 1: Balanced tree",
            {"root": [4, 2, 7, 1, 3, 6, 9]},
            [4, 7, 2, 9, 6, 3, 1]
        ),
        (
            "Example 2: Small tree",
            {"root": [2, 1, 3]},
            [2, 3, 1]
        ),
        (
            "Empty tree",
            {"root": []},
            []
        ),
        (
            "Single node",
            {"root": [1]},
            [1]
        ),
    ]


def run_tests():
    """Run all test cases."""
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent))

    from Blind75.q226 import Solution
    from test_utils.test_runner import TestRunner
    from test_utils.builders import build_tree
    from test_utils.comparators import compare_trees

    runner = TestRunner(Solution, "invertTree")

    for name, inputs, expected_list in get_test_cases():
        actual_inputs = {
            "root": build_tree(inputs["root"])
        }
        expected = build_tree(expected_list)
        runner.add_test(name, actual_inputs, expected, compare_trees)

    return runner.run()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
