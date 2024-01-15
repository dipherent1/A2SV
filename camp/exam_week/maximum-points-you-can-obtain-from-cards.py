class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints)
        if k == len(cardPoints):
            return total

        n = len(cardPoints)
        l = 0
        sums = sum(cardPoints[:n-k])
        ans = sums
        
        for r in range(n-k,len(cardPoints)):
            
            sums+=cardPoints[r]
            sums-=cardPoints[l]
            
            l+=1
            ans = min(sums,ans)
        
        return total-ans