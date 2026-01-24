"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None 
        curr = head 
        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.next 
            curr.next = new_node
            curr = new_node.next 
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next 
            curr = curr.next.next 

        curr = head 
        copy_head = head.next 
        while curr:
            copy = curr.next
            curr.next = copy.next
            copy.next = copy.next.next if copy.next else None 
            curr = curr.next
        return copy_head 
        


    #Truthfully i prefer this particular approach using the hashmaps
        oldtocopy = {None: None}
        curr = head 
        while curr:
            copy = Node(curr.val)
            oldtocopy[curr] = copy
            curr = curr.next
        
        curr = head 
        while curr:
            copy = oldtocopy[curr]
            copy.next = oldtocopy[curr.next]
            copy.random = oldtocopy[curr.random]
            curr = curr.next
        return oldtocopy[head]