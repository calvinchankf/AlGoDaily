/*
    dynamic programming: recursion + hashtable

    Time    O(N * 9) there are 9 digits (not 10 because 5 has zero cells to go)
    Space   O(N * 9)
    2464 ms, faster than 23.51%
*/
var knightDialer = function(n) {
    const m = {
        0: [4, 6],
        1: [6, 8],
        2: [7, 9],
        3: [4, 8],
        4: [3, 9, 0],
        5: [],
        6: [1, 7, 0],
        7: [2, 6],
        8: [1, 3],
        9: [2, 4]
    }
    let total = 0
    const cache = {}
    for (let i = 0; i < 10; i++) {
        total += dfs(n-1, i, m, cache)
        total %= 10**9 + 7
    }
    return total
};

const dfs = (n, num, m, cache) => {
    if (n == 0) {
        return 1
    }
    
    const key = `${n},${num}`
    if (key in cache) {
        return cache[key]
    }
    
    let total = 0
    const cands = m[num]
    for (let i = 0; i < cands.length; i++) {
        const _num = cands[i]
        total += dfs(n-1, _num, m, cache)
        total %= 10**9 + 7
    }
    
    cache[key] = total
    return total
}