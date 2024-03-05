class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        
        l = len(candidates)
        
        def helper(i,path):
            
            if sum(path) == target:
                ans.append(path[:])
            
            if sum(path)>target:
                return 
            
            for j in range(i,l):
                
                path.append(candidates[j])
                helper(j,path)
                path.pop()

        helper(0,[])
        return ans
