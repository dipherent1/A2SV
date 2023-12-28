class Robot:

    def __init__(self, width: int, height: int):
        self.row = height
        self.col = width
        self.pos = [0,0]
        self.face = 0 #0 east 1 north 2 west  3 south
        self.edges = [[0,0],[0,self.col-1],[self.row-1,self.col-1],[self.row-1,0]]

    def step(self, num: int) -> None:
        num %= (2*(self.row-1)+2*(self.col-1))
        if not num and self.pos==[0,0]:
            self.face = 3
        if not num and self.pos==[0,self.col-1]:
            self.face = 0
        if not num and self.pos==[self.row-1,self.col-1]:
            self.face = 1
        if not num and self.pos==[self.row-1,0]:
            self.face = 2
        while num:
            # print(num)
            if self.face%4 == 0:             
                self.pos[1]+=num

                if self.pos[1] >= self.col-1:
                    num=self.pos[1]-(self.col-1)
                    self.pos[1] = self.col-1
                    if num:
                        self.face+=1
                else:
                    num = 0

            elif self.face%4 == 1:           
                self.pos[0]+=num

                if self.pos[0] >= self.row-1:
                    num=self.pos[0]-(self.row-1)           
                    self.pos[0] = self.row-1
                    if num:
                        self.face+=1
                else:
                    num = 0

            elif self.face%4 == 2:
                self.pos[1]-=num

                if self.pos[1] <= 0:
                    num=abs(self.pos[1])
                    self.pos[1] = 0
                    if num:
                        self.face+=1
                else:
                    num = 0

            elif self.face%4 == 3:
                self.pos[0]-=num
                # print(self.pos,"first")
                if self.pos[0] <= 0:
                    num=abs(self.pos[0])
                    self.pos[0] = 0
                    if num:
                        self.face+=1
                else:
                    num = 0
                # print(self.pos)
    def getPos(self) -> List[int]:
        return self.pos[::-1]
        

    def getDir(self) -> str:
        if self.face%4 == 0: return "East"
        if self.face%4 == 1: return "North"
        if self.face%4 == 2: return "West"
        if self.face%4 == 3: return "South"

        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()