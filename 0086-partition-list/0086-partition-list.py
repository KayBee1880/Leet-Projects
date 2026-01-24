# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next: return head
        after_head = ListNode()
        before_head = ListNode()
        after = after_head
        before = before_head
        curr = head
        while curr:
            if curr.val < x:
                before.next = curr
                before = before.next
            else:
                after.next = curr
                after = after.next 
            curr = curr.next 
        after.next = None
        before.next = after_head.next 
        return before_head.next

        