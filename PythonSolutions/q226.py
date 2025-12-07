# 226. Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Invert a binary tree.

        This function takes a binary tree as input and returns the inverted binary tree.
        The function works by swapping the left and right child nodes of each node in the tree.

        :param root: The root of the binary tree.
        :type root: Optional[TreeNode]
        :return: The inverted binary tree.
        :rtype: Optional[TreeNode]
        """
        
        if not root:
            return None
        
        # Swap the left and right child nodes of the current node
        tmp = root.left
        root.left = root.right
        root.right = tmp

        # Recursively invert the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

# Time Complexity: O(n)
# Space Complexity: O(h)