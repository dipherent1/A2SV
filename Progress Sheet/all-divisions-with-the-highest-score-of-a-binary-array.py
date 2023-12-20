class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        ones_count = 0
        dic = defaultdict(list)
        zero_count = 0
        count0 = 0
        for i in nums:
            if i == 1:
                ones_count+=1
            else:
                count0+=1
        for i in range(len(nums)):
            dic[zero_count+ones_count].append(i)
            if nums[i] == 0:
                zero_count+=1
            else:
                ones_count-=1
        if  max(dic.keys()) > count0:
            print("1")
            return dic[max(dic.keys())]
        elif max(dic.keys()) < count0:
            print("2")
            return [len(nums)]
        else:
            ans = (dic[max(dic.keys())])
            print(ans + [len(nums)])
            return ans + [len(nums)]
