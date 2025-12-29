"""
Comparator functions to check equality of data structures.

This module provides functions to compare LeetCode data structures:
- compare_values: Compare basic values with float tolerance
- compare_linked_lists: Compare two linked lists
- compare_trees: Compare two binary trees
- compare_graphs: Compare two graphs
- compare_2d_lists: Compare 2D lists with optional order flexibility
- Helper converters for debugging
"""

from typing import Optional, List
from collections import deque
from .data_structures import ListNode, TreeNode, Node


def compare_values(actual, expected) -> bool:
    """
    Compare two values, handling floats with tolerance.

    Args:
        actual: The actual result
        expected: The expected result

    Returns:
        True if values are equal (within tolerance for floats)
    """
    if isinstance(actual, float) and isinstance(expected, float):
        return abs(actual - expected) < 1e-5
    return actual == expected


def linked_list_to_list(head: Optional[ListNode], max_length: int = 100) -> List[int]:
    """
    Convert linked list to Python list for comparison.
    Handles cycles by limiting maximum length.

    Args:
        head: Head of linked list
        max_length: Maximum nodes to traverse (prevents infinite loops)

    Returns:
        List of node values
    """
    result = []
    current = head
    count = 0

    while current and count < max_length:
        result.append(current.val)
        current = current.next
        count += 1

    return result


def compare_linked_lists(actual: Optional[ListNode], expected: Optional[ListNode]) -> bool:
    """
    Compare two linked lists for equality.

    Args:
        actual: Actual linked list
        expected: Expected linked list

    Returns:
        True if lists contain same values in same order
    """
    while actual and expected:
        if actual.val != expected.val:
            return False
        actual = actual.next
        expected = expected.next

    return actual is None and expected is None


def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    """
    Convert binary tree to level-order list representation.

    Args:
        root: Root of binary tree

    Returns:
        Level-order list with None for missing nodes
    """
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()

    return result


def compare_trees(actual: Optional[TreeNode], expected: Optional[TreeNode]) -> bool:
    """
    Compare two binary trees for structural and value equality.

    Args:
        actual: Actual tree
        expected: Expected tree

    Returns:
        True if trees have same structure and values
    """
    if not actual and not expected:
        return True
    if not actual or not expected:
        return False
    if actual.val != expected.val:
        return False

    return (compare_trees(actual.left, expected.left) and
            compare_trees(actual.right, expected.right))


def graph_to_adj_list(node: Optional[Node]) -> List[List[int]]:
    """
    Convert graph to adjacency list representation.

    Args:
        node: Starting node of graph

    Returns:
        Adjacency list (sorted for consistent comparison)
    """
    if not node:
        return []

    # BFS to find all nodes
    visited = {}
    queue = deque([node])
    visited[node.val] = node

    while queue:
        curr = queue.popleft()
        for neighbor in curr.neighbors:
            if neighbor.val not in visited:
                visited[neighbor.val] = neighbor
                queue.append(neighbor)

    # Build adjacency list
    if not visited:
        return []

    max_val = max(visited.keys())
    adj_list = [[] for _ in range(max_val)]

    for val, n in visited.items():
        adj_list[val - 1] = sorted([neighbor.val for neighbor in n.neighbors])

    return adj_list


def compare_graphs(actual: Optional[Node], expected: Optional[Node]) -> bool:
    """
    Compare two graphs for equality.

    Args:
        actual: Actual graph
        expected: Expected graph

    Returns:
        True if graphs have same structure and connections
    """
    actual_adj = graph_to_adj_list(actual)
    expected_adj = graph_to_adj_list(expected)
    return actual_adj == expected_adj


def compare_2d_lists(actual: List[List], expected: List[List], order_matters: bool = True) -> bool:
    """
    Compare two 2D lists, optionally ignoring order.

    Args:
        actual: Actual 2D list
        expected: Expected 2D list
        order_matters: If False, treat as set of lists

    Returns:
        True if lists match (considering order_matters setting)
    """
    if order_matters:
        return actual == expected

    # Convert inner lists to tuples for set comparison
    actual_set = {tuple(sorted(inner)) if isinstance(inner, list) else inner
                  for inner in actual}
    expected_set = {tuple(sorted(inner)) if isinstance(inner, list) else inner
                    for inner in expected}
    return actual_set == expected_set
