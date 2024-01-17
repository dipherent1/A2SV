class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n = 0
        for _,_,size in trips:
            n = max(size,n)
        car = [0]*(n+1)
        for ppl,start,end in trips:
            if ppl>capacity:
                return False
            car[start] +=ppl
            car[end] -=ppl
        for i in range(1,n+1):
            car[i]+=car[i-1]
            if car[i]>capacity:
                return False
        return True