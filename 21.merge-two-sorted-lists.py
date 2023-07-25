#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # combine the two lists
        list3 = []
        
        while list1:
            list3.append(list1.val)
            list1 = list1.next
        
        while list2:
            list3.append(list2.val)
            list2 = list2.next

        # sort the combined list
        list3.sort()
        
        # create a new linked list
        head = ListNode()
        current = head

        # loop through each item in the sorted list
        for item in list3:
            # create a new node
            current.next = ListNode(item)
            # move the pointer
            current = current.next
        
        return head.next
        
# @lc code=end

