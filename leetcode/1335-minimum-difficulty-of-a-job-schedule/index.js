/*
    1st: dynamic programming(recursion + hashtable)
    - similar to lc410, 1043, 1335
    - instead of calculating the max(subarray) from the top, we can do it from the bottom of the recursion
    - sub problem = min(
                        max(nums[:i]), 
                        max(nums[i:])
                    )
    sub problem: find the minimum sum from all the a + b pairs
    Time    O(NNK)
    Space   O(N)
    6240 ms, faster than 5.74%
*/
var minDifficulty = function(jobDifficulty, d) {
    const res = dfs(jobDifficulty, 0, d, {})
    if (res === 2**31) {
        return -1
    }
    return res
};

const dfs = (nums, fromIdx, d, ht) => {
    if (fromIdx === nums.length) {
        if (d === 0) {
            return 0
        }
        return 2**31
    }
    
    const key = `${fromIdx},${d}`
    if (key in ht) {
        return ht[key]
    }
    
    let maxLeft = 0
    let minCombo = 2**31
    for (let i = fromIdx; i < nums.length; i++) {
        maxLeft = Math.max(maxLeft, nums[i])
        let maxRight = dfs(nums, i+1, d - 1, ht)
        minCombo = Math.min(minCombo, maxLeft + maxRight)
    }
    ht[key] = minCombo
    return ht[key]
}

/*
    The testing consists of executing tasks in a particular order, with each task having an assigned complexity. ... 
    The goal is to have at least one task sent to the beta testers every day and to plan the tasks in a way that minimizes the overall complexity of the test.
*/