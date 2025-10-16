# Two Sum - LeetCode 1

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        This function takes a list of numbers and a target number and returns the indices of the two numbers in the list that add up to the target number.

        The function uses a hash map to store the numbers in the list as keys and their indices as values. It then iterates over the list and checks if the target number minus the current number is in the hash map. If it is, then the function returns the indices of the two numbers. If not, it adds the current number and its index to the hash map.

        :param nums: A list of numbers
        :type nums: List[int]
        :param target: The target number
        :type target: int
        :return: The indices of the two numbers in the list that add up to the target number
        :rtype: List[int]
        """
        hash_map = {}
        for i in range(len(nums)):
            # Check if the target number minus the current number is in the hash map
            if target - nums[i] in hash_map:
                # Return the indices of the two numbers if the target number minus the current number is in the hash map
                return [hash_map[target - nums[i]], i]
            else: 
                # Add the current number and its index to the hash map if the target number minus the current number is not in the hash map
                hash_map[nums[i]] = i

        # Time complexity: O(n)
        # Space complexity: O(n)


        