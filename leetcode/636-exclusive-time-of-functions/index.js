/*
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
*/
var exclusiveTime = function(n, logs) {
    let curTime = 0
    const stack = []
    const res = Array(n).fill(0)
    for (let log of logs) {
        let [task, se, t] = log.split(':')
        task = parseInt(task)
        t = parseInt(t)
        if (se == 'start') {
            const prevTask = stack[stack.length-1]
            res[prevTask] += t - curTime
            curTime = t
            stack.push(task)
        } else {
            const startTime = stack.pop()
            res[task] += t - curTime + 1
            curTime = t + 1
        }
    }
    return res
};