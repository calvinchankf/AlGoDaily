/*
    2nd approach: stack <= learned from others 
    - use a stack to store the indeces where the corresponding height can create a potential largest retangle

    ref:
    - https://www.youtube.com/watch?v=ZmnqCZp9bBs

    Time	O(n)
    Space	O(n)
*/
var largestRectangleArea = function(heights) {
    const n = heights.length
    let res = 0
    const stack = [[0, -1]]
    for (let i = 0; i < n; i++) {
        const x = heights[i]
        if (x > stack[stack.length-1][0]) {
            stack.push([x, i])
        } else {
            while (stack[stack.length-1][0] > x) {
                const [h, _] = stack.pop()
                const w = i - stack[stack.length-1][1] - 1
                const area = w * h
                res = Math.max(res, area)
            }
            stack.push([x, i])
        }
    }
    while (stack.length > 1) {
        const [h, _] = stack.pop()
        const w = n - stack[stack.length-1][1] - 1
        const area = w * h
        res = Math.max(res, area)
    }
    return res
};