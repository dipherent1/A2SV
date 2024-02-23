class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        for i in range(k):
            while q and q[-1]<nums[i]:
                q.pop()
            q.append(nums[i])
        
        l = 0
        ans = []
        
        for r in range(k,len(nums)):
            ans.append(q[0])
            
            if nums[l] == q[0]:
                q.popleft()
            
            l+=1            
            while q and q[-1]<nums[r]:
                q.pop()
            q.append(nums[r])
        
        if q: ans.append(q[0])
        return ans
