class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        mapping = {"2": "abc", 
        "3": "def", 
        "4": "ghi", 
        "5": "jkl", 
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []
        path = []
        def backtrack(index): 
            if index == len(digits): 
                result.append("".join(path))
                return 
            letters = mapping[digits[index]]
            for letter in letters: 
                path.append(letter)
                backtrack(index + 1)
                path.pop()
        backtrack(0)
        return result 



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna