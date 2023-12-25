class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        # for i in range(len())
        sum1 = 0
        sum2 = 0
        i,j = 0,0
        while i<len(mat):
            sum1+=mat[i][j]
            i+=1
            j+=1
        i = 0
        j-=1
        while j >= 0:
            num = mat[i][j]
            sum1+=num
            i+=1
            j-=1
        if len(mat)%2:
            i = (len(mat))//2
            sum1-=mat[i][i]
        return sum1
