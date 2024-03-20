class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count= Counter(nums)
        
        print(count)

        maxx = max(count.values())
        minn = min(count.values())
        
        ans = []
        
        buckets = [[] for _ in range(maxx)]

        for key,val in count.items():
            buckets[val-1].append(key)
        
        for i in range(len(buckets)-1,-1,-1):
            if k <= 0:
                break

            if buckets[i]:
                ans.extend(buckets[i])
                k-=len(buckets[i])

        return ans
