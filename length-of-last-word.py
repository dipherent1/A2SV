class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split(" ")
        print(words)
        return len(words[-1])