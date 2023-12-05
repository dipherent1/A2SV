class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start>destination:
            start, destination = destination, start
        distance1 = sum(distance[start:destination])
        distance2 = sum(distance)-distance1
        # print(ans)
        return min(distance1,distance2)