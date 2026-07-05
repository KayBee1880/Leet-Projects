class Solution:
    def leaders(self, arr):
        # code here
        #leaders_list
        #max?
        n = len(arr)
        leaders_list = []
        if n == 0: 
            return []
        max_from_right = arr[n-1]
        leaders_list.append(max_from_right)
        
        for i in range(n-2, -1, -1):
            if arr[i] >= max_from_right: 
                leaders_list.append(arr[i])
                max_from_right = arr[i]
        leaders_list.reverse()
        return leaders_list
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna