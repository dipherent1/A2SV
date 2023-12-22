class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check(i,j):
            ls = set()
            count= 0
            for r in range(3):
                for c in range(3):
                    if board[i+r][j+c] == ".":
                        continue
                    if board[i+r][j+c] in ls:
                        return False
                    ls.add(board[i+r][j+c])
            return True
        
        #check box
        for i in range(0,len(board)-1,3):
            for j in range(0,len(board[0])-1,3):
                if not check(i,j):
                    return False
        #check row
        for i in range(len(board)):
            ls =set()
            for j in range(len(board[0])):
                if board[i][j].isnumeric():
                    if board[i][j] in ls:
                        return False
                    else:
                        ls.add(board[i][j])
        #check col
        for  j in range(len(board[0])):
            ls = set()
            for i in range(len(board)):
                if board[i][j].isnumeric():
                    if board[i][j] in ls:
                        return False
                    else:
                        ls.add(board[i][j])

        return True
