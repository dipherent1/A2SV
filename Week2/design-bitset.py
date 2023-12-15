class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.ones = 0
        self.zeros = size
        self.bit = [0]*size
        self.flipped = False
        

    def fix(self, idx: int) -> None:
        if self.flipped:
            if self.bit[idx] == 0:
                pass
            else:
                self.bit[idx] = 0
                self.zeros -=1
                self.ones+=1
        
        #     self.zeros,self.ones = self.ones,self.zeros
            # if self.bit[idx]:
            #     self.bit[idx] = 0
            #     self.zeros +=1
            #     self.ones-=1
            # else:
            #     pass

        elif self.bit[idx]:
            pass
        else:
            self.bit[idx] = 1
            self.zeros -=1
            self.ones+=1
        

    def unfix(self, idx: int) -> None:
        if self.flipped:
            if self.bit[idx] == 1:
                pass
            else:
                self.bit[idx] = 1
                self.zeros +=1
                self.ones-=1
        #     self.zeros,self.ones = self.ones,self.zeros
            # if self.bit[idx]:
            #     pass
            # else:
            #     self.bit[idx] = 1
            #     self.zeros -=1
            #     self.ones+=1

        elif self.bit[idx]:
            self.bit[idx] = 0
            self.zeros +=1
            self.ones-=1
        else:
            pass

    def flip(self) -> None:
        self.zeros,self.ones = self.ones,self.zeros
        self.flipped = not(self.flipped)        

    def all(self) -> bool:
        return self.ones == self.size

    def one(self) -> bool:
        return self.ones>=1

    def count(self) -> int:
        return self.ones
        

    def toString(self) -> str:
        # print(type(self.bit))
        s = list(map(str,self.bit))
        si = []
        if self.flipped:
            for char in s:
                if char == "0":
                    si.append("1")
                else:
                    si.append("0")
            return "".join(si)

        return "".join(s)
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()