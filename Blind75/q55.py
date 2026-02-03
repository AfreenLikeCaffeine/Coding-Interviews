# https://leetcode.com/problems/jump-game/
# 55. Jump Game

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Determine whether it is possible to jump from the first index to the last index.

        The function uses dynamic programming to solve the problem. It creates a boolean array result of size len(nums), where result[i] is True if it is possible to jump from index i to the last index. It then iterates over the array from right to left and for each index i, it checks if it is possible to jump from index i to the last index. If it is possible, result[i] is set to True. Finally, it returns result[0].

        :param nums: The list of numbers representing maximum jump lengths.
        :type nums: List[int]
        :return: True if it is possible to reach the last index, False otherwise.
        :rtype: bool
        """
        n = len(nums)
        result = [False] * n
        result[n - 1] = True

        def validate(i):
            """
            Returns True if it is possible to jump from index i to the last index, False otherwise.

            :param i: The current index.
            :type i: int
            :return: True if it is possible to jump from index i to the last index, False otherwise.
            :rtype: bool
            """
            max_jump = nums[i]
            while max_jump > 0:
                if i + max_jump >= n - 1:
                    return True
                if result[i + max_jump]:
                    return True
                max_jump -= 1
            return False

        for i in range(n - 2, -1, -1):
            result[i] = validate(i)

        return result[0]

# Time complexity: O(n^2)
# Space complexity: O(n)


if __name__ == "__main__":
    from q55_test import run_tests
    run_tests()
