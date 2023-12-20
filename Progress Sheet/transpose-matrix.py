class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        t = [[0 for j in range(n)] for i in range(m)]
        
        # print(t)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                t[j][i] = matrix[i][j]
                # matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        return t
        