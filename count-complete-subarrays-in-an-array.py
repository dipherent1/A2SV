class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        '''
        [1,3,1,2,2,3]
        '''
        visited = []
        k = 0
        for num in nums:
            if num not in visited:
                k+=1
            visited.append(num)
        hashmap = {}
        visited2 = []
        k2 = 0
        count = 0
        res = 0
        l = 0
        for i in range(len(nums)):
            hashmap[nums[i]] = 1+hashmap.get(nums[i],0)
            # if nums[i] not in visted2:
            #     k2+=1

            while len(hashmap)==k and l<=i:
                count+=1
                if hashmap[nums[l]]>1:
                    hashmap[nums[l]]-=1
                elif hashmap[nums[l]]==1:
                    del(hashmap[nums[l]])
                
                l+=1
            res+=count
        return res