# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, curr_sum): 
            if not node: return 0
            curr_sum = curr_sum * 10 + node.val
            if not node.left and not node.right: 
                return curr_sum 
            left = dfs(node.left, curr_sum)
            right = dfs(node.right, curr_sum)
            return left +right 
        return dfs(root, 0)
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna