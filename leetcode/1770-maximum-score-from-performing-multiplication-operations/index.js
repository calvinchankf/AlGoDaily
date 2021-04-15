/*
    1st: dyanmic programming

    Time    O(N^2)
    Space   O(N^2)
    8996 ms, faster than 100.00%
*/
var maximumScore = function(nums, multipliers) {
    
    const cache = {}
    
    const dfs = (i, j, k) => {
        if (k == multipliers.length) {
            return 0
        }
        if (i == j) {
            return nums[i] * multipliers[k]
        }
        const key = `${i},${j}`
        if (key in cache) {
            return cache[key]
        }
        const left = dfs(i+1, j, k+1) + nums[i] * multipliers[k]
        const right = dfs(i, j-1, k+1) + nums[j] * multipliers[k]
        cache[key] = Math.max(left, right)
        return cache[key]
    }
    
    return dfs(0, nums.length-1, 0)
};