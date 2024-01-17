class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.sum = []
        for i in range(len(matrix)+1):
            self.sum.append([0]*(len(matrix[0])+1))
        
        for i in range(1,len(self.sum)):
            for j in range(1,len(self.sum[0])):
                self.sum[i][j] = self.sum[i-1][j] + self.sum[i][j-1] - self.sum[i-1][j-1] + matrix[i-1][j-1] 
        

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        return self.sum[r2+1][c2+1]-self.sum[r1][c2+1]-self.sum[r2+1][c1]+self.sum[r1][c1]

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)