class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid)

        row = [0]*n
        col = [0]*m

        for i in range(n):
            for j in range(m):
                col[i] = max(col[i],grid[i][j])
                row[j] = max(row[j],grid[i][j])

        ans = 0

        for i in range(n):
        
            for j in range(m):
                if grid[i][j] == row[j] or grid[i][j] == col[i]:
                    continue
                ans+= min(row[j],col[i]) - grid[i][j] 
        
        return ans