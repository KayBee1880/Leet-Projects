# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        heap =[]
        for i, node in enumerate(lists): 
            if node:
                heapq.heappush(heap, (node.val, i, node))
        dummy = ListNode()
        curr = dummy 
        while heap: 
            _, i, node = heapq.heappop(heap)
            curr.next = node 
            curr = curr.next 
            if node.next: 
                heapq.heappush(heap,(node.next.val, i , node.next))
        curr.next = None 
        return dummy.next 