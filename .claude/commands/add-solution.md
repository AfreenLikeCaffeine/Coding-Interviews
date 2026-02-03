# Add LeetCode Solution

This skill sets up a new LeetCode solution file with tests, following the repository conventions.

## Usage

```
/add-solution <path-to-solution-file>
```

Example: `/add-solution Blind75/q55.py`

## Arguments

- `$ARGUMENTS` - Path to the solution file (e.g., `Blind75/q55.py`)

## Instructions

When this skill is invoked with a solution file path:

### 1. Read and Analyze the Solution File

Read the file at `$ARGUMENTS` and extract:
- **Problem number**: From the filename (e.g., `q55.py` → `55`)
- **Problem name**: From the comment at the top (e.g., `# 55. Jump Game`)
- **LeetCode URL**: From the comment (e.g., `# https://leetcode.com/problems/jump-game/`)
- **Method name**: The main method in the `Solution` class (e.g., `canJump`)
- **Method signature**: Parameters and return type
- **Folder**: The parent folder (e.g., `Blind75` or `Important questions`)

### 2. Refactor the Solution File

Update the solution file to match project conventions:

a) **Add typing imports** if the code uses type hints like `list[int]`:
   - Add `from typing import List` (or `List, Optional, Dict` as needed)
   - Replace `list[int]` with `List[int]`, `dict[str, int]` with `Dict[str, int]`, etc.

b) **Ensure proper file header**:
   ```python
   # https://leetcode.com/problems/problem-name/
   # N. Problem Name
   ```

c) **Add the test runner block** at the end of the file if not present:
   ```python
   if __name__ == "__main__":
       from qN_test import run_tests
       run_tests()
   ```

d) **Ensure complexity comments** are present at the bottom:
   ```python
   # Time complexity: O(...)
   # Space complexity: O(...)
   ```

### 3. Create the Test File

Create a test file at `{folder}/qN_test.py` with this structure:

```python
"""
Test cases for {Problem Name} (LeetCode {N})
https://leetcode.com/problems/{problem-slug}/
"""

import sys


def get_test_cases():
    """
    Returns list of test cases for {Problem Name}.
    Each test case is a tuple: (name, inputs, expected)
    """
    return [
        (
            "Example 1: {description}",
            {"{param1}": value1, "{param2}": value2},
            expected1
        ),
        (
            "Example 2: {description}",
            {"{param1}": value1, "{param2}": value2},
            expected2
        ),
        # Add edge cases...
    ]


def run_tests():
    """Run all test cases."""
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent))

    from {folder}.q{N} import Solution
    from test_utils.test_runner import TestRunner

    runner = TestRunner(Solution, "{methodName}")

    for name, inputs, expected in get_test_cases():
        runner.add_test(name, inputs, expected)

    return runner.run()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
```

### 4. Add Test Cases

Ask the user for test cases. For each test case, gather:
- A descriptive name
- Input values (matching the method parameters)
- Expected output

Include at minimum:
- The LeetCode example test cases (usually 2-3)
- At least one edge case

For problems using data structures, use the appropriate builders:
- **Linked lists**: `{"head": [1, 2, 3]}` with `input_transformer={"head": build_linked_list}`
- **Binary trees**: `{"root": [3, 9, 20, None, None, 15, 7]}` with `input_transformer={"root": build_tree}`
- **Graphs**: Use `build_graph` for adjacency lists

### 5. Verify the Solution

Run the tests to ensure everything works:

```bash
python {folder}/qN.py
```

If tests fail, work with the user to fix issues.

### 6. Summary

After completion, provide a summary:
- Files created/modified
- Number of test cases added
- Test results (pass/fail)
- Remind user to commit when ready

## Special Cases

### Design Problems (ClassTestRunner)

For design problems like MedianFinder, MinStack, etc., use `ClassTestRunner`:

```python
from test_utils.test_runner import ClassTestRunner

runner = ClassTestRunner(MedianFinder)
runner.add_test(
    "Example 1",
    ["MedianFinder", "addNum", "addNum", "findMedian"],
    [[], [1], [2], []],
    [None, None, None, 1.5]
)
```

### Problems with Complex Output Comparison

For problems where output order doesn't matter, use comparators:

```python
from test_utils.comparators import compare_2d_lists

runner = TestRunner(Solution, "methodName", comparator=lambda a, e: compare_2d_lists(a, e, order_matters=False))
```
