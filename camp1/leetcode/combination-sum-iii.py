class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def helper(i,path):
            if sum(path) == n and len(path) == k:
                ans.append(path[:])
                return 
            
            if sum(path) > n:
                return
            
            for j in range(i,10):
                
                path.append(j)

                helper(j+1,path)

                path.pop()
        
        helper(1,[])
        return ans