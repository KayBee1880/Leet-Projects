class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        bucket = [0] * (n+1)
        for c in citations: 
            if c >= n: 
                bucket[n] += 1
            else: 
                bucket[c] += 1
        total = 0
        for h in range(n, -1, -1): 
            total += bucket[h]
            if total >= h: 
                return h