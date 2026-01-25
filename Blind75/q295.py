# 295. Find Median from Data Stream
# https://leetcode.com/problems/find-median-from-data-stream/

import heapq


class MedianFinder:

    def __init__(self):
        """
        Initializes the MedianFinder object.
        
        The object will maintain two heaps: a min heap (self.large) and a max heap (self.small).
        The max heap will store the smaller half of the numbers, and the min heap will store the larger half.
        """
        self.small, self.large = [], []
        

    def addNum(self, num: int) -> None:
        """
        Adds a num to the median finder.

        The median finder maintains two heaps: a min heap (self.large) and a max heap (self.small).
        The max heap will store the smaller half of the numbers, and the min heap will store the larger half.
        The median is calculated by comparing the sizes of the two heaps.
        If the size of the max heap (self.small) is greater than the size of the min heap (self.large),
        the median is the largest element in the max heap.
        If the size of the max heap is less than the size of the min heap,
        the median is the smallest element in the min heap.
        If the sizes are equal, the median is the average of the largest element in the max heap and the smallest element in the min heap.

        :param num: The number to be added to the median finder.
        :type num: int
        """
        heapq.heappush(self.small, -1 * num)

        # If the max heap is empty or the largest element in the max heap is greater than the smallest element in the min heap,
        # move the largest element from the max heap to the min heap.
        if (self.small and self.large and (-1*self.small[0]) > self.large[0]):
            smaller_element = heapq.heappop(self.small) * -1
            heapq.heappush(self.large, smaller_element)
        
        # If the size of the max heap is greater than the size of the min heap by more than one element,
        # move the largest element from the max heap to the min heap.
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        # If the size of the min heap is greater than the size of the max heap by more than one element,
        # move the smallest element from the min heap to the max heap.
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)


    def findMedian(self) -> float:
        """
        Returns the median of the elements currently in the stream.

        The median is calculated by comparing the sizes of the two heaps.
        If the size of the max heap (self.small) is greater than the size of the min heap (self.large),
        the median is the largest element in the max heap.
        If the size of the max heap is less than the size of the min heap,
        the median is the smallest element in the min heap.
        If the sizes are equal, the median is the average of the largest element in the max heap and the smallest element in the min heap.
        """
        if len(self.small) > len(self.large):
            # If the size of the max heap is greater than the size of the min heap,
            # the median is the largest element in the max heap.
            return self.small[0] * -1
        elif len(self.small) < len(self.large):
            # If the size of the max heap is less than the size of the min heap,
            # the median is the smallest element in the min heap.
            return self.large[0]
        
        # If the sizes are equal, the median is the average of the largest element in the max heap and the smallest element in the min heap.
        return (self.small[0]*-1 + self.large[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# Time Complexity: O(log n) for addNum and O(1) for findMedian
# Space Complexity: O(n) where n is the number of elements added to the MedianFinder


if __name__ == "__main__":
    from q295_test import run_tests
    run_tests()