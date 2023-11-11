class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        '''
        approch:
        since its a single thread cpu what ends is what is currently running, i.e u close the bracket of what is currently open 

        the problem with this is to not forget to include the  time stamps

        whenever we start we need to add the time spent to the previous time.
        we access the previous id using stack. 
        
        when we end we pop the last elemen of the stack effectively stoping it and add its ending time - stating time +1

        the problem with just using prev_id arises when there are multiple ends at the end. we keep on poping stack to find which id to stop
        '''
        res = [0]*n
        prev_time = 0
        stack = []
        for log in logs:
            funcid,status,timestamp = log.split(":")
            funcid = int(funcid)
            timestamp =int(timestamp)
            if status == "start":
                if stack:
                    res[stack[-1]] += timestamp - prev_time
                stack.append(funcid)
                prev_time = timestamp
            else:
                res[stack.pop()]+=timestamp - prev_time + 1
                prev_time = timestamp+1
            prev_id = funcid
        return res