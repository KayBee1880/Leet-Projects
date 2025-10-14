class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        numset = set(nums)
        if len(numset) == 1: return 1
        arr = []
        arr.append(nums[0])
        for i in range(1,len(nums)):
            if nums[i] <= arr[-1]: 
                arr[-1] = nums[i]
            else: 
                arr.append(nums[i])
        return len(arr) 
