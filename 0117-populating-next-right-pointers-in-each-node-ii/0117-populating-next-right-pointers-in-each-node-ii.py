"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        leftmost = root 
        while leftmost: 
            dummy = Node()
            prev = dummy
            curr = leftmost 
            while curr: 
                if curr.left: 
                    prev.next = curr.left
                    prev = prev.next 
                if curr.right: 
                    prev.next = curr.right
                    prev = prev.next
                curr = curr.next
            leftmost = dummy.next 
        return root


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna