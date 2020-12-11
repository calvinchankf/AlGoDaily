/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    const sign = x >= 0 ? 1 : -1
    x = Math.abs(x)
    const s = `${x}`
    let _s = ''
    for (let i = s.length-1; i >= 0; i--) {
        _s += s[i]
    }
    const res = sign * _s
    if (res < -(2**31) || res > 2**31-1) {
        return 0
    }
    return res
};