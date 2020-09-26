/*
    1st: dynamic programming, hashtable
    - learned from others
    - similar to lc1218

    for each index, store a hashtable of diff : count of longest subsequence
    
    e.g. [20,1,15,3,10,5,8]

    id| num | hashtable
    0 | 20:  { } becomes { -5: 1}
    1 | 1:  { -19: 1 }
    2 | 15: { -5: 1, 14: 1 }
              ^^^^^
    Stop at here, we see that 20 is in fact in our dp, and dp[0][-5] doesnt exist, so we should add ht[-5] = 1 to dp[0]
    Then it becomes...
    2 | 15: { -5: 2, 14: 1 }
              ^^^^^
    3 | 3:  { -17: 1, 2: 1, -12: 1}
    4 | 10: { -10: 1, 9: 1, -5: 1.......again
                            ^^^^^
    Stop at here, we see that 15 is in fact in our dp, and dp[2][-5] also exists, so we can add dp[2][-5] to dp[4][-5]. 
    Then it becomes...
    4 | 10: { -10: 1, 9: 1, -5: 3, 7:1 }
                            ^^^^^
    5 | 5: { -15: 1, 4: 1, -10: 1, 2: 1, -5: 1.....again
    Stop at here, we see that 15 is in fact in our dp, and dp[4][-5] also exists, so we can add dp[4][-5] to dp[5][-5]. 
    Then it becomes...
    5 | 5: { -15: 1, 4: 1, -10: 1, 2: 1, -5: 4 }

    ref:
    - https://leetcode.com/problems/longest-arithmetic-subsequence/discuss/274584/Same-as-LIS-problem-python-solution

    Time    O(N^2)
    Space   O(N)
    3188 ms, faster than 20.63%
*/
var longestArithSeqLength = function (A) {
	const dp = [];
	for (let i = 0; i < A.length; i++) {
		dp[i] = {};
	}

	let res = 0;
	for (let i = 0; i < A.length; i++) {
		for (let j = 0; j < i; j++) {
			const x = A[i];
			const y = A[j];
			const diff = x - y;

			if (dp[i][diff] == undefined) {
				dp[i][diff] = 0;
			}
			if (dp[j][diff] == undefined) {
				dp[j][diff] = 1;
			}

			dp[i][diff] = Math.max(dp[i][diff], dp[j][diff] + 1);
			res = Math.max(res, dp[i][diff]);
		}
	}

	return res;
};
