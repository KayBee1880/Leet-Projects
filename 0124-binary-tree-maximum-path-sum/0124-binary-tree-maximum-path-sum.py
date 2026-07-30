# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float("-inf")
        def pathSum(node): 
            if not node: return 0
            left = max(0,pathSum(node.left))
            right = max(0,pathSum(node.right))
            self.max_sum = max(self.max_sum, node.val + left + right)
            return node.val + max(left, right)
        pathSum(root)
        return self.max_sum


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna