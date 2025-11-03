class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums = Counter(nums)
        g = defaultdict(list)
        for key, val in count_nums.items(): 
            g[val].append(key)
        sorted_g = sorted(g, reverse = True)
        result = []
        for key in sorted_g: 
            for value in g[key]: 
                result.append(value)
                if len(result) > k: 
                    return result[:k]
        return result

