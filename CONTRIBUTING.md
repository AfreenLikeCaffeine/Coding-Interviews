# Contributing to Coding Interviews

Thank you for your interest in contributing! This guide will help you add new LeetCode solutions to the repository.

## Quick Start with Claude Code

The fastest way to add a new solution is using the `/add-solution` skill in Claude Code:

1. **Solve the problem on LeetCode** and copy your solution

2. **Create the solution file** (e.g., `Blind75/q55.py`):
   ```python
   # https://leetcode.com/problems/jump-game/
   # 55. Jump Game

   class Solution:
       def canJump(self, nums: list[int]) -> bool:
           # Your solution here
           pass
   ```

3. **Run the skill**:
   ```
   /add-solution Blind75/q55.py
   ```

4. **Provide test cases** when prompted (use LeetCode examples + edge cases)

5. **Commit your changes** when tests pass

The skill automatically:
- Refactors code to match project conventions
- Creates the test file with proper structure
- Adds typing imports and fixes annotations
- Runs tests to verify everything works

## Manual Setup

If you prefer to set things up manually, follow these steps:

### 1. Create the Solution File

Create `Blind75/qN.py` (or `Important questions/qN.py`):

```python
# https://leetcode.com/problems/problem-name/
# N. Problem Name

from typing import List  # Add imports as needed


class Solution:
    def methodName(self, nums: List[int]) -> bool:
        """
        Brief description of what the method does.

        :param nums: Description of parameter
        :type nums: List[int]
        :return: Description of return value
        :rtype: bool
        """
        # Your solution here
        pass

# Time complexity: O(n)
# Space complexity: O(1)


if __name__ == "__main__":
    from qN_test import run_tests
    run_tests()
```

### 2. Create the Test File

Create `Blind75/qN_test.py`:

```python
"""
Test cases for Problem Name (LeetCode N)
https://leetcode.com/problems/problem-name/
"""

import sys


def get_test_cases():
    """
    Returns list of test cases.
    Each test case is a tuple: (name, inputs, expected)
    """
    return [
        (
            "Example 1: description",
            {"nums": [2, 3, 1, 1, 4]},
            True
        ),
        (
            "Example 2: description",
            {"nums": [3, 2, 1, 0, 4]},
            False
        ),
        # Add edge cases...
    ]


def run_tests():
    """Run all test cases."""
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

### 3. Run Tests

```bash
python Blind75/qN.py
```

## Code Style Guidelines

### Type Annotations

Use `typing` module imports for consistency:

```python
# Good
from typing import List, Optional, Dict

def method(self, nums: List[int]) -> List[int]:

# Avoid (PEP 585 style - less consistent with existing code)
def method(self, nums: list[int]) -> list[int]:
```

### Docstrings

Include docstrings with parameter descriptions:

```python
def canJump(self, nums: List[int]) -> bool:
    """
    Determine whether it is possible to reach the last index.

    :param nums: Maximum jump length at each position
    :type nums: List[int]
    :return: True if last index is reachable
    :rtype: bool
    """
```

### Complexity Comments

Document time and space complexity:

```python
# Time complexity: O(n)
# Space complexity: O(1)
```

## Working with Data Structures

### Linked Lists

```python
from test_utils.builders import build_linked_list
from test_utils.comparators import compare_linked_lists

runner = TestRunner(
    Solution, "reverseList",
    input_transformer={"head": build_linked_list},
    comparator=compare_linked_lists
)
```

### Binary Trees

```python
from test_utils.builders import build_tree
from test_utils.comparators import compare_trees

runner = TestRunner(
    Solution, "invertTree",
    input_transformer={"root": build_tree},
    comparator=compare_trees
)
```

### Design Problems

Use `ClassTestRunner` for problems like LRUCache, MedianFinder:

```python
from test_utils.test_runner import ClassTestRunner

runner = ClassTestRunner(MedianFinder)
runner.add_test(
    "Example 1",
    ["MedianFinder", "addNum", "findMedian"],
    [[], [1], []],
    [None, None, 1.0]
)
```

## Test Case Guidelines

Include at minimum:
- **LeetCode examples**: The 2-3 examples from the problem description
- **Edge cases**: Empty input, single element, large values, etc.
- **Boundary conditions**: Min/max constraints from the problem

Example test case structure:

```python
(
    "Descriptive name",           # What this test checks
    {"param1": value1},           # Inputs (dict matching method signature)
    expected_output               # Expected return value
),
```

## Submitting Changes

1. Create a branch: `git checkout -b add-qN-solution`
2. Add your solution and tests
3. Verify tests pass: `python Blind75/qN.py`
4. Commit with a descriptive message
5. Push and create a pull request

## Questions?

Open an issue if you have questions or run into problems.
