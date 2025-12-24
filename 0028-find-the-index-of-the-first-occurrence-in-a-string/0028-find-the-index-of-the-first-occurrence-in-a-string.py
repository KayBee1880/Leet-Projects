class Solution:
    def lps_builder(self, pattern): 
        m = len(pattern)
        length = 0
        i = 1
        lps = [0] * m
        while i < m: 
            if pattern[i] == pattern[length]: 
                length += 1
                lps[i] = length 
                i += 1
            else: 
                if length != 0: 
                    length = lps[length - 1]
                else: 
                    lps[i] = 0
                    i += 1
        return lps


    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        if n > m: return -1
        lps = self.lps_builder(needle)
        i = j = 0
        while i < m:
            if haystack[i] == needle[j]: 
                i += 1
                j += 1
            if j == n: 
                return i-j
            elif i < m and haystack[i] != needle[j]: 
                if j != 0: 
                    j = lps[j-1]
                else: 
                    i += 1
        return -1

