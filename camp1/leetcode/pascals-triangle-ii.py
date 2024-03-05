class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        row = self.getRow(rowIndex-1)
        arr = [1]
        for i in range(1,len(row)):
            arr.append(row[i]+row[i-1])
        arr.append(1)

        return arr

