# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return True 
        def isSame(p, q):
            if not p and not q: return True
            if not p or not q or p.val != q.val:
                return False 
            left = isSame(p.left, q.right)
            right = isSame(p.right, q.left)
            if left and right: 
                return True 
            return False 
        return isSame(root.left, root.right)
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna