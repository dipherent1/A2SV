class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        n = len(flips)
        ans = 0
        running_sum = 0
        idx_sum = 0
        for i in range(1,n+1):
            running_sum+=flips[i-1]
            idx_sum+=i
            if running_sum == idx_sum:
                ans+=1
            
        return ans