# Climbing stairs - LeetCode 70

class Solution:
    def _climb_stairs_recursion(self, num_stairs: int, solutions: dict) -> int:
        """
        This function calculates the number of ways to climb num_stairs stairs where at each step, you can either climb 1 or 2 steps using recursion with memoization.
        :param num_stairs: The number of stairs.
        :param solutions: A dictionary to store the subproblems.
        :return: The number of ways to climb num_stairs stairs.
        """
        if num_stairs in solutions:
            # If the subproblem has already been solved, return the stored result
            return solutions[num_stairs]
        
        if num_stairs == 0:
            # Base case: there is 1 way to climb 0 stairs
            return 1
        elif num_stairs < 0:
            # Base case: there are 0 ways to climb negative stairs
            return 0
        
        # Calculate the number of ways to climb the current number of stairs
        # by recursively calling the function with the current number of stairs - 1 and - 2
        solutions[num_stairs] = self._climb_stairs_recursion(num_stairs - 1, solutions) + self._climb_stairs_recursion(num_stairs - 2, solutions)
        return solutions[num_stairs]

    def climbStairs(self, n: int) -> int:
        """
        This function calculates the number of ways to climb n stairs where at each step, you can either climb 1 or 2 steps.
        :param n: The number of stairs.
        :return: The number of ways to climb n stairs.
        """
        # dictionary to store subproblems
        sols = {}
        # call the recursive helper function
        return self._climb_stairs_recursion(n, sols)

        # Time complexity: O(n)
        # Space complexity: O(n)