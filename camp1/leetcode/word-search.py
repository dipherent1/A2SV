class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        ind = 0
        n = len(board)
        m = len(board[0])
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        visited = set()

        def helper(ind,i,j):
            if ind == len(word):
                return True
            
            for x,y in directions:
                
                iCur = i+x
                jCur = j+y


                if 0 <= jCur < m and 0 <= iCur < n and board[iCur][jCur] == word[ind] and (iCur,jCur) not in visited:
                    visited.add((iCur,jCur))
                    val = helper(ind+1,iCur,jCur)      
                    visited.remove((iCur,jCur))
                   
                    if val:
                        return True


        for i in range(n):
            for j in range(m):
                if board[i][j] == word[ind]:
                    visited.add((i,j))
                    val = helper(ind+1,i,j)      
                    visited.remove((i,j))
                   
                    if val:
                        return True

        return False

