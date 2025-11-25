# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        This function takes a list of integers and a target integer, and returns a list of lists of integers.
        Each sublist in the returned list represents a combination of integers from the input list that sum up to the target integer.
        
        :param candidates: A list of integers.
        :type candidates: List[int]
        :param target: An integer representing the target sum.
        :type target: int
        :return: A list of lists of integers, where each sublist is a combination of integers that sum up to the target integer.
        :rtype: List[List[int]]
        """
        sol_list = []

        def dfs(start, curr, total):
            """
            This helper function is used to perform a depth-first search on the input list.
            It takes three parameters: start, curr, and total.
            start is the starting index for the current iteration.
            curr is the current sublist of integers.
            total is the current total sum of the integers in curr.
            
            The function checks if the total is greater than the target sum. If so, it returns immediately.
            If the total is equal to the target sum, it adds the current sublist to the solution list.
            Otherwise, it recursively calls itself with the next index, the current sublist with the next integer added, and the total with the next integer added.
            """
            if total > target:
                return
            if total == target:
                sol_list.append(curr[:])
                return
            
            for i in range(start, len(candidates)):
                curr.append(candidates[i])
                dfs(i, curr, total + candidates[i])
                curr.pop()

        dfs(0, [], 0)
        return sol_list
        
        
# Time complexity: O(2^n)
# Space complexity: O(n)