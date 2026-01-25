"""
Test cases for Word Break (LeetCode 139)
https://leetcode.com/problems/word-break/
"""

import sys


def get_test_cases():
    """
    Returns list of test cases for Word Break.
    Each test case is a tuple: (name, inputs, expected)
    """
    return [
        (
            "Example 1: leetcode",
            {"s": "leetcode", "wordDict": ["leet", "code"]},
            True
        ),
        (
            "Example 2: applepenapple",
            {"s": "applepenapple", "wordDict": ["apple", "pen"]},
            True
        ),
        (
            "Example 3: Cannot segment",
            {"s": "catsandog", "wordDict": ["cats", "dog", "sand", "and", "cat"]},
            False
        ),
        (
            "Single word match",
            {"s": "a", "wordDict": ["a"]},
            True
        ),
    ]


def run_tests():
    """Run all test cases."""
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent))

    from Blind75.q139 import Solution
    from test_utils.test_runner import TestRunner

    runner = TestRunner(Solution, "wordBreak")

    for name, inputs, expected in get_test_cases():
        runner.add_test(name, inputs, expected)

    return runner.run()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
