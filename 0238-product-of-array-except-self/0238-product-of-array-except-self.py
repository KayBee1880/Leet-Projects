class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Doc String: 
        An Algorithm that returns an array "answer" such that answer[i] == product of nums[:] except nums[i]
        Input: 
            - nums : List[int]
        Output: 
            - answer : List[int]
        Edge case: 
            - if zero(0) is an element 
            - No division is allowed
            - if len(nums) < 2 ??
            - If all elements are same non-neg number
            - more than one zero in nums[:]
        Constraints; 
            - Guaranteed that input fits in a 32 bit integer

        Thought Process:
            - n = len(nums) 
            - #if n <2: return [1] "This is void since question explains that the n >= 2"
            - answer = [1] * n
            - General formula: answer[i] = (product to the left of i) * (product of all elements to the right of i)

        """
        n = len(nums)
        answer = [1] * n
        # First pass: Prefix product
        left = 1 #this records the prefix product 
        for i in range(n): 
            answer[i] = left 
            left *= nums[i]
        # Second pass: suffix product 
        right = 1
        for i in reversed(range(n)): 
            answer[i]*=right
            right *= nums[i]
        return answer


