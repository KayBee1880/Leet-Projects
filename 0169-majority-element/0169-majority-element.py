class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        for key, val in freq.items(): 
            if val == max(list(freq.values())):
                return key 
        