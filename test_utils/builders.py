"""
Builder functions to construct data structures from Python lists/dicts.

This module provides functions to build LeetCode data structures from
user-friendly Python native types:
- build_linked_list: Create linked list from list of values
- build_tree: Create binary tree from level-order traversal
- build_graph: Create graph from adjacency list
- create_cycle_linked_list: Create linked list with cycle
"""

from typing import Optional, List
from collections import deque
from .data_structures import ListNode, TreeNode, Node


def build_linked_list(values: Optional[List[int]]) -> Optional[ListNode]:
    """
    Build a singly-linked list from a list of values.

    Args:
        values: List of integers, e.g., [1, 2, 3, 4, 5]
                None or [] returns None

    Returns:
        Head of the linked list, or None if values is empty

    Example:
        >>> head = build_linked_list([1, 2, 3])
        >>> # Returns: 1 -> 2 -> 3
    """
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


def build_tree(values: Optional[List[Optional[int]]]) -> Optional[TreeNode]:
    """
    Build a binary tree from level-order traversal with None for missing nodes.

    Args:
        values: Level-order list with None for missing nodes
                e.g., [3, 9, 20, None, None, 15, 7]
                None or [] returns None

    Returns:
        Root of the binary tree, or None if values is empty

    Example:
        >>> root = build_tree([3, 9, 20, None, None, 15, 7])
        >>> #       3
        >>> #      / \
        >>> #     9  20
        >>> #       /  \
        >>> #      15   7
    """
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        # Process left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        # Process right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


def build_graph(adj_list: Optional[List[List[int]]]) -> Optional[Node]:
    """
    Build an undirected graph from adjacency list representation.

    Args:
        adj_list: Adjacency list where adj_list[i] contains neighbors of node i+1
                  e.g., [[2,4],[1,3],[2,4],[1,3]] for a 4-node graph
                  Node values are 1-indexed
                  None or [] returns None

    Returns:
        Reference to node 1 (first node), or None if adj_list is empty

    Example:
        >>> node = build_graph([[2,4],[1,3],[2,4],[1,3]])
        >>> # Creates graph: 1--2
        >>> #                |  |
        >>> #                4--3
    """
    if not adj_list:
        return None

    # Create all nodes first (1-indexed)
    nodes = {i + 1: Node(i + 1) for i in range(len(adj_list))}

    # Build neighbor relationships
    for i, neighbors in enumerate(adj_list):
        node_val = i + 1
        nodes[node_val].neighbors = [nodes[n] for n in neighbors]

    return nodes[1]  # Return first node


def create_cycle_linked_list(values: List[int], pos: int) -> Optional[ListNode]:
    """
    Create a linked list with a cycle at the given position.

    Args:
        values: List of node values
        pos: Index where the cycle starts (-1 for no cycle)

    Returns:
        Head of the linked list with cycle

    Example:
        >>> head = create_cycle_linked_list([3,2,0,-4], pos=1)
        >>> # Creates: 3 -> 2 -> 0 -> -4
        >>> #              ^           |
        >>> #              |___________|
    """
    if not values:
        return None

    head = build_linked_list(values)

    if pos == -1:
        return head

    # Find the node at position pos
    cycle_node = head
    for _ in range(pos):
        cycle_node = cycle_node.next

    # Find the last node and create cycle
    current = head
    while current.next:
        current = current.next
    current.next = cycle_node

    return head
