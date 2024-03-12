class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s)<2:
            return ""
        
        isvalid = True
        for i, c in enumerate(s):
            if c.swapcase() not in s:
                isvalid = False
                break
            
        if isvalid:
            return s
        else:
            s1 = self.longestNiceSubstring(s[:i])
            s2 = self.longestNiceSubstring(s[i+1:])
            return max(s1,s2,key = len)