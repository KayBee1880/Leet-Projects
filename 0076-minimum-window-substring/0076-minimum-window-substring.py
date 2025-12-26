from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t): 
            return ""
        window_count = defaultdict(int)
        count_t = Counter(t)
        left = 0
        min_left = 0
        min_len = float("inf")
        required = len(count_t)
        formed = 0
        for right in range(len(s)): 
            char = s[right]
            window_count[char] += 1
            if char in count_t and count_t[char] == window_count[char]: 
                formed += 1
            while left <= right and formed == required: 
                if right - left + 1 < min_len and formed == required: 
                    min_len = right - left +1
                    min_left = left 
                left_char = s[left]
                window_count[left_char] -= 1
                if left_char in count_t and count_t[left_char] > window_count[left_char]: 
                    formed -= 1
                left += 1
        return "" if min_len == float("inf") else s[min_left: min_left + min_len]
            
            

