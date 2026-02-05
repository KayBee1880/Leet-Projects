class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        list_s = s.split()
        list_s.reverse()
        return " ".join(list_s)
        