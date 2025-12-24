class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        m = len(s)
        i = 1
        length = 0
        lps = [0]*m
        while i < m: 
            if s[i] == s[length]: 
                length += 1
                lps[i] = length
                i += 1
            else: 
                if length != 0: 
                    length = lps[length -1]
                else: 
                    lps[i] = 0
                    i += 1
        len_sub = m - lps[-1]
        return lps[-1] !=0 and m % len_sub == 0 
