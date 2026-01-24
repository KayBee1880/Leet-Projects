# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB: 
            return None 
        def length(node): 
            curr = node 
            length = 0
            while curr: 
                length += 1
                curr = curr.next
            return length 
        lenA, lenB = length(headA), length(headB)
        currA, currB = headA, headB
        if lenA > lenB: 
            for _ in range(lenA-lenB): 
                currA = currA.next 
        if lenB > lenA:
            for _ in range(lenB-lenA): 
                currB = currB.next 
        while currA is not currB: 
            currA = currA.next 
            currB = currB.next
        return currA