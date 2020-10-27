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
        if (toExclude.has(i) == false) {
            res += s[i]
        }
    }
    return res
};