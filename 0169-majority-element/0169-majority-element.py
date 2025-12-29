class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        return max(freq,key=freq.get)
        

###Note carefully that this implementation is from the Boyer Moore's Voting Algorithm
       