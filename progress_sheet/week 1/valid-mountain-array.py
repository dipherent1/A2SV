class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        flag = 0
        # arr+=[-1]
        max_num = max(arr)
        if n<3:
            return False
        for i in range(n-1):
            if flag and arr[i]<=arr[i+1]:
                return False
            if arr[i]>=arr[i+1]:
                flag += 1
            # max_num = max(max_num,arr[i])
        print(max_num)
        if arr[0] == max_num or arr[n-1] == max_num:
            return False
        return True
