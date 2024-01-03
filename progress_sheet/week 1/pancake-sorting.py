class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        for i in range(len(arr)):
            for j in range(0,len(arr)-i):
                if arr[j]==len(arr)-i:
                    break

            print(len(arr)-i,j)
            
            ans.append(j+1)
            arr[:j+1] = arr[:j+1][::-1]
            
            print(arr,"a")
            
            arr[:len(arr)-i] = arr[:len(arr)-i][::-1]
            ans.append(len(arr)-i)
            
            print(arr,"b")
        return ans
