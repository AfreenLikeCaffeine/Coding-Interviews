# Container with Most Water - LeetCode 11

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        This function calculates the maximum area that can be formed from a list of lines of different heights.
        The lines are represented as a list of integers where each integer is the height of the line.
        The function takes the list of heights as input and returns the maximum area that can be formed.
        """
        maxVol = 0
        l,r = 0, len(height) - 1

        # loop until we have processed all the lines
        while l < r:
            # calculate the current volume
            currVol = min(height[l], height[r]) * (r-l)
            # update the maximum volume if the current volume is greater
            maxVol = max(currVol,maxVol)
            
            # Keep moving the shorter wall inward
            # if the left line is shorter, move the left pointer to the right
            if height[l] < height[r]:
                l+=1
            # else move the right pointer to the left
            else:
                r-=1
        return maxVol

        # Time complexity: O(n)
        # Space complexity: O(1)