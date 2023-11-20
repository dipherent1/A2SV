from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)-k
        if not n:
            return sum(cardPoints)
        m = 0
        l = 0
        total = sum(cardPoints)
        min_ans = float("inf")
        max_ans = float("-inf")
        running_sum = 0
        for r,val in enumerate(cardPoints):
            # total+=val
            
            running_sum+=val
            # m+=1
            if r-l+1>=n:
                max_ans = max(max_ans,total-running_sum)
                running_sum-=cardPoints[l]
                
                l+=1
                # m-=1
        return max_ans