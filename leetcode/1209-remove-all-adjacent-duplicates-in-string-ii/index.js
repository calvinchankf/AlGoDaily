/*
    stack

    Time    O(N)
    Space   O(N)
    96 ms, faster than 49.73%
*/
var removeDuplicates = function(s, k) {
    const stack = []
    for (let c of s) {
        if (stack.length > 0 && stack[stack.length-1][0] == c) {
            stack[stack.length-1][1] += 1
        } else {
            stack.push([c, 1])
        }
        if (stack.length > 0 && stack[stack.length-1][1] == k) {
            stack.pop()
        }
    }
    let res = ''
    for (let [char, count] of stack) {
        res += char.repeat(count)
    }
    return res
};