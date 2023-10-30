class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[2])
        max_trip = trips[-1][-1]
        passengersincar = [0]*(trips[-1][-1]+1)
        total_passengers =0
        for people,start,end in trips:
            passengersincar[start]+=people
            passengersincar[end]-=people
        for passengers in passengersincar:
            total_passengers += passengers
            if total_passengers > capacity:
                return False
        return True