/*
    1st: recursion
    - similar to lc77(combinations)

    Time    O(nCk)
    Space   O(nCk)
    80 ms, faster than 32.73% 
*/
var combinationSum3 = function (k, n) {
	const res = []
    const nums = [1,2,3,4,5,6,7,8,9]
    const dfs = (cands, chosen, total) => {
        if (chosen.length == k) {
            if (total == n) {
                res.push(chosen)
            }
            return
        }
        if (total >= n) {
            return
        }
        for (let i = 0; i < cands.length; i++) {
            const _cands = cands.slice(i+1)
            const _chosen = [...chosen, cands[i]]
            const _total = total + cands[i]
            dfs(_cands, _chosen, _total)
        }
    }
    dfs(nums, [], 0)
    return res
};
