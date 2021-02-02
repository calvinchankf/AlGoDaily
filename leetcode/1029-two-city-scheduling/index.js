/*
    2nd: dynamic programming
    - recursion to get all the combinations
    - use a hashtable to avoid redundant calculation to optimize the speed from O(2^N) tp O(N^2)

    Time    O(N^2)
    Space   O(N^2)
    88 ms, faster than 27.27%
*/
var twoCitySchedCost = function(costs) {
    const n = costs.length
    const half =  Math.floor(n/2)
    return dfs(costs, 0, half, half, {})
};

const dfs = (costs, i, countA, countB, ht) => {
    if (countA == 0 && countB == 0) {
        return 0
    }
    if (countA < 0 || countB < 0 || i == costs.length) {
        return 2**32
    }
    const key = `${countA},${countB}`
    if (key in ht) {
        return ht[key]
    }
    const a = dfs(costs, i+1, countA-1, countB, ht) + costs[i][0]
    const b = dfs(costs, i+1, countA, countB-1, ht) + costs[i][1]
    ht[key] = Math.min(a, b)
    return ht[key]
}

let a

a = [[10, 20],[30, 200],[400, 50],[30, 20]];
console.log(twoCitySchedCost(a));

a = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
console.log(twoCitySchedCost(a));

a = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
console.log(twoCitySchedCost(a));

console.log('-----')

/*
    1st: sort
    - learned from others
    - first fill CityA, then the remaning people go to CityB

    e.g.1
    [[10,20],[30,200],[400,50],[30,20]]
    
    consider idx0, cityA is the way cheaper to go
    consider idx1, cityA is the way cheaper to go

    so we can sort the costs by diff btw going to cityA and cityB

    person1     person0   person3   person2
    ------------------------------------------
    [[30, 200], [10, 20], [30, 20], [400, 50]]
        -170        -10     10          350     <= diff


    e.g.2 
    [[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]

    person0      person3     person5     person2     person1    person4
    -----------------------------------------------------------------------
    [[259, 770], [184, 139], [577, 469], [926, 667], [448, 54], [840, 118]]
        -551        45          108         259         394         722     <= diff
    
    ref:
    - https://leetcode.com/problems/two-city-scheduling/solution/
    - https://www.youtube.com/watch?v=3A98vh5zsqw

    Time    O(NlogN)
    Space   O(1)
    36 ms, faster than 82.68%
*/
var twoCitySchedCost = function(costs) {
    costs.sort((a, b) => {
        const diffA = a[0] - a[1]
        const diffB = b[0] - b[1]
        return diffA - diffB
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