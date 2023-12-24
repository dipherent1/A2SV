import copy
class ATM:

    def __init__(self):
        self.notes = {0:[0,20],1:[0,50],2:[0,100],3:[0,200],4:[0,500]}

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(len(banknotesCount)):
            self.notes[i][0]+=banknotesCount[i]
        

    def withdraw(self, amount: int) -> List[int]:           
        # self.cur = self.notes.deepcopy()
        ans = [0]*5
        for i in range(4,-1,-1):
            ans[i] = min(self.notes[i][0],amount//self.notes[i][1])
            amount -= ans[i] * self.notes[i][1]
        if not amount:
            for i in range(4,-1,-1):
                self.notes[i][0] -= ans[i]
        return [-1] if amount else ans