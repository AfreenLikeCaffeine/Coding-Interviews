"""
Test cases for Find Median from Data Stream (LeetCode 295)
https://leetcode.com/problems/find-median-from-data-stream/
"""

import sys


def get_test_cases():
    """
    Returns list of test cases for MedianFinder.
    Each test case is a tuple: (name, operations, arguments, expected)
    """
    return [
        (
            "Example 1: Basic operations",
            ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"],
            [[], [1], [2], [], [3], []],
            [None, None, None, 1.5, None, 2.0]
        ),
        (
            "Single element",
            ["MedianFinder", "addNum", "findMedian"],
            [[], [5], []],
            [None, None, 5.0]
        ),
        (
            "Descending order",
            ["MedianFinder", "addNum", "addNum", "addNum", "findMedian"],
            [[], [5], [3], [1], []],
            [None, None, None, None, 3.0]
        ),
        (
            "Even count",
            ["MedianFinder", "addNum", "addNum", "addNum", "addNum", "findMedian"],
            [[], [1], [2], [3], [4], []],
            [None, None, None, None, None, 2.5]
        ),
    ]


def run_tests():
    """Run all test cases."""
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent))

    from Blind75.q295 import MedianFinder
    from test_utils.test_runner import ClassTestRunner

    runner = ClassTestRunner(MedianFinder)

    for name, operations, arguments, expected in get_test_cases():
        runner.add_test(name, operations, arguments, expected)

    return runner.run()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
