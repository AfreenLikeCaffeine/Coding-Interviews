# Clone Graph - LeetCode 133

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        Clone an undirected graph.

        Return a deep copy of the graph.

        :param node: The node to start the cloning from.
        :type node: Optional[Node]
        :return: A deep copy of the graph.
        :rtype: Optional[Node]
        """
        if node is None:
            return None

        # Create a dictionary to store the cloned nodes
        clones = {node: Node(node.val)}
        # Create a stack to store the nodes to be cloned
        stack = [node]

        # Iterate over the nodes in the graph
        while stack:
            curr = stack.pop()
            # Iterate over the neighbors of the current node
            for neigh in curr.neighbors:
                # If the neighbor hasn't been cloned yet, clone it
                if neigh not in clones:
                    clones[neigh] = Node(neigh.val)
                    stack.append(neigh)
                # Add the cloned neighbor to the cloned current node
                clones[curr].neighbors.append(clones[neigh])
        return clones[node]
        # Time complexity: O(V + E), where V is the number of vertices and E is the number of edges in the graph.
        # Space complexity: O(V), for storing the cloned nodes in the dictionary.
        




        