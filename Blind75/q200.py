# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/

import collections
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        This function takes a 2D grid as input and returns the number of islands in the grid.
        An island is a group of connected "1"s in the grid.
        
        The function uses a breadth-first search (BFS) algorithm to traverse the grid and find the islands.
        
        Parameters:
        grid (List[List[str]]): A 2D grid of "0"s and "1"s.
        
        Returns:
        int: The number of islands in the grid.
        """
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r,c):
            """
            This helper function performs a breadth-first search (BFS) from the given cell.
            
            Parameters:
            r (int): The row of the cell.
            c (int): The column of the cell.
            
            Returns:
            None
            """
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()
                # Check all four directions
                dirs = [[0,1],[-1,0],[1,0],[0,-1]]
                for dr, dc in dirs:
                    r, c = row + dr, col + dc
                    # Check if the cell is within the grid and is a "1" and has not been visited
                    if (r in range(rows) 
                        and c in range(cols) 
                        and grid[r][c] == "1" 
                        and (r,c) not in visited):
                            visited.add((r,c))
                            q.append((r,c))

        for r in range(rows):
            for c in range(cols):
                # Check if the cell is a "1" and has not been visited
                if (r,c) not in visited and grid[r][c] == "1":
                    islands += 1
                    bfs(r, c)
        
        return islands
        
        # Time Complexity: O(m*n) where m is the number of rows and n is the number of columns
        # Space Complexity: O(m*n) where m is the number of rows and n is the number of columns