class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def isvalid(val):
            count = 1
            total = 0
            
            for i in range(len(weights)-1):
                total+=weights[i]
            
                if total+weights[i+1]>val:
                    count+=1
                    total = 0
            
            return count<=days

        l = max(weights)
        r = sum(weights)

        while l<=r:
            mid = (l+r)//2
            if isvalid(mid):
                print(mid)
                r = mid-1
            else:
                l = mid+1
        
        return l
