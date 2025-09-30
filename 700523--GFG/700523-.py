'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def get_middle(self, node): 
        if not node or not node.next: return node
        slow = node
        fast = node.next 
        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next
        return slow
    def merge_two(self, l1, l2): 
        if not l1: return l2
        if not l2: return l1
        if l1.data < l2.data: 
            result = l1
            result.next = self.merge_two(l1.next, l2)
        else: 
            result = l2
            result.next = self.merge_two(l1, l2.next)
        return result
            
        
    def mergeSort(self, head):
        # code here
        if not head or not head.next: return head
        mid = self.get_middle(head)
        right = mid.next
        mid.next = None
        left = head
        
        left_head = self.mergeSort(left)
        right_head = self.mergeSort(right)
        return self.merge_two(left_head, right_head)
        
        
        
        
        