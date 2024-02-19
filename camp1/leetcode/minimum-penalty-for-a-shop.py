class Solution:
    def bestClosingTime(self, customers: str) -> int:
        no = [0]
        rs = 0
        for char in customers:
            if char == "N":
                rs+=1
            no.append(rs)
        
        yes = [0]
        rs = 0
        for i in range(len(customers)-1,-1,-1):
            if customers[i] == "Y":
                rs+=1
            yes.append(rs)
        
        penality = float("inf")
        ans = []
        m = float("inf")
        for i in range(len(no)):
            
            penality = no[i]+yes[len(customers)-i]
            m = min(m,penality)
            ans.append(penality)
        for i in range(len(ans)):
            if ans[i] == m:
                return i
