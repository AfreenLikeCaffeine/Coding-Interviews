# 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        This function calculates the maximum depth of a binary tree.
        
        The function takes a binary tree as input and returns the maximum depth of the tree.
        The maximum depth of a tree is the number of nodes along the longest path from the root node down to the farthest leaf node.
        
        :param root: The root of the binary tree.
        :type root: Optional[TreeNode]
        :return: The maximum depth of the binary tree.
        :rtype: int
        """
        
        if not root:
            return 0

        def findHeight(root) -> int:
            """
            This helper function is used to calculate the height of a subtree.
            
            The function takes a subtree as input and returns its height.
            The height of a subtree is the number of nodes along the longest path from its root node down to the farthest leaf node.
            
            :param root: The root of the subtree.
            :type root: Optional[TreeNode]
            :return: The height of the subtree.
            :rtype: int
            """
            if not root:
                return 0
            
            return 1 + max(findHeight(root.left), findHeight(root.right))
        
        return findHeight(root)
        
# Time Complexity: O(n)
# Space Complexity: O(h) where h is the height of the tree