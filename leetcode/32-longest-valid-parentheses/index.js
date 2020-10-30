/*
    2nd: stack
    - similar to lc20

    e.g. ")()(()))"

    01234567
    )()(()))()
     ^    ^
    the longest valid one


    1. just store the parentheses and corresponding indices into a stack [(parentheses, index), ...]
    2. then when we see a (, we can calculate the length of a valid parentheses by i - stack[-1][1]

    Time    O(N)
    Space   O(N)
    84 ms, faster than 79.21%
*/
var longestValidParentheses = function(s) {
    const stack = []
    let res = 0
    for (let i = 0; i < s.length; i++) {
        const c = s[i]
        if (c == '(') {
            stack.push([c, i])
        } else {
            if (stack.length > 0 && stack[stack.length-1][0] == '(') {
                stack.pop()
                let diff
                if (stack.length > 0) {
                    diff = i - stack[stack.length-1][1]
                } else {
                    diff = i + 1
                }
                res = Math.max(res, diff)
            } else {
                stack.push([c, i])
            }
        }
    }
    return res
};