class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:

        arr_length = (n*m)-len(walls)
        ans = 0
        mat = []
        for _ in range(m):
            mat.append([0]*n)
        for i,j in guards:
            mat[i][j] = "G"
        for i,j in walls:
            mat[i][j] = "W"
        
        for x,y in guards:
            tempx = x
            tempy = y

            #down row
            tempx+=1
            while tempx<m and (mat[tempx][tempy] != "G" and mat[tempx][tempy] != "W"):
                
                mat[tempx][tempy] = "X"
                tempx+=1
            tempx = x
            
            #up row
            tempx-=1
            while tempx>=0 and (mat[tempx][tempy] != "G" and mat[tempx][tempy] != "W"):
                
                mat[tempx][tempy] = "X"
                tempx-=1
            tempx = x
            
            #right row
            tempy+=1
            while tempy<n and (mat[tempx][tempy] != "G" and mat[tempx][tempy] != "W"):
                
                mat[tempx][tempy] = "X"
                tempy+=1
            tempy = y
            
            #right row
            tempy-=1
            while tempy>=0 and (mat[tempx][tempy] != "G" and mat[tempx][tempy] != "W"):
                
                mat[tempx][tempy] = "X"
                tempy-=1
            tempy = y
        print(mat)
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    ans+=1
        return ans
