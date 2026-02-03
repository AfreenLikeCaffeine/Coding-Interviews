# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This repository contains Python solutions to coding interview problems, primarily organized around the Blind75 list. Solutions follow the LeetCode problem naming convention (e.g., `q1.py` for Two Sum).

## Running Tests

Run a single problem's tests:
```bash
python Blind75/q1.py           # Runs tests via __main__ block
python Blind75/q1_test.py      # Runs test file directly
```

## Test Infrastructure

The `test_utils/` package provides reusable components for testing LeetCode solutions:

- **Data Structures** (`data_structures.py`): `ListNode`, `TreeNode`, `Node` (graph) classes matching LeetCode definitions
- **Builders** (`builders.py`): Convert Python lists to data structures
  - `build_linked_list([1,2,3])` → linked list
  - `build_tree([3,9,20,None,None,15,7])` → binary tree (level-order)
  - `build_graph([[2,4],[1,3],[2,4],[1,3]])` → graph from adjacency list
  - `create_cycle_linked_list([3,2,0,-4], pos=1)` → linked list with cycle
- **Comparators** (`comparators.py`): Compare data structures for test assertions
  - `compare_linked_lists()`, `compare_trees()`, `compare_graphs()`
  - `compare_2d_lists(actual, expected, order_matters=False)` for set-like comparisons
- **Test Runners** (`test_runner.py`):
  - `TestRunner(Solution, "methodName")` for standard problems
  - `ClassTestRunner(SolutionClass)` for design problems (e.g., MedianFinder)

## Solution File Pattern

Each solution file follows this structure:
```python
from test_utils.data_structures import ListNode  # if needed

class Solution:
    def methodName(self, ...):
        # implementation
        pass

if __name__ == "__main__":
    from q{N}_test import run_tests
    run_tests()
```

Test files use `get_test_cases()` returning `(name, inputs_dict, expected)` tuples and a `run_tests()` function that wires up the TestRunner with appropriate builders/comparators.

## Custom Skills

### /add-solution

Use `/add-solution <path>` to set up a new LeetCode solution. This skill:

1. Reads the solution file and extracts problem metadata
2. Refactors code to match project conventions:
   - Adds `from typing import List` imports
   - Fixes type annotations (`list[int]` → `List[int]`)
   - Adds `if __name__ == "__main__"` block
3. Creates the test file with proper structure
4. Prompts for test cases (LeetCode examples + edge cases)
5. Runs tests to verify

Example: `/add-solution Blind75/q55.py`
