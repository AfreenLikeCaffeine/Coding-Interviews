"""
Test cases for Jump Game (LeetCode 55)
https://leetcode.com/problems/jump-game/
"""

import sys


def get_test_cases():
    """
    Returns list of test cases for Jump Game.
    Each test case is a tuple: (name, inputs, expected)
    """
    return [
        (
            "Example 1: can reach end",
            {"nums": [2, 3, 1, 1, 4]},
            True
        ),
        (
            "Example 2: cannot reach end",
            {"nums": [3, 2, 1, 0, 4]},
            False
        ),
        (
            "Single element",
            {"nums": [0]},
            True
        ),
        (
            "Two elements, can jump",
            {"nums": [1, 0]},
            True
        ),
        (
            "Two elements, cannot jump",
            {"nums": [0, 1]},
            False
        ),
        (
            "Large jump at start",
            {"nums": [5, 0, 0, 0, 0, 1]},
            True
        ),
        (
            "All zeros except first",
            {"nums": [1, 0, 0, 0]},
            False
        ),
    ]


def run_tests():
    """Run all test cases."""
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent))

    from Blind75.q55 import Solution
    from test_utils.test_runner import TestRunner

    runner = TestRunner(Solution, "canJump")

    for name, inputs, expected in get_test_cases():
        runner.add_test(name, inputs, expected)

    return runner.run()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
