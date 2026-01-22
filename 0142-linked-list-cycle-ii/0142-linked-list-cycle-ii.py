# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return None 
        slow = fast = head 
        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next 
            if slow is fast: 
                ptr1, ptr2 = slow, head 
                while ptr1 is not ptr2: 
                    ptr1 = ptr1.next 
                    ptr2 = ptr2.next 
                return ptr1
        return None 
            
