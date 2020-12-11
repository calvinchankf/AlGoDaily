/*
    Recursive DFS
    - the way similar to lc416
    - for each number, we can either include or exclude it the result, therefore we have 2^n options in total

    Time    O(2^n)
    Space   O(2^n) recursion tree
    92 ms, faster than 21.88% 
*/
var subsets = function (nums) {
	const res = []
    const dfs = (cands, chosen) => {
        res.push(chosen)
        for (let i = 0; i < cands.length; i++) {
            const _cands = cands.slice(i+1)
            const _chosen = [...chosen, cands[i]]
            dfs(_cands, _chosen)
        }
    }
    dfs(nums, [])
    return res
};
