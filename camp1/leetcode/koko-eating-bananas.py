class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def isvalid(val):
            count = 0

            for i in range(len(piles)):
                
                if piles[i]<= val:
                    count+=1
                
                else:
                    count+=ceil(piles[i]/val)

            return count<=h
        
        l = 1
        r= max(piles)

        while l<=r:
            mid = (l+r)//2
            if isvalid(mid):
                r = mid-1
            else:
                l = mid+1
        
        return l
