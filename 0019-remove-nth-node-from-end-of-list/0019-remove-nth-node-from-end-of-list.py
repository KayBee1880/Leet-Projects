# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        dummy.next = head 
        prev = dummy 
        length = 0
        curr = head 
        while curr: 
            length += 1
            curr = curr.next 
        for _ in range(length - n): 
            prev = prev.next
        prev.next = prev.next.next 
        return dummy.next 
