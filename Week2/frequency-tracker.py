class FrequencyTracker:

    def __init__(self):
        self.elem = defaultdict(int)
        self.freq = defaultdict(int)
        

    def add(self, number: int) -> None:

        self.freq[self.elem[number]] -= 1 
        self.elem[number] = 1+self.elem.get(number,0)
        self.freq[self.elem[number]] = 1+self.freq.get(self.elem[number],0)

    def deleteOne(self, number: int) -> None:
        if number in self.elem:
            self.freq[self.elem[number]] = self.freq.get(self.elem[number],0)-1
            
            self.elem[number] = self.elem.get(number,0)-1

            self.freq[self.elem[number]] = self.freq.get(self.elem[number],0)+1
            if not self.elem[number]:
                del (self.elem[number])
        

    def hasFrequency(self, frequency: int) -> bool:
        # print(self.freq,"freq")
        # print(self.elem,"elem")
        return frequency in self.freq and self.freq[frequency]
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)