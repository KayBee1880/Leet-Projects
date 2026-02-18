# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        def get_height(node):
            height = 0
            while node.left:
                height += 1
                node = node.left
            return height 
        height = get_height(root)
        if height == 0: return 1
        left, right = 0, (2**height) - 1
        while left <= right:
            mid = (left+right)//2
            if self.exist(mid,height,root):
                left = mid + 1
            else:
                right = mid - 1
        return (2**height) - 1 + left
    
    def exist(self, idx, height, node):
        left, right = 0, (2**height) - 1
        for _ in range(height):
            mid = (left+right)//2
            if idx <= mid:
                node = node.left
                right = mid
            else:
                node = node.right
                left = mid +1
        return node is not None 
