class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s

        row_list = {row:"" for row in range(numRows)}
        # print(row_list)
        up = True
        row = 0

        for l in s:
            row_list[row] += l
            if row < numRows-1 and up or row == 0:
                row+=1
                up = True
            else:
                up = False
                row-=1
        res = ""
        for rows in row_list:
            res+=row_list[rows]
        return res