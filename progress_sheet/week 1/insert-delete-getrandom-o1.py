from random import randint
class RandomizedSet:

    def __init__(self):
        self.rand = []
        self.dic = {}
        self.ind = 0
        

    def insert(self, val: int) -> bool:

        if val not in self.dic:
            self.dic[val] = (self.ind) #added together
            self.rand.append(val)
            self.ind+=1
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:
        # print(self.rand,self.dic,"f")
        if val not in self.dic:
            return False
        else:
            i = self.dic[val]

            self.rand[i],self.rand[-1] = self.rand[-1],self.rand[i]
            self.dic[self.rand[i]] = i
            self.ind-=1
            
            self.rand.pop() #delete desired number once it in at [-1]
            
            del self.dic[val]
            # print(self.rand,self.dic)
            return True
        

    def getRandom(self) -> int:
        # print(self.rand,self.dic)

        i = randint(0,len(self.rand)-1)
        # print(i)
        return self.rand[i]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()