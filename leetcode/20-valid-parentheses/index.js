/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
    const m = {
        ')':'(',
        ']':'[',
        '}':'{'
    }
    const stack = []
    for (const c of s) {
        if (c == '(' || c == '[' || c == '{') {
            stack.push(c)
        } else {
            if (stack.length > 0 && stack[stack.length-1] == m[c]) {
                stack.pop()
            } else {
                return false
            }
        }
    }
    return stack.length == 0
};