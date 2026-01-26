"""
Test cases for Maximum Depth of Binary Tree (LeetCode 104)
https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""

import sys


def get_test_cases():
    """
    Returns list of test cases for Maximum Depth of Binary Tree.
    Each test case is a tuple: (name, inputs, expected)
    """
    return [
        (
            "Example 1: Balanced tree",
            {"root": [3, 9, 20, None, None, 15, 7]},
            3
        ),
        (
            "Example 2: Two nodes",
            {"root": [1, None, 2]},
            2
        ),
        (
            "Empty tree",
            {"root": []},
            0
        ),
        (
            "Single node",
            {"root": [1]},
            1
        ),
        (
            "Left-skewed tree",
            {"root": [1, 2, None, 3, None, 4]},
            4
        ),
    ]


def run_tests():
    """Run all test cases."""
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent))

    # Import with the actual filename (104.py, not q104.py)
    import importlib.util
    spec = importlib.util.spec_from_file_location("solution_104", Path(__file__).parent / "104.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    Solution = module.Solution

    from test_utils.test_runner import TestRunner
    from test_utils.builders import build_tree

    runner = TestRunner(Solution, "maxDepth")

    for name, inputs, expected in get_test_cases():
        # Convert list input to TreeNode structure
        actual_inputs = {
            "root": build_tree(inputs["root"])
        }

        runner.add_test(name, actual_inputs, expected)

    return runner.run()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
