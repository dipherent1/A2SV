class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        return " ".join(reversed(s))