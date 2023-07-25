#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # create a new linked list
        current = head
        
        # loop through each item in the sorted list
        while current:
            # if the next item is the same as the current item
            if current.next and current.val == current.next.val:
                # skip the next item
                current.next = current.next.next
            # else, move the pointer
            else:
                current = current.next
        
        return head
        
# @lc code=end

