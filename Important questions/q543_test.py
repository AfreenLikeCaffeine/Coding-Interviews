"""
Test cases for Diameter of Binary Tree (LeetCode 543)
https://leetcode.com/problems/diameter-of-binary-tree/
"""

import sys


def get_test_cases():
    """
    Returns list of test cases for Diameter of Binary Tree.
    Each test case is a tuple: (name, inputs, expected)
    """
    return [
        (
            "Example 1: Standard tree",
            {"root": [1, 2, 3, 4, 5]},
            3  # Path: 4 -> 2 -> 1 -> 3 or 5 -> 2 -> 1 -> 3
        ),
        (
            "Example 2: Two nodes",
            {"root": [1, 2]},
            1
        ),
        (
            "Single node",
            {"root": [1]},
            0
        ),
        (
            "Empty tree",
            {"root": []},
            0
        ),
        (
            "Left skewed",
            {"root": [1, 2, None, 3, None, 4]},
            3
        ),
    ]


def run_tests():
    """Run all test cases."""
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent))

    # Use importlib for folder with space in name
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "q543",
        Path(__file__).parent / "q543.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    Solution = module.Solution

    from test_utils.test_runner import TestRunner
    from test_utils.builders import build_tree

    runner = TestRunner(Solution, "diameterOfBinaryTree")

    for name, inputs, expected in get_test_cases():
        actual_inputs = {
            "root": build_tree(inputs["root"])
        }
        runner.add_test(name, actual_inputs, expected)

    return runner.run()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
