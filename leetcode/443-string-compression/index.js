/*
    1st approach: cache the result and put it back in the input

    Time    O(n)
    Space   O(n)
    92 ms, faster than 39.28%
*/
var compress = function(chars) {
    if (chars.length == 0) { return '' }
    const res = []
    let count = 1
    let cur = chars.shift()
    while (chars.length > 0) {
        const c = chars.shift()
        if (c == cur) {
            count += 1
        } else {
            res.push([cur, count])
            cur = c
            count = 1
        }
    }
    res.push([cur, count])
    
    while (res.length > 0) {
        const [cur, count] = res.shift()
        if (count == 1) {
            chars.push(cur)
        } else {
            chars.push(cur)
            chars.push(...`${count}`)
        }
    }
    return chars.length
};