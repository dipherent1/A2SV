class Solution:
    def maxConsecutiveAnswers(self, s: str, k: int) -> int:
        '''
        "TTFF"
         ^ 
        "TTfTTfTT"
              r
            l
         values = [2,1]
         min(values)<=k --> true 
         values[l]-1
         l+=1
         
         ans = r - l + 1 
        k = 1
        '''

        hash_map = {"T": 0, "F": 0}
        l = 0
        res = 0
        for r in range(len(s)):
            hash_map[s[r]]+=1
            while min(hash_map.values())>k and l<r:
                hash_map[s[l]]-=1
                l+=1
            res = max(r-l+1,res)
        return res