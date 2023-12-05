class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start
        ans = sum(distance[start:destination])
        ans2 = sum(distance) - ans
        return min(ans, ans2)
