class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.l = [0]*n
        self.ptr = 0
    def insert(self, idKey: int, value: str) -> List[str]:
        self.l[idKey-1] = value
        ans = []
        if self.ptr<idKey-1:
            return []
        else:
            while self.ptr<self.n and self.l[self.ptr]:
                ans.append(self.l[self.ptr])
                self.ptr+=1
        return ans
            
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)