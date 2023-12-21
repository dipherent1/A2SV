class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        def get_sum(i,j):
            sums = 0
            # print(grid[i][j:j+3],grid[i+1][j+1],grid[i+2][j:j+3])
            sums += sum(grid[i][j:j+3]) 
            sums += grid[i+1][j+1] 
            sums += sum(grid[i+2][j:j+3])
            return sums
        ans = 0
        m = len(grid)
        n = len(grid[0])
        i = 0
        j = 0
        while i <= m-3:
            print("1")
            j=0
            while j<=n-3:
                ans = max(ans,get_sum(i,j))
                j+=1
            i+=1 
        return ans

'''class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        def get_sum(i,j):
            sums = 0
            print(grid[i][j:j+3],grid[i+1][j+1],grid[i+2][j:j+3])
            sums += sum(grid[i][j:j+3]) 
            sums += grid[i+1][j+1] 
            sums += sum(grid[i+2][j:j+3])
            return sums
        ans = 0
        m = len(grid)
        n = len(grid[0])
        i = 0
        j = 0
        for i in range(n-2):
            for j in range(m-2):
                ans = max(ans,get_sum(i,j))
        return ans'''