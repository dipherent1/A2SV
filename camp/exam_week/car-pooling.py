class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n = 0
        for _,_,i in trips:
            n = max(n,i)
        passenger_no = [0]*(n+2)
        print(n)
        for passengers,start,end in trips:
            if passengers>capacity:
                return False
            passenger_no[start]+=passengers
            passenger_no[end]-=passengers
        for i in range(1,n+1):
            passenger_no[i]+=passenger_no[i-1]
            if passenger_no[i]>capacity:
                return False
        return True