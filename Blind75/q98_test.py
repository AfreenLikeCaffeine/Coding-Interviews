"""
Test cases for Validate Binary Search Tree (LeetCode 98)
https://leetcode.com/problems/validate-binary-search-tree/
"""

import sys


def get_test_cases():
    """
    Returns list of test cases for Validate Binary Search Tree.
    Each test case is a tuple: (name, inputs, expected)
    """
    return [
        (
            "Example 1: Valid BST",
            {"root": [2, 1, 3]},
            True
        ),
        (
            "Example 2: Invalid BST",
            {"root": [5, 1, 4, None, None, 3, 6]},
            False
        ),
        (
            "Single node",
            {"root": [1]},
            True
        ),
        (
            "Empty tree",
            {"root": []},
            True
        ),
        (
            "Left skewed valid",
            {"root": [3, 2, None, 1]},
            True
        ),
    ]


def run_tests():
    """Run all test cases."""
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent))

    from Blind75.q98 import Solution
    from test_utils.test_runner import TestRunner
    from test_utils.builders import build_tree

    runner = TestRunner(Solution, "isValidBST")

    for name, inputs, expected in get_test_cases():
        actual_inputs = {
            "root": build_tree(inputs["root"])
        }
        runner.add_test(name, actual_inputs, expected)

    return runner.run()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
