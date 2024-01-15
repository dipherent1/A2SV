class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l = 0
        count = [0,0]
        
        if len(answerKey) == k:
            return len(answerKey)
        
        
        if answerKey[0] == "T":
            count[1]+=1
        else:
            count[0]+=1
        
        ans = 0
        for r in range(1,len(answerKey)):
            
            if answerKey[r] == "T":
                count[1]+=1
            else:
                count[0]+=1
            
            while l<r and min(count)>k:
                if answerKey[l] == "T":
                    count[1]-=1
                else:
                    count[0]-=1
                l+=1
            ans = max(ans,r-l+1)
        return ans