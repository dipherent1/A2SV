class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        dic = defaultdict(list)
        ans = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                dic[i+j].append(mat[i][j])
        for keys,val in dic.items():
            if keys%2 == 0:
                ans.extend(val[::-1])
            else:
                ans.extend(val)
        return(ans)        