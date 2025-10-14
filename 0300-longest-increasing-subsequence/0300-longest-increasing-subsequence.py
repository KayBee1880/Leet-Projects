class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = []
        for num in nums:
            pos = 0
            while pos < len(arr) and arr[pos] < num:
                pos += 1
            if pos == len(arr):
                arr.append(num)
            else:
                arr[pos] = num
        return len(arr)

