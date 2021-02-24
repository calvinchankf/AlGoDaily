/*
    2nd approach: 2 pointers
	- fast pointer is the index of iteration
	- slow pointer is the index which indicates the nums[slow:fast+1] having valid count of zeros
	- learned from others: https://leetcode.com/problems/max-consecutive-ones-iii/discuss/247543/O(n)-Java-Solution-using-sliding-window
	- see ./idea.jpeg

	Time	O(2n)
	Space	O(1)
	60 ms, faster than 100.00%
*/
var longestOnes = function(A, K) {
    const n = A.length
    let zeroCount = 0
    let j = 0
    let res = 0
    for (let i = 0; i < n; i++) {
        if (A[i] == 0) {
            zeroCount += 1
        }
        while (zeroCount > K) {
            const left = A[j]
            j += 1
            if (left == 0) {
                zeroCount -= 1
            }
        }
        res = Math.max(res, i - j + 1)
    }
    return res
};