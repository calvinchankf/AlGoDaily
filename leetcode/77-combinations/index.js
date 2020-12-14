/*
    Implementation similar to permutations
    
    Time    O(nCk)
    Space   O(nCk) due to the recrusion
    648 ms, faster than 39.65%
*/
var combine = function(n, k) {
    const res = []
    const dfs = (start, chosen) => {
        if (chosen.length == k) {
            return res.push(chosen)
        }
        for (let i = start; i <= n; i++) {
            const _chosen = [...chosen, i]
            dfs(i+1, _chosen)
        }
    }
    dfs(1, [])
    return res
};