class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        num_words = len(words)
        word_len = len(words[0])
        word_count = Counter(words)
        s_len = len(s)
        res = []
        if not s or not words: return res 
        for i in range(word_len): 
            left, right = i, i
            current_count = Counter()
            count = 0
            while right + word_len <= s_len: 
                word = s[right: right + word_len]
                right += word_len
                if word in word_count: 
                    current_count[word] += 1
                    count += 1
                    while current_count[word] > word_count[word]: 
                        remove_word = s[left: left+word_len]
                        current_count[remove_word] -= 1
                        count -= 1
                        left += word_len
                    if count == num_words: 
                        res.append(left)
                else: 
                    current_count.clear()
                    count = 0
                    left = right 
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna