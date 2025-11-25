# 33. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Searches for a target element in a rotated sorted array.

        Args:
            nums (List[int]): A rotated sorted array.
            target (int): The element to be searched.

        Returns:
            int: The index of the target element if found, -1 otherwise.
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            # If the target is found, return its index
            if target == nums[middle]:
                return middle

            # If the left side is sorted
            if nums[left] <= nums[middle]:
                # If the target is in the left side, update the right boundary
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                # If the target is not in the left side, update the left boundary
                else:
                    left = middle + 1
            # If the right side is sorted
            else:
                # If the target is in the right side, update the left boundary
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                # If the target is not in the right side, update the right boundary
                else:
                    right = middle - 1

        # If the target is not found, return -1
        return -1

        
# Time complexity: O(log n)
# Space complexity: O(1)