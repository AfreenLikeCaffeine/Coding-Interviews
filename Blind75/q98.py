# 98. Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        This function checks if a given binary tree is a valid Binary Search Tree (BST).

        A valid BST is a tree where each node has a value greater than any node in its left subtree
        and less than any node in its right subtree.

        The function takes the root of the tree as input and returns True if the tree is a valid BST, False otherwise.

        :param root: The root of the binary tree.
        :type root: Optional[TreeNode]
        :return: True if the tree is a valid BST, False otherwise.
        :rtype: bool
        """
        def checkBST(root, low, high):
            """
            This helper function is used to check if a subtree is a valid BST.

            The function takes three parameters: root, low, and high.
            root is the root of the subtree.
            low and high are the lower and upper bounds for the subtree's values, respectively.

            The function checks if the subtree is a valid BST by checking if the values of all nodes in the subtree
            are within the given bounds.

            :param root: The root of the subtree.
            :type root: Optional[TreeNode]
            :param low: The lower bound for the subtree's values.
            :type low: float
            :param high: The upper bound for the subtree's values.
            :type high: float
            :return: True if the subtree is a valid BST, False otherwise.
            :rtype: bool
            """
            if not root:
                return True
            
            if not (low < root.val < high):
                return False
            
            return checkBST(root.left, low, root.val) and checkBST(root.right, root.val, high)

        return checkBST(root, float('-inf'), float('inf'))

# Time Complexity: O(n)
# Space Complexity: O(h) where h is the height of the tree