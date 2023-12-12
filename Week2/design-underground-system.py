class UndergroundSystem:

    def __init__(self):
        self.trip = defaultdict(list)
        self.log = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.log[id] = (stationName,t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation,start_time = self.log[id]
        self.trip[(startStation,stationName)].append(abs(start_time-t))
        del(self.log[id])

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.trip[(startStation,endStation)])/len(self.trip[(startStation,endStation)])
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)