class Solution:
    def romanToInt(self, s: str) -> int:
        #Create a hashmap with key, value == symbol, value 
        symMap = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        prev_value = 0 #Assign a variable called the previous value to 0
        total = 0
        for char in reversed(s): 
            curr_value = symMap[char]
            if curr_value < prev_value:
                total -= curr_value 
            else:
                total += curr_value 
            prev_value = curr_value 
        return total 