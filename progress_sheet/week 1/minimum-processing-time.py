class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse = True)
        processorTime.sort()
        print(tasks)
        print(processorTime)
        ans = 0
        j = 0
        for i in range(len(processorTime)):
            ans = max(ans,tasks[j]+processorTime[i])
            j = j+4
        return ans