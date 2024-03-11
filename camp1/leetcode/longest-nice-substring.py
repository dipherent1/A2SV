class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def isvalid(check):
            # check = set(words)
            return all(ch.upper() in check and ch.lower() in check for ch in check)
        
        ans = ""
        for i in range(len(s)):
            for j in range(i+1,len(s)):
       
                if isvalid(set(s[i:j+1])):
       
                    if j-i+1 > len(ans):
                        ans = s[i:j+1]
       
        return ans