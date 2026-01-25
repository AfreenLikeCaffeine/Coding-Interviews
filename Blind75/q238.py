# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        This function calculates the product of all elements in a list except for the element at the current index.
        It uses two pointers, one moving from left to right and the other moving from right to left.
        The product of all elements to the left of the current index is stored in the left variable.
        The product of all elements to the right of the current index is stored in the right variable.
        The product of the two variables is the product of all elements in the list except for the element at the current index.
        :param nums: A list of integers
        :return: A list of integers where each element is the product of all elements in the input list except for the element at the same index
        :rtype: List[int]
        """
        sol = [1] * len(nums)
        n = len(nums)

        left = 1
        for i in range(n):
            sol[i] *= left
            left *= nums[i]

        right = 1
        for i in range(n-1,-1,-1):
            sol[i] *= right
            right *= nums[i]
            
        return sol

# Time complexity: O(n)
# Space complexity: O(1) (excluding the output list)


if __name__ == "__main__":
    from q238_test import run_tests
    run_tests()