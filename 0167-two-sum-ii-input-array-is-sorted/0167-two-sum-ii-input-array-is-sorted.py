class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for i in range(len(numbers)): 
        #     for j in range(i+ 1, len(numbers)): 
        #         if numbers[i] + numbers[j] == target: 
        #             return [i+1, j+1]

        l, r = 0, len(numbers) - 1
        while l < r: 
            num = numbers[l] + numbers[r]
            if num == target: 
                return [l+1, r+1]
            elif num < target: 
                l += 1
            else: 
                r -= 1
