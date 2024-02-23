class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        idxs = defaultdict(list)
        ans = [0]*len(temperatures)
        stack = []
        
        for i in range(len(temperatures)):
            
            while stack and stack[-1]<temperatures[i]:
                temp = stack.pop()
                ind = idxs[temp].pop()
                ans[ind] = i - ind
            
            stack.append(temperatures[i])
            idxs[temperatures[i]].append(i)
        
        return ans
