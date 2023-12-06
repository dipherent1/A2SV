class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        week = 1
        investment = 1
        for i in range(1,n+1):
            ans+=investment
            investment+=1
            if i%7==0:
                week+=1
                investment=week
        return ans
        