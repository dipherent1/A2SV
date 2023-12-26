class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count =  Counter(arr1)
        ans = []
        ls = set()
        over = []
        for i in arr2:
            ans.extend([i]*count[i])
            ls.add(i)
        for i in arr1:
            if i not in ls:
                over.append(i)
        over.sort()
        (ans.extend(over))
        return ans