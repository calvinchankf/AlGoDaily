/*
    1st: math + sort

    Time    O(k + klogk ) k = sqrt(N)
    Space   O(2 * sqrt(N))
    92 ms, faster than 10.71%
*/
var kthFactor = function(n, k) {
    const root = Math.sqrt(n)
    const factors = []
    for (let i = 1; i <= root; i++) {
        if (n%i == 0) {
            const remain = Math.floor(n/i)
            if (i == remain) {
                factors.push(i)
            } else {
                factors.push(i)
                factors.push(remain)
            }
        }
    }
    factors.sort((a, b) => a - b)
    if (k-1 < 0 || k-1 == factors.length) {
        return -1
    }
    return factors[k-1]
};