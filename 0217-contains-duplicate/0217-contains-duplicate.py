class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums: return False 
        # for i in range(len(nums)): 
        #     for j in range(i+1, len(nums)): 
        #         if nums[i] == nums[j]: 
        #             return True 
        # return False 
        count = Counter(nums)
        for val in count.values(): 
            if val >=2 : 
                return True 
        return False 