# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge two sorted singly-linked lists.

        This function takes two sorted singly-linked lists as input and returns a new sorted singly-linked list.

        :param list1: The first sorted singly-linked list.
        :type list1: Optional[ListNode]
        :param list2: The second sorted singly-linked list.
        :type list2: Optional[ListNode]
        :return: A new sorted singly-linked list.
        :rtype: Optional[ListNode]
        """

        # If the first list is empty, return the second list
        if list1 == None:
            return list2
        # If the second list is empty, return the first list
        if list2 == None:
            return list1
        
        # Determine which list has the smaller value
        if list1.val <= list2.val:
            new_node = list1
            # Recursively call the function to merge the remaining lists
            new_node.next = self.mergeTwoLists(list1.next, list2)
        else:
            new_node = list2
            # Recursively call the function to merge the remaining lists
            new_node.next = self.mergeTwoLists(list1, list2.next)
        
        # Return the merged list
        return new_node

# Time complexity: O(n)
# Space complexity: O(n)        