/*
    2nd: zero sum subarray
    - similar to lc325, 525, 560, 930, 1124, 1171
    - rephase: finding a subarray that sum to 0(mod-ed prefix sum)

    e.g.1 [23, 2, 4, 6, 7], 6
    pfs   5   1  5
          ^      ^
    the mod-ed pfs comes back to 5, it means there is a subarray [2,4] can sum up to 6

    e.g.2 [23, 8, 10, 6, 7], 6
    pfs   5   1   5
          ^       ^
    the mod-ed pfs comes back to 5, it means there is a subarray [2,4] can sum up to 6

    Time    O(N)
    Space   O(N)
    84 ms, faster than 76.47% 
*/
var checkSubarraySum = function (nums, k) {
	const n = nums.length
    const ht = {}
    let pfs = 0
    for (let i = 0; i < n; i++) {
        pfs += nums[i]
        pfs = k != 0 ? pfs%k : pfs
        if (pfs == 0 && i > 0) {
            return true
        }
        if (pfs in ht && ht[pfs] + 1 < i) {
            return true
        }
        if (ht[pfs] === undefined) {
            ht[pfs] = i
        }
    }
    return false
};
