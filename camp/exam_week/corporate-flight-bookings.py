class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0]*(n+1)
        for start,end,seats in bookings:
            ans[start-1]+=seats
            ans[end]-=seats
        for i in range(1,n+1):
            ans[i]+=ans[i-1]
        return ans[:n]
        