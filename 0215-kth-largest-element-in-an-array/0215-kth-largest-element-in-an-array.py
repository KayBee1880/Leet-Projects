class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        for i in range(k): 
            a = nums.pop()
        return a

