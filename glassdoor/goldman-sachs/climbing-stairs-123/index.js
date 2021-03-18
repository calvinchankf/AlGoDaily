/*
    https://www.1point3acres.com/bbs/interview/goldmansachs-software-engineer-430866.html

    You are climbing a staircase. It takes n steps to reach the top.
    Each time you can climb 1, 2 or 3 steps. 
    In how many distinct ways can you climb to the top?
*/
const climbStairs = (n) => {
    const cache = {}
    const dfs = x => {
        if (x == 0) {
            return 1
        } else if (x < 0) {
            return 0
        }
        if (x in cache) {
            return cache[x]
        }
        const ways = dfs(x-1) + dfs(x-2) + dfs(x-3)
        cache[x] = ways
        return ways
    }
    return dfs(n)
}

console.log(climbStairs(1))
console.log(climbStairs(2))
console.log(climbStairs(3))
console.log(climbStairs(4))
console.log(climbStairs(5))
console.log(climbStairs(6))