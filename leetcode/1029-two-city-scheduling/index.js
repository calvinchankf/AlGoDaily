/*
    2nd: dynamic programming
    - recursion to get all the combinations
    - use a hashtable to avoid redundant calculation to optimize the speed from O(2^N) tp O(N^2)

    Time    O(N^2)
    Space   O(N^2)
    116 ms, faster than 7.24%
*/
var twoCitySchedCost = function(costs) {
    const n2 = costs.length
    const n = n2/2
    const ht = {}
    const dfs = (i, countA, countB) => {
        if (countA == 0 && countB == 0) {
            return 0
        }
        if (i == n2) {
            return 2**32
        }
        const key = `${countA},${countB}`
        if (key in ht) {
            return ht[key]
        }
        const left = dfs(i+1, countA-1, countB) + costs[i][0]
        const right = dfs(i+1, countA, countB-1) + costs[i][1]
        ht[key] = Math.min(left, right)
        return ht[key]
    }
    const res = dfs(0, n, n)
    return res
};

let a

a = [[10, 20],[30, 200],[400, 50],[30, 20]];
console.log(twoCitySchedCost(a));

a = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
console.log(twoCitySchedCost(a));

a = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
console.log(twoCitySchedCost(a));

console.log('-----')

var twoCitySchedCost = function(costs) {
    costs.sort((a, b) => {
        const diffA = a[0] - a[1]
        const diffB = b[0] - b[1]
        return diffA < diffB ? -1 : 1
    })
    let res = 0
    for (let i = 0; i < costs.length; i++) {
        if (i < costs.length/2) {
            res += costs[i][0]
        } else {
            res += costs[i][1]
        }
    }
    return res
};

a = [[10, 20],[30, 200],[400, 50],[30, 20]];
console.log(twoCitySchedCost(a));

a = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
console.log(twoCitySchedCost(a));

a = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
console.log(twoCitySchedCost(a));