class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        def helper(n,k):
            if n == 2:
                if k == 1:
                    return 0
                else:
                    return 1
            
            if k%2 == 1:
                val = helper(n-1, (k+1)//2)
                if val == 0:
                    return 0
                else:
                    return 1
            else:
                val = helper(n-1, (k+1)//2)
                if val == 0:
                    return 1
                else:
                    return 0
        print(helper(n,k))
        return helper(n,k)
            
           