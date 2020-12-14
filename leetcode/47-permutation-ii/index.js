/*
    e.g. 2, -1, 3, -1
    sort it such that nums = -1, -1, 2, 3

    compute permutations of - 1(index 0)
    skip computation for index 1 becos - 1(index 0) has been considered
    compute permutations of 2(index 2)
    compute permutations of 3(index 3)

    time        O(N!) -> O(N x N!)
    space	    O(n!)
    40 ms, faster than 98.27%
*/
var permuteUnique = function (nums) {
    nums.sort((a, b) => a - b)
    
    const res = []
    const dfs = (cands, chosen) => {
        if (cands.length == 0) {
            res.push(chosen)
        }
        for (let i = 0; i < cands.length; i++) {
            if (i-1 >= 0 && cands[i-1] == cands[i]) {
                continue
            }
            const _cands = [...cands.slice(0, i), ...cands.slice(i+1)]
            const _chosen = [...chosen, cands[i]]
            dfs(_cands, _chosen)
        }
    }
    dfs(nums, [])

    return res
};
