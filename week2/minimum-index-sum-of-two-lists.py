class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans = defaultdict(list)
        for i in range(len(list1)):
            if list1[i] in list2:
                ind = list2.index(list1[i])
                # if ind+i not in ans:
                ans[ind+i].append(list1[i])
        return ans[min(ans.keys())]

        