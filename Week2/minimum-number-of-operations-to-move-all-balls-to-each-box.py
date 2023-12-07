class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        balls = [i for i in range(len(boxes)) if boxes[i] == "1"]
        ans = []
        steps = 0
        print(balls)
        for i in range(len(boxes)):
            steps = 0
            for ball in balls:
                steps+=(abs(i-ball))
            ans.append(steps)

        return ans
