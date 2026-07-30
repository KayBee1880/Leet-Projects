# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        queue = deque([(root, 0)])
        total_sum = 0
        while queue: 
            node, curr_sum = queue.popleft()
            curr_sum = curr_sum * 10 + node.val 
            if not node.left and not node.right: 
                total_sum += curr_sum
            if node.left: 
                queue.append((node.left, curr_sum))
            if node.right: 
                queue.append((node.right, curr_sum))
        return total_sum

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna