"""
Data structure definitions for LeetCode problems.

This module defines common data structures used across LeetCode problems:
- ListNode: Singly-linked list node
- TreeNode: Binary tree node
- Node: Graph node with neighbors list
"""

from typing import Optional, List


class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        """String representation for debugging."""
        values = []
        current = self
        while current:
            values.append(str(current.val))
            current = current.next
            if len(values) > 100:  # Prevent infinite loop in case of cycles
                values.append("...")
                break
        return "ListNode[" + " -> ".join(values) + "]"


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        """String representation for debugging."""
        return f"TreeNode({self.val})"


class Node:
    """Definition for a graph node."""

    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self):
        """String representation for debugging."""
        neighbor_vals = [n.val for n in self.neighbors] if self.neighbors else []
        return f"Node({self.val}, neighbors={neighbor_vals})"
