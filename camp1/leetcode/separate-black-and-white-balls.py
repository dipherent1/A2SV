class Solution:
    def minimumSteps(self, s: str) -> int:
        ans = 0
        count = 0
        for c in s:
            if c == "1":
                count+=1
            else:
                ans+=count
        
        return ans

        