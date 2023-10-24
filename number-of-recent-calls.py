class RecentCounter:

    def __init__(self):
        self.request = []
        # self.range = [-3000,0]

    def ping(self, t: int) -> int:
        self.request.append(t)
        self.range = [t - 3000, t]
        while self.request[0] > self.range[1] or self.request[0] < self.range[0]:
            self.request.pop(0)
        return len(self.request)

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)