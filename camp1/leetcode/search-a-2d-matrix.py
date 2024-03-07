class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ur,lc = 0,0
        br,rc = len(matrix)-1,len(matrix[0])-1

        while ur <= br:
            midr = (ur + br)//2
            # midc = (lc + rc)//2

            if matrix[midr][0] > target:
                br = midr-1
            elif matrix[midr][0] < target:
                ur = midr+1
            
            if matrix[midr][0] == target:
                return True
        
        print(matrix[br])
        
        while lc<=rc:
            midc = (lc+rc)//2
            
            if matrix[br][midc]>target:
                rc = midc-1
            
            elif matrix[br][midc]<target:
                lc = midc+1
            
            if matrix[br][midc] == target:
                return True

            
