class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        freq1 = [0] * 26
        freq2 = [0] * 26
        res = []
        for c in p: 
            freq1[ord(c)-ord("a")] += 1
        left = 0
        for right in range(len(s)): 
            freq2[ord(s[right])-ord("a")] += 1
            if right - left + 1 > len(p): 
                freq2[ord(s[left])- ord("a")] -= 1
                left += 1
            if freq1 == freq2: 
                res.append(left)
        return res 