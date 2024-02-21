class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        start = True
        openp = 0
        closep = 0
        
        
        for i in range(len(s)):
            if s[i] == "(":
                openp+=1
            else:
                if openp:
                    openp-=1
                else:
                    closep+=1
        return openp+closep
            
        