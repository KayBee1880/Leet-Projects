class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return "" 
        min_window = ""
        min_length = float("inf")
        count_t = Counter(t)
        for i in range(len(s)): 
            for j in range(i + len(t), len(s) + 1): 
                substring = s[i:j]
                sub_count = Counter(substring)
                valid = True
                for key, val in count_t.items(): 
                    if sub_count[key] < val: 
                        valid = False 
                        break
                if valid and len(substring) < min_length: 
                    min_length = len(substring)
                    min_window = substring
        return min_window


