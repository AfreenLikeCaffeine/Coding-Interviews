"""
Test cases for Clone Graph (LeetCode 133)
https://leetcode.com/problems/clone-graph/
"""

import sys


def get_test_cases():
    """
    Returns list of test cases for Clone Graph.
    Each test case is a tuple: (name, inputs, expected)

    Adjacency list format: adj_list[i] contains neighbors of node i+1
    """
    return [
        (
            "Example 1: 4-node graph",
            {"node": [[2, 4], [1, 3], [2, 4], [1, 3]]},
            [[2, 4], [1, 3], [2, 4], [1, 3]]
        ),
        (
            "Example 2: Single node no neighbors",
            {"node": [[]]},
            [[]]
        ),
        (
            "Example 3: Empty graph",
            {"node": []},
            []
        ),
        (
            "Linear graph",
            {"node": [[2], [1, 3], [2]]},
            [[2], [1, 3], [2]]
        ),
    ]


def run_tests():
    """Run all test cases."""
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent))

    from Blind75.q133 import Solution
    from test_utils.test_runner import TestRunner
    from test_utils.builders import build_graph
    from test_utils.comparators import compare_graphs

    runner = TestRunner(Solution, "cloneGraph")

    for name, inputs, expected_adj_list in get_test_cases():
        # Convert adjacency list to graph
        actual_inputs = {
            "node": build_graph(inputs["node"])
        }

        # Build expected graph
        expected = build_graph(expected_adj_list)

        runner.add_test(name, actual_inputs, expected, compare_graphs)

    return runner.run()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
