/*
    1st approach: dynamic programming

    very similar to lc300

    the basic idea is, instead of storing a list of counts [1,1,1,1,1]
    we store a list of [count, possibilites]
    [
        [1:1],
        [1:1],
        [1:1],
        [1:1],
        [1:1],
    ]

    e.g.
    1,   3,   5,   4,   7,   7,   7,   8
    [1,1]<1,1><1,1><1,1><1,1><1,1><1,1><1,1>
         [2,1]<2,1><2,1><2,1><2,1><2,1><2,1>
              [3,1][3,1]<3,1><3,1><3,1><3,1>
                        <4,1><4,1><4,1><4,1>
                        [4,2][4,2][4,2]<4,2>
                                       <5,2>
                                       <5,4>
                                       [5,6]
    Time    O(n^2)
    Space   O(n)
    112 ms, faster than 48.65%
*/
var findNumberOfLIS = function(nums) {
    if (nums.length == 0) {
        return 0
    }
    const n = nums.length
    const dp = Array(n).fill(1)
    const counts = Array(n).fill(1)
    let maxLen = 1
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < i; j++) {
            if (nums[j] < nums[i]) {
                let curLen = dp[j] + 1
                if (curLen > dp[i]) {
                    dp[i] = curLen
                    counts[i] = counts[j]
                } else if (curLen == dp[i]) {
                    counts[i] += counts[j]
                }
            }
        }
        maxLen = Math.max(maxLen, dp[i])
    }
    let res = 0
    for (let i = 0; i < n; i++) {
        if (dp[i] == maxLen) {
            res += counts[i]
        }
    }
    return res
};