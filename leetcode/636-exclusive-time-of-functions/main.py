"""
    1st: stack
    1. When we see a 'start'
        - pause the current function(if any), and update its execution time 
        - put the new start onto the stack
        - update the PREVIOUS TIME !!!
    2. When we see an 'end'
        - pop the current function from the stack, and update its execution time
        - increment the PREVIOUS TIME by one !!!
    
    To ask:
    - assume that the input must be a valid sequence of starts and ends?
    - input logs are sorted by timestamp?

    Time    O(N)
    Space   O(N/2) <- because there must be equal number of start and end
    76 ms, faster than 49.13%
"""
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        res = n * [0]
        prevTime = 0
        for i in range(len(logs)):
            log = logs[i].split(':')
            fn, se, t = int(log[0]), log[1], int(log[2])
            if se == 'start':
                if len(stack) > 0:
                    res[stack[-1]] += t - prevTime
                stack.append(fn)
                prevTime = t
            else:
                res[stack.pop()] += t - prevTime + 1
                prevTime = t + 1
        return res