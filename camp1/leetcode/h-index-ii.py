class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = 0
        n = len(citations)
        r = len(citations)-1
        
        if n == 1:
            if citations[0] == 0:
                return 0
            else:
                return 1

        while l <= r:
            mid = (l+r)//2
            
            if citations[mid] <= n - mid or citations[mid] == 0:
                l = mid+1
            
            else:
                r = mid-1
        if r>=0:
            val = citations[r]
        else:
            val = 0
        return max(val,n-l)