# 543. Diameter of Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree/

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from typing import Optional
from test_utils.data_structures import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        This function calculates the diameter of a binary tree.

        The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
        This path may or may not pass through the root.

        The function takes the root of the tree as input and returns the diameter of the tree.

        :param root: The root of the binary tree.
        :type root: Optional[TreeNode]
        :return: The diameter of the binary tree.
        :rtype: int
        """
        self.res = 0

        def findHeight(root):
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

            left = findHeight(root.left)
            right = findHeight(root.right)
            
            self.res = max(self.res, left + right)
            return max(left, right) + 1

        findHeight(root)
        return self.res

# Time Complexity: O(n)
# Space Complexity: O(h), where h is the height of the tree


if __name__ == "__main__":
    from q543_test import run_tests
    run_tests()