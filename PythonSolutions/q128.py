# Longest Consecutive Sequence - LeetCode 128

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        This function takes a list of numbers and returns the longest consecutive sequence found in the list.

        The function first creates a set of the list of numbers. It then iterates over the set and for each number, it checks if the number before it is in the set. If it is not, then it starts counting the length of the consecutive sequence. It then continues counting the length of the sequence until it finds a number that is not in the set. The length of the sequence is then compared to the maximum length found so far and if it is greater, it is updated.

        :param nums: A list of numbers
        :type nums: List[int]
        :return: The longest consecutive sequence found in the list
        :rtype: int
        """
        my_set = set(nums)
        max_length = 0
        for num in my_set:
            # Check if the number before the current number is in the set
            if (num - 1) not in my_set:
                current_length = 1
                while((num + 1) in my_set):
                    # Increment the length of the sequence if the number after the current number is in the set
                    current_length = current_length + 1
                    num = num + 1
                # Update the maximum length if the current length is greater
                if current_length > max_length:
                    max_length = current_length
        return max_length

        # Time complexity: O(n)
        # Space complexity: O(n)        