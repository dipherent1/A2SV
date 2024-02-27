class Solution:

    def countGoodNumbers(self, n: int) -> int:
        
        length = n
        k = n//2
        if n ==1:
            return 5
        def helper(k):
            if k <= 1:
                return 20
            if k%2 == 0: 
                return (helper(k//2)**2)%((10**9)+7)
            else:
                k-=1
                return ((helper(k//2)**2)*20)%((10**9)+7)
        val = helper(k)
        
        if length %2:
            val*=5
            return val%((10**9)+7)
        return val%((10**9)+7)