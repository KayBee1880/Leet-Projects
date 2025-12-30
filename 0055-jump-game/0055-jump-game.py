class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Check if the last index can be reached
        Input: 
            - list[int]
        Output: 
            - bool val [True / False]
        Edge Case: 
            - If list[int] is empty 
            - If jumps get stuck in the middle of the array
            - If we get to a point in the traversal where the jump can't take us to the last index
            -
        """
        farthest = 0
        for i in range(len(nums)): 
            if i > farthest: return False
            farthest = max(farthest, i + nums[i])
            if farthest >= len(nums) - 1: 
                return True 
        return False 