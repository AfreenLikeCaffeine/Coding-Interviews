"""
Test cases for Merge Two Sorted Lists (LeetCode 21)
https://leetcode.com/problems/merge-two-sorted-lists/
"""

import sys


def get_test_cases():
    """
    Returns list of test cases for Merge Two Sorted Lists.
    Each test case is a tuple: (name, inputs, expected)
    """
    return [
        (
            "Example 1: Both lists non-empty",
            {
                "list1": [1, 2, 4],
                "list2": [1, 3, 4]
            },
            [1, 1, 2, 3, 4, 4]
        ),
        (
            "Example 2: One empty list",
            {
                "list1": [],
                "list2": [0]
            },
            [0]
        ),
        (
            "Example 3: Both empty",
            {
                "list1": [],
                "list2": []
            },
            []
        ),
        (
            "Different lengths",
            {
                "list1": [1, 3, 5, 7, 9],
                "list2": [2, 4]
            },
            [1, 2, 3, 4, 5, 7, 9]
        ),
    ]


def run_tests():
    """Run all test cases."""
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent))

    from Blind75.q21 import Solution
    from test_utils.test_runner import TestRunner
    from test_utils.builders import build_linked_list
    from test_utils.comparators import compare_linked_lists

    runner = TestRunner(Solution, "mergeTwoLists")

    for name, inputs, expected_list in get_test_cases():
        # Convert list inputs to ListNode structures
        actual_inputs = {
            "list1": build_linked_list(inputs["list1"]),
            "list2": build_linked_list(inputs["list2"])
        }

        # Convert expected list to ListNode for comparison
        expected = build_linked_list(expected_list)

        # Add test with custom comparator
        runner.add_test(name, actual_inputs, expected, compare_linked_lists)

    return runner.run()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
