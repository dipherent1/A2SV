class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = deque(tickets)
        count = 0
        if k != len(tickets)-1:
            while k+1:
                if q[0]:
                    q[0]-=1
                    count+=1
                q.append(q.popleft())
                k-=1
        for i in range(len(tickets)):
            print(q[-1])
            l = q[i]
            if q[i]<q[-1]:
                count+=q[i]
            else:
                count+=q[-1]
        return count
