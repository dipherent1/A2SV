class Solution:
    def numberOfWays(self, s: str) -> int:
        ans = 0
        zeros = 0
        ones = 0

        if s[0] == "1":
            rz = 0
            ro = 1
        else:
            rz = 1
            ro = 0
        
        for i in range( 1,len(s)):
            if s[i] == "1":
                ones+=1
            else:
                zeros+=1
        
        for i in range(1,len(s)):
            
            if  s[i] == "0":
                zeros-=1
                if ro and ones:
                    ans+=(ro*ones)
                rz +=1
            else:
                ones-=1
                if rz and zeros:
                    ans+=(rz*zeros)
                ro+=1

        return ans
        
        
        
        
        

