/*
    1st approach: DP
    - clone and revert the input string
    - do longest common subsequence against the input string

    Time    O(n^2)
    Space   O(n^2)
    304 ms, faster than 34.10%
*/
var longestPalindromeSubseq = function(s) {
    let t = ''
    for (let i = s.length - 1; i >= 0; i--) {
        t += s[i]
    }
    return longestCommonSubsequence(s, t)
};

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