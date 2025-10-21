class Solution:
    def isPalindrome(self, x: int) -> bool:
        #time and space complexity is O(logx)
        y = str(x)
        return y == y[::-1]