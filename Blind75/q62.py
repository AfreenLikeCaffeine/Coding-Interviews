# Question Link: https://leetcode.com/problems/unique-paths/
# 62. Unique Paths

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        This function returns the number of unique paths from the top-left
        corner to the bottom-right corner of a m x n grid.
        
        :param m: The number of rows in the grid
        :type m: int
        :param n: The number of columns in the grid
        :type n: int
        :return: The number of unique paths
        :rtype: int
        """
        # Initialize a 2D array to store the number of paths from each cell
        paths_from_here = [[0] * n for _ in range(m)]
        # Initialize a 2D array to store whether each cell has been finished
        finished = [[False] * n for _ in range(m)]

        def count_paths(row, col):
            """
            This function returns the number of unique paths from the given cell
            to the bottom-right corner of the grid.
            
            :param row: The row of the cell
            :type row: int
            :param col: The column of the cell
            :type col: int
            :return: The number of unique paths
            :rtype: int
            """
            if row >= m or col >= n:
                # If the cell is out of bounds, return 0
                return 0
            if row == m - 1 and col == n - 1:
                # If the cell is the bottom-right corner, return 1
                return 1
            if finished[row][col]:
                # If the cell has been finished, return the stored result
                return paths_from_here[row][col]
            # Calculate the number of paths from the cell
            paths_from_here[row][col] = (
                count_paths(row + 1, col)
              + count_paths(row, col + 1)
            )
            # Mark the cell as finished
            finished[row][col] = True
            return paths_from_here[row][col]

        return count_paths(0,0)


if __name__ == "__main__":
    from q62_test import run_tests
    run_tests()

# Time Complexity: O(m*n) where m is the number of rows and n is the number of columns
# Space Complexity: O(m*n) where m is the number of rows and n is the number of columns