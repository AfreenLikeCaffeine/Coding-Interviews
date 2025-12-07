# 56. Merge Intervals
# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Merge overlapping intervals in a list of intervals.

        The function takes a list of intervals as input and returns a list of non-overlapping intervals.
        The intervals are sorted by their start time before merging.

        :param intervals: A list of intervals.
        :type intervals: List[List[int]]
        :return: A list of non-overlapping intervals.
        :rtype: List[List[int]]
        """
        intervals.sort(key = lambda i: i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = output[-1][1]

            # If the current interval overlaps with the previous one, merge them
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            # Otherwise, add the current interval to the output list
            else:
                output.append([start,end])
        
        return output
    
# Time Complexity: O(n log n) due to the sorting step, where n is the number of intervals.
# Space Complexity: O(n) for the output list, where n is the number of intervals.