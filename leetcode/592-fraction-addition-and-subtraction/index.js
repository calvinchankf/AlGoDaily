/*
    1st: math
    - add the fraction one by one using lcm
    - calculate the final result using gcd

    Time    O(NlogX) N = number of fractions, X = largest value of a denominator
    Space   O(N)
    68 ms, faster than 100.00%
*/
const { abs } = Math
var fractionAddition = function(expression) {
    const fractions = expression.replace(/[+]/g, ' +').replace(/[-]/g, ' -').split(' ')
    let res = [0, 1]
    for (let f of fractions) {
        if (f.length == 0) { continue }
        const [_a, _b] = f.split('/')
        const a = parseInt(_a)
        const b = parseInt(_b)
        const parent = lcm(res[1], b)
        const child = res[0] * parent / res[1] + a * parent / b
        res = [child, parent]
    }
    if (res[0] == 0) {
        return '0/1'
    }
    const sign = res[0] * res[1] > 0 ? 1 : -1
    const _gcd = gcd(res[0], res[1])
    const A = abs(res[0] / _gcd)
    const B = abs(res[1] / _gcd)
    return `${sign * A}/${B}`
};

const gcd = (a, b) => {
    if (b == 0) {
        return a
    }
    return gcd(b, a % b)
}

const lcm = (a, b) => {
    return a * b / gcd(a, b)
}