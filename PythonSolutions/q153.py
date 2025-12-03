#153. Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        This function takes a rotated sorted array and returns the minimum element in the array.

        The function uses binary search to find the minimum element. It checks if the array is rotated or not. If the array is not rotated, it returns the first element. If the array is rotated, it divides the array into two halves, and checks which half contains the minimum element.

        :param nums: A rotated sorted array.
        :type nums: List[int]
        :return: The minimum element in the array.
        :rtype: int
        """
        l = 0
        r = len(nums) - 1

        # if array not rotated
        if nums[l] <= nums[r]:
            return nums[l]

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                # min is in right half
                l = mid + 1
            else:
                # min is in left half including mid
                r = mid

        return nums[l]

# Time complexity: O(log n)
# Space complexity: O(1)