class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        result = []
        i = 0
        n = len(words)
        while i < n:
            line_len = len(words[i])
            j = i + 1
            while j < n and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1
            num_words = j - i 
            is_last_line = (j == n)
            if num_words == 1 or is_last_line: 
                line = " ".join(words[i:j])
                line += " "*(maxWidth - len(line))
                result.append(line)
            else: 
                char_len = sum([len(w) for w in words[i:j]])
                spaces = maxWidth - char_len
                gaps = num_words - 1
                base = spaces // gaps 
                extra = spaces % gaps 
                parts = []
                for k in range(i, j-1): 
                    parts.append(words[k])
                    space = base + (1 if k - i < extra else 0)
                    parts.append(" "*space)
                parts.append(words[j - 1])
                result.append("".join(parts))
            i = j 
        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna