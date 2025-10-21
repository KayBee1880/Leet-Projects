class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n <= 1: 
            result = 1
        result = 1
        for i in range(2,n+1):
            result *= i
        count = 0
        while result%10 == 0:
            count += 1
            result//=10
        return count
        
    