/*
    class dynamic programming problem
    - longest common substring
    - similar to lc712
    - see miscellaneous/longest-common-subsequence/idea.png

    ref:
    - https://en.wikipedia.org/wiki/Longest_common_subsequence_problem

    Time    O(AB)
    Space   O(AB)
    108 ms, faster than 74.25%
*/
var longestCommonSubsequence = function(text1, text2) {
    const R = text1.length
    const C = text2.length
    
    const dp = []
    for (let i = 0; i < R; i++) {
        dp.push(Array(C).fill(0))
    }
    
    for (let i = 0; i < R; i++) {
        if (text1[i] == text2[0] || (i > 0 && dp[i-1][0] == 1)) {
            dp[i][0] = 1
        }
    }
    for (let j = 0; j < C; j++) {
        if (text1[0] == text2[j] || (j > 0 && dp[0][j-1] == 1)) {
            dp[0][j] = 1
        }
    }
    
    let res = 0
    for (let i = 0; i < R; i++) {
        for (let j = 0; j < C; j++) {
            
            if (i > 0 && j > 0) {
                if (text1[i] == text2[j]) {
                    dp[i][j] = dp[i-1][j-1] + 1
                } else {
                    dp[i][j] = Math.max(dp[i][j-1], dp[i-1][j])
                }
            }
            
            res = Math.max(res, dp[i][j])
        }
    }
    return res
};