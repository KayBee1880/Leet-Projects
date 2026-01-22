# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        l1_list = []
        l2_list = []
        curr = l1
        while curr: 
            l1_list.append(curr.val)
            curr = curr.next 
        l1_value = 0
        for d in l1_list: 
            l1_value = l1_value*10 + d
        
        curr = l2
        while curr: 
            l2_list.append(curr.val)
            curr = curr.next 
        l2_string = "".join([str(c) for c in l2_list])
        l2_value = int(l2_string)

        if l1_value == 0 and l2_value == 0: 
            return ListNode()

        total = l1_value + l2_value 
        result = []
        while total > 0: 
            result.append(total%10)
            total//=10
        result = result[::-1]
        dummy = ListNode()
        curr = dummy 
        for i in range(len(result)): 
            curr.next = ListNode(result[i])
            curr = curr.next 
        return dummy.next 
