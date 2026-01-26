# Missing Number - LeetCode 268

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        This function takes a list of numbers and returns the missing number from the list.
        
        The missing number is calculated by subtracting the sum of the numbers in the list from the sum of the first 'n' natural numbers.
        
        :param nums: A list of numbers.
        :type nums: List[int]
        :return: The missing number from the list.
        :rtype: int
        """
        # Calculate the sum of the first 'n' natural numbers
        total = (len(nums) * (len(nums) + 1)) // 2
        # Calculate the sum of the numbers in the list
        nums_sum = sum(nums)
        # Return the missing number
        return total - nums_sum

# Time complexity: O(n)
# Space complexity: O(1)


if __name__ == "__main__":
    from q268_test import run_tests
    run_tests()