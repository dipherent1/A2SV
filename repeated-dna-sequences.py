class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        l= 0
        seen={}
        ans = []
        while l<=len(s)-10:
            r = l+10
            if s[l:r] in seen:
                seen[s[l:r]]+=1
            else:
                seen[s[l:r]] =1
            l+=1
        print(seen)
        for key ,val in seen.items():
            if val>1:
                ans.append(key)
        return ans