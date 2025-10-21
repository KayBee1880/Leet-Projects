class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = ""
        for digit in digits: 
            n+=str(digit)
        n = int(n) + 1
        n = str(n)
        arr = [int(c) for c in n]
        return arr
        
