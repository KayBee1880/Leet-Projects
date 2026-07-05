class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        
        # unique_arr = set(arr)
        # if len(unique_arr) <= 1: 
        #     return -1
        # sorted_set_arr = sorted(unique_arr)
        # return sorted_set_arr[-2]
        if len(arr) <= 1: return -1 
        largest = -1
        second_largest = -1
        for num in arr: 
            if num > largest: 
                second_largest = largest
                largest = num 
            elif second_largest < num < largest:
                second_largest = num 
        return second_largest 