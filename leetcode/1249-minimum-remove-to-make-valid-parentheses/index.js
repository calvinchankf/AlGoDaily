/*
    1st: stack + hashtable
    - similar to lc921 but save the indices of the redundant opens & closes
    - construct the result by removing the characters at redundant indices
    
    Time    O(2N)
    Space   O(N)
    104 ms, faster than 62.64%
*/
var minRemoveToMakeValid = function(s) {
    const opens = []
    const closes = []
    for (let i = 0; i < s.length; i++) {
        const c = s[i]
        if (c == '(') {
            opens.push(i)
        } else if (c == ')') {
            if (opens.length > 0) {
                opens.pop()
            } else {
                closes.push(i)
            }
        }
    }
    let res = ''
    const toExclude = new Set(opens.concat(closes))
    for (let i = 0; i < s.length; i++) {
        if (toExclude.has(i) === false) {
            res += s[i]
        }
    }
    return res
};

/*
    2nd: same as 1st but only use 1 stack

    Time    O(2N)
    Space   O(N)
    108 ms, faster than 48.36%
*/
var minRemoveToMakeValid = function(s) {
    const n = s.length
    const stack = []
    for (let i = 0; i < n; i++) {
        const c = s[i]
        if (c == '(') {
            stack.push([c, i])
        } else if (c == ')') {
            if (stack.length > 0 && stack[stack.length-1][0] == '(') {
                stack.pop()
            } else {
                stack.push([c, i])
            }
        }
    }
    const hs = new Set()
    stack.forEach((x) => hs.add(x[1]))
    let res = ''
    for (let i = 0; i < n; i++) {
        const c = s[i]
        if (hs.has(i) === false) {
            res += c
        }
    }
    return res
};