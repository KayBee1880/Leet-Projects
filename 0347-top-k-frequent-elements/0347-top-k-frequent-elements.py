class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        m = []
        for key, val in freq.items(): 
            m.append([val, key])
        m.sort()
        lst = []
        for i in range(k):
            lst.append(m.pop())
        return [lst[i][1] for i in range(len(lst))]


