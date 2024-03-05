class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def helper(num,path):
            if len(path) == k:
                ans.append(path[:])
                return 
            
            if num >n:
                return

            
            helper(num+1,path)
            path.append(num)
            
            helper(num+1,path)
            path.pop()

        helper(1,[])

        return ans