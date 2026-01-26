# Coding Interviews

A curated repository for coding interview preparation. It organizes practice problems and study materials across popular categories, starting with Python solutions for the classic Blind75 list while expanding to other must-know interview topics.

## Prerequisites

- **Python 3.8+** (tested with Python 3.12)
- No external dependencies required (uses only Python standard library)

## Repository Structure
- **Blind75/**: Python solutions to the Blind 75 interview problems, named by their LeetCode question numbers.
- **test_utils/**: Reusable test infrastructure for running and validating solutions.
- **Important questions/**: Additional high-value problems outside the classic Blind75 list.
- **Data Structures/**: Space for notes, implementations, and practice problems.
- **Algorithms/**: Space for algorithm primers, patterns, and problem solutions.

## Running Tests

Each problem has a companion test file. Run tests for any problem directly:

```bash
# Run a single problem's tests
python Blind75/q1.py

# Or run the test file directly
python Blind75/q1_test.py
```

## Adding a New Problem

1. Create the solution file `Blind75/qN.py`:
```python
# N. Problem Name
# https://leetcode.com/problems/problem-name/

from typing import List  # Add imports as needed

class Solution:
    def methodName(self, params) -> ReturnType:
        # Your solution here
        pass

if __name__ == "__main__":
    from qN_test import run_tests
    run_tests()
```

2. Create the test file `Blind75/qN_test.py`:
```python
import sys

def get_test_cases():
    return [
        ("Test name", {"param1": value1, "param2": value2}, expected),
        # Add more test cases...
    ]

def run_tests():
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).parent.parent))

    from Blind75.qN import Solution
    from test_utils.test_runner import TestRunner

    runner = TestRunner(Solution, "methodName")
    for name, inputs, expected in get_test_cases():
        runner.add_test(name, inputs, expected)
    return runner.run()

if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
```

3. Run your tests: `python Blind75/qN.py`

## Test Utilities

The `test_utils/` package provides:

- **data_structures.py**: `ListNode`, `TreeNode`, `Node` classes matching LeetCode definitions
- **builders.py**: Convert Python lists to data structures
  - `build_linked_list([1,2,3])` → linked list
  - `build_tree([3,9,20,None,None,15,7])` → binary tree (level-order)
  - `build_graph([[2,4],[1,3],[2,4],[1,3]])` → graph from adjacency list
- **comparators.py**: Compare data structures for equality
  - `compare_linked_lists()`, `compare_trees()`, `compare_graphs()`
- **test_runner.py**: `TestRunner` for methods, `ClassTestRunner` for design problems

## Contributing

Contributions that expand coverage with clear explanations or additional test cases are welcome.
