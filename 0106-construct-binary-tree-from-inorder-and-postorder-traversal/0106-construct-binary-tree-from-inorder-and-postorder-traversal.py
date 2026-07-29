# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        post_idx = len(postorder) - 1
        inorder_map = {val:idx for idx, val in enumerate(inorder)}
        def helper(in_left, in_right): 
            nonlocal post_idx
            if in_left > in_right: 
                return None 
            root_val = postorder[post_idx]
            root = TreeNode(root_val)
            post_idx -= 1
            root_idx = inorder_map[root_val]
            root.right = helper(root_idx+1, in_right)
            root.left = helper(in_left, root_idx-1)

            return root 
        return helper(0, len(postorder)-1)
        


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna